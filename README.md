# Cost Center API Load Testing with Locust

This project uses [Locust](https://locust.io/) to simulate realistic load on the Cost Center API and evaluate its performance under stress. It includes automated budget lifecycle operations, secure credential handling, and detailed metrics analysis.

---

## Project Overview

- **Tool**: Locust (Python-based load testing framework)
- **Target**: Cost Center API endpoints (budgets, departments, users, etc.)
- **Purpose**: Measure throughput, latency, failure rates, and scalability
- **Users Simulated**: Up to 300 concurrent users
- **Test Flow**: Login → Create Budget → Update Budget → Delete Budget → Read Operations

---

## Key Features

- **Secure login** using `.env` file and `python-dotenv`
- **Dynamic budget creation** with auto-cleanup to avoid DB pollution
- **Sequential task execution** via `SequentialTaskSet`
- **Realistic user behavior** with randomized payloads
- **Performance reporting** via CSV, HTML, and log files

---

## Setup Instructions

### 1. Environment Variables

Create a `.env` file in the root directory:

```env
LOCUST_EMAIL=your_email@example.com
LOCUST_PASSWORD=your_secure_password
```

### 2. Virtual Environment Activation

Activate your virtual environment

```bash
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # macOS/Linux
```

### 3. Install Dependencies

Install required packages

```bash
pip install -r requirements.txt
```

## Running Tests

Start locust using your configuration file

```bash
locust --config locust.conf
```

N/B: You can access the Locust web interface at http://localhost:8089 to monitor real-time performance metrics.
