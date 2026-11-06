# QuickKart: Inside the Engine Room
## Building Intelligence for India's Digital Native Businesses

**Workshop:** Digital Natives India – 30-minute interactive session  
**Industry:** Quick Commerce  
**Business Scenario:** Order Intelligence and Operational Monitoring  
**Technology:** Python, GitHub, GitHub Copilot and Microsoft Cloud Architecture  
**Difficulty:** Beginner-friendly  
**Python:** 3.10 or later

---

# 1. Business Scenario

Imagine that you are the CTO of QuickKart, a rapidly growing Indian quick-commerce company.

QuickKart operates across Bengaluru, Gurugram, Hyderabad and Pune.

Customers expect:
- Real-time order confirmation.
- Accurate inventory availability.
- Instant payment confirmation.
- Fast delivery.
- Proactive notifications when something goes wrong.

However, the company is experiencing operational challenges:

1. Payments remain pending.
2. Inventory becomes unavailable after an order is placed.
3. Delivery assignments are delayed.
4. Operations teams struggle to identify problematic orders.

Your challenge is to build a simple Order Intelligence Engine that identifies operational exceptions.

**Business objective:** Identify unhealthy orders before they become customer complaints.

This workshop uses fictional business data. It does not connect to real payment gateways, inventory systems or customer accounts.

# 2. What You Will Build

You will create a small Python application that:

1. Reads order information from a JSON file.
2. Evaluates payment and inventory status.
3. Identifies orders requiring attention.
4. Classifies orders as HEALTHY, AT_RISK or COMPLETED.
5. Runs automated unit tests.

The application demonstrates the basic business logic behind a digital-native operational platform.

# 3. Architecture

```text
                QuickKart Customer
                        |
                        v
                 Order Management
                        |
                        v
                 orders.json
                        |
                        v
             Order Intelligence Engine
                        |
              +---------+---------+
              |         |         |
              v         v         v
           Payment   Inventory  Delivery
           Status     Status     Status
              |         |         |
              +---------+---------+
                        |
                        v
                 Risk Assessment
                        |
              +---------+---------+
              |         |         |
              v         v         v
           HEALTHY   AT_RISK   COMPLETED
```

This is a simplified teaching architecture. A production implementation would use persistent storage, asynchronous event processing, authentication, monitoring and reliable payment reconciliation.

# 4. Prerequisites

Install or verify:

- Python 3.10+
- Visual Studio Code
- Git
- GitHub account (optional for the local demonstration)

Verify Python:

```powershell
python --version
```

Verify Git:

```powershell
git --version
```

No external Python packages are required.

# 5. Step 1 – Create the Repository

Open PowerShell.

Create the project directory:

```powershell
mkdir quickkart
cd quickkart
```

Create the application directories:

```powershell
mkdir app
mkdir data
mkdir tests
```

Create the required files:

```powershell
New-Item app/__init__.py -ItemType File
New-Item app/order_intelligence.py -ItemType File
New-Item data/orders.json -ItemType File
New-Item tests/test_order_intelligence.py -ItemType File
```

Open the repository in Visual Studio Code:

```powershell
code .
```

Your project structure should look like this:

```text
quickkart/
│
├── README.md
│
├── app/
│   ├── __init__.py
│   └── order_intelligence.py
│
├── data/
│   └── orders.json
│
└── tests/
    └── test_order_intelligence.py
```

# 6. Step 2 – Create Sample Order Data

Open:

`data/orders.json`

Add the following sample data:

```json
[
  {
    "order_id": "QK-1001",
    "city": "Bengaluru",
    "payment_status": "PAID",
    "inventory_status": "RESERVED",
    "delivery_status": "ASSIGNED",
    "created_minutes_ago": 8
  },
  {
    "order_id": "QK-1002",
    "city": "Gurugram",
    "payment_status": "PENDING",
    "inventory_status": "RESERVED",
    "delivery_status": "NOT_ASSIGNED",
    "created_minutes_ago": 19
  },
  {
    "order_id": "QK-1003",
    "city": "Hyderabad",
    "payment_status": "PAID",
    "inventory_status": "OUT_OF_STOCK",
    "delivery_status": "NOT_ASSIGNED",
    "created_minutes_ago": 12
  },
  {
    "order_id": "QK-1004",
    "city": "Pune",
    "payment_status": "PAID",
    "inventory_status": "RESERVED",
    "delivery_status": "DELIVERED",
    "created_minutes_ago": 42
  }
]
```

## Understand the business data

| Field | Meaning |
|---|---|
| order_id | Unique order identifier |
| city | Customer order location |
| payment_status | Payment processing state |
| inventory_status | Stock reservation state |
| delivery_status | Fulfilment state |
| created_minutes_ago | Order age in minutes |

**Trainer discussion:**

Ask participants why payment status, inventory status and delivery status should be maintained independently.

Expected answer: Each is a separate business capability and may change independently.

# 7. Step 3 – Build the Order Intelligence Engine

Open:

`app/order_intelligence.py`

Add the complete implementation:

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ORDERS_FILE = ROOT / "data
