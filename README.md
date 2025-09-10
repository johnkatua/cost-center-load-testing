# 📊 Cost Center API Load Testing with Locust

This project uses [Locust](https://locust.io/) to simulate realistic load on the Cost Center API and evaluate its performance under stress. It includes automated budget lifecycle operations, secure credential handling, and detailed metrics analysis.

---

## 🚀 Project Overview

- **Tool**: Locust (Python-based load testing framework)
- **Target**: Cost Center API endpoints (budgets, departments, users, etc.)
- **Purpose**: Measure throughput, latency, failure rates, and scalability
- **Users Simulated**: Up to 300 concurrent users
- **Test Flow**: Login → Create Budget → Update Budget → Delete Budget → Read Operations

---

## 🧪 Key Features

- ✅ **Secure login** using `.env` file and `python-dotenv`
- ✅ **Dynamic budget creation** with auto-cleanup to avoid DB pollution
- ✅ **Sequential task execution** via `SequentialTaskSet`
- ✅ **Realistic user behavior** with randomized payloads
- ✅ **Performance reporting** via CSV, HTML, and log files

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
LOCUST_EMAIL=your_email@example.com
LOCUST_PASSWORD=your_secure_password
```

## Virtual Environment Setup

Run the below command to activate virtual environment:-

```bash
source .venv/Script/Activate
```

## Install Dependencies

Run the below command to install the project dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
locust --config locust.conf
```
