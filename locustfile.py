import os
import random
from dotenv import load_dotenv
from locust import HttpUser, SequentialTaskSet, task, between

load_dotenv()

class BudgetLifecycle(SequentialTaskSet):
    def on_start(self):
        email = os.getenv("LOCUST_EMAIL")
        password = os.getenv("LOCUST_PASSWORD")
        payload = {"email": email, "password": password}
        with self.client.post("/api/users/login", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Login failed")

    @task
    def create_budget(self):
        payload = {"name": f"Budget Automation {random.randint(1,1000)}", "description": "Test"}
        with self.client.post("/api/budgets", json=payload, catch_response=True) as response:
            if response.status_code == 201 and "data" in response.json() and "budget_id" in response.json()["data"]:
                self.budget_id = response.json()["data"]["budget_id"]
                response.success()
            else:
                response.failure("Failed to create budget")

    @task
    def update_budget(self):
        if hasattr(self, "budget_id"):
            payload = {"name": f"Updated Budget Automation {random.randint(1,1000)}"}
            self.client.put(f"/api/budgets/{self.budget_id}", json=payload)

    @task
    def delete_budget(self):
        if hasattr(self, "budget_id"):
            with self.client.delete(f"/api/budgets/{self.budget_id}", catch_response=True) as response:
                if response.status_code == 204:
                    response.success()
                else:
                    response.failure("Failed to delete budget")

class CostCenterUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [BudgetLifecycle]
    print(BudgetLifecycle.delete_count, BudgetLifecycle.update_count, BudgetLifecycle.create_count)

    # @task
    # def create_budget(self):
    #     payload = {"name": f"Budget Automation {random.randint(1,1000)}", "description": "Test"}
    #     with self.client.post("/api/budgets", json=payload, catch_response=True) as response:
    #         print(response.json()['data']['budget_id'], response.status_code)
    #         if response.status_code == 201:
    #             print('Here')
    #             CostCenterUser.budget_id = response.json()['data']["budget_id"]
    #             response.success()
    #         else:
    #             response.failure("Failed to create budget")

    # @task
    # def update_budget(self):
    #     if CostCenterUser.budget_id:
    #         payload = {"name": f"Updated Budget Automation {random.randint(1, 1000)}"}
    #         self.client.put(f"/api/budgets/{CostCenterUser.budget_id}", json=payload)
    #     else:
    #         print("No budget ID available for update")

    # @task
    # def delete_budget(self):
    #     if CostCenterUser.budget_id:
    #         self.client.delete(f"/api/budgets/{CostCenterUser.budget_id}")
    #     else:
    #         print("No budget ID available for deletion")

    # @task
    # def get_budgets(self):
    #     self.client.get("/api/budgets")

    # @task
    # def get_budget(self):
    #     if CostCenterUser.budget_id:
    #         self.client.get(f"/api/budgets/{CostCenterUser.budget_id}")
    #     else:
    #         print("No budget ID is available")
 

    # @task
    # def get_budget_items(self):
    #     self.client.get("/api/budget_items")

    # # @task
    # # def create_budget_item(self):
    # #     payload = {
    # #         "name": f"NHIF {random.randint(1, 1000)}",
    # #         "budget_id": "f321c19d-eec0-47e8-b73a-f9b0b852ff5d"
    # #     }
    # #     self.client.post("/api/budget_items", json=payload)

    # @task
    # def get_departments(self):
    #     self.client.get("/api/departments")

    # # @task
    # # def create_department(self):
    # #     payload = {
    # #         "name": f"Information Technology (IT) {random.randint(1,1000)}",
    # #         "description": "Oversees technology infrastructure, software systems, cybersecurity, technical support, and digital transformation initiatives."
    # #     }
    # #     self.client.post("/api/departments", json=payload)


    # @task
    # def get_users(self):
    #     self.client.get("/api/users")

    # @task
    # def get_permissions(self):
    #     self.client.get("/api/permissions")

    # @task
    # def get_requisitions(self):
    #     self.client.get("/api/requisitions")

    # @task
    # def get_lpos(self):
    #     self.client.get("/api/lpos")

    # @task
    # def get_vouchers(self):
    #     self.client.get("/api/vouchers")

    # def on_start(self):
    #     email = os.getenv("LOCUST_EMAIL")
    #     password = os.getenv("LOCUST_PASSWORD")

    #     if not email or not password:
    #         print("Missing credentials")
    #         return
    #     payload = {
    #         "email": email,
    #         "password": password
    #     }
    #     with self.client.post("/api/users/login", json=payload, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success
    #         else:
    #             response.failure("Login failed")