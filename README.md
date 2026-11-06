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

ORDERS_FILE = ROOT / "data" / "orders.json"


def assess_order(order):

    reasons = []

    if (
        order["payment_status"] == "PENDING"
        and order["created_minutes_ago"] >= 10
    ):
        reasons.append("Payment pending")

    if order["inventory_status"] == "OUT_OF_STOCK":
        reasons.append("Inventory unavailable")

    status = "AT_RISK" if reasons else "HEALTHY"

    if order["delivery_status"] == "DELIVERED":
        status = "COMPLETED"
        reasons = ["Order delivered"]

    return {
        "order_id": order["order_id"],
        "status": status,
        "reasons": reasons
    }


def main():

    orders = json.loads(
        ORDERS_FILE.read_text(encoding="utf-8")
    )

    print("QUICKKART ORDER INTELLIGENCE")
    print("-" * 45)

    for order in orders:

        result = assess_order(order)

        print(
            result["order_id"],
            result["status"],
            result["reasons"]
        )


if __name__ == "__main__":
    main()
```

## Understand the implementation

**A. Load the JSON data**

```python
orders = json.loads(
    ORDERS_FILE.read_text(encoding="utf-8")
)
```

Reads the order information from the JSON file and converts it into Python objects.

**B. Check payment delays**

```python
if (
    order["payment_status"] == "PENDING"
    and order["created_minutes_ago"] >= 10
):
    reasons.append("Payment pending")
```

If a payment remains pending for 10 minutes or more, the order is marked as requiring attention.

**C. Check inventory**

```python
if order["inventory_status"] == "OUT_OF_STOCK":
    reasons.append("Inventory unavailable")
```

If stock is unavailable, the system flags the order.

**D. Determine the order status**

```python
status = "AT_RISK" if reasons else "HEALTHY"
```

Orders with no identified exceptions are classified as healthy.

Delivered orders are classified as completed.

# 8. Step 4 – Run the Application

From the repository root:

```powershell
python -m app.order_intelligence
```

Expected output:

```text
QUICKKART ORDER INTELLIGENCE
---------------------------------------------
QK-1001 HEALTHY []
QK-1002 AT_RISK ['Payment pending']
QK-1003 AT_RISK ['Inventory unavailable']
QK-1004 COMPLETED ['Order delivered']
```

## Interpret the results

| Order | Status | Business interpretation |
|---|---|---|
| QK-1001 | HEALTHY | Payment and inventory are fine; delivery assigned |
| QK-1002 | AT_RISK | Payment has remained pending |
| QK-1003 | AT_RISK | Inventory is unavailable |
| QK-1004 | COMPLETED | Order delivered successfully |

**Ask participants:**

What should QuickKart do when an order is marked AT_RISK?

Possible responses:
- Investigate payment status.
- Recheck inventory.
- Trigger a customer notification.
- Initiate a refund or substitution workflow when appropriate.
- Escalate to the operations team.

# 9. Step 5 – Create Unit Tests

Open:

`tests/test_order_intelligence.py`

Add the complete test implementation:

```python
import unittest

from app.order_intelligence import assess_order


class TestOrderIntelligence(unittest.TestCase):

    def test_healthy_order(self):

        order = {
            "order_id": "QK-1001",
            "payment_status": "PAID",
            "inventory_status": "RESERVED",
            "delivery_status": "ASSIGNED",
            "created_minutes_ago": 8
        }

        result = assess_order(order)

        self.assertEqual(result["status"], "HEALTHY")
        self.assertEqual(result["reasons"], [])

    def test_payment_pending(self):

        order = {
            "order_id": "QK-1002",
            "payment_status": "PENDING",
            "inventory_status": "RESERVED",
            "delivery_status": "NOT_ASSIGNED",
            "created_minutes_ago": 19
        }

        result = assess_order(order)

        self.assertEqual(result["status"], "AT_RISK")
        self.assertIn(
            "Payment pending",
            result["reasons"]
        )

    def test_inventory_unavailable(self):

        order = {
            "order_id": "QK-1003",
            "payment_status": "PAID",
            "inventory_status": "OUT_OF_STOCK",
            "delivery_status": "NOT_ASSIGNED",
            "created_minutes_ago": 12
        }

        result = assess_order(order)

        self.assertEqual(result["status"], "AT_RISK")
        self.assertIn(
            "Inventory unavailable",
            result["reasons"]
        )

    def test_completed_order(self):

        order = {
            "order_id": "QK-1004",
            "payment_status": "PAID",
            "inventory_status": "RESERVED",
            "delivery_status": "DELIVERED",
            "created_minutes_ago": 42
        }

        result = assess_order(order)

        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(
            result["reasons"],
            ["Order delivered"]
        )

    def test_payment_pending_under_threshold(self):

        order = {
            "order_id": "QK-1005",
            "payment_status": "PENDING",
            "inventory_status": "RESERVED",
            "delivery_status": "NOT_ASSIGNED",
            "created_minutes_ago": 5
        }

        result = assess_order(order)

        self.assertEqual(result["status"], "HEALTHY")


if __name__ == "__main__":
    unittest.main()
```

# 10. Step 6 – Execute Unit Tests

Run:

```powershell
python -m unittest discover -s tests -v
```

Expected result:

```text
test_completed_order ... ok
test_healthy_order ... ok
test_inventory_unavailable ... ok
test_payment_pending ... ok
test_payment_pending_under_threshold ... ok

Ran 5 tests

OK
```

## Why are unit tests important?

In a Digital Native company, business logic changes frequently.

For example:
- Payment timeout rules may change.
- Inventory reservation policies may change.
- New order states may be introduced.
- Delivery SLA thresholds may be updated.

Unit tests help ensure that existing behaviour continues to work when developers modify the application.

# 11. Step 7 – Explore with GitHub Copilot

Open GitHub Copilot Chat in Visual Studio Code.

Try these prompts.

**Prompt 1 – Understand the code**

```text
Explain the QuickKart order intelligence application.
Explain how assess_order works and identify all business rules.
```

**Prompt 2 – Add a new business rule**

```text
Modify the application to identify orders
where payment is PAID but delivery is NOT_ASSIGNED
for more than 15 minutes.

Keep the existing application structure.
Add a corresponding unit test.
```

**Prompt 3 – Improve testing**

```text
Review the existing unit tests.

Identify missing edge cases and generate
additional unittest test cases.

Do not introduce external dependencies.
```

**Prompt 4 – Generate documentation**

```text
Generate developer documentation explaining:
- Business workflow
- Order lifecycle
- Business rules
- Test scenarios
- Known limitations
```

# 12. Step 8 – Understand the Production Architecture

The demonstration uses a JSON file and a local Python function.

A production QuickKart platform would need a more sophisticated architecture.

```text
             Customer Mobile App
                     |
                     v
              API Management
                     |
          +----------+----------+
          |          |          |
          v          v          v
        Order     Payment   Inventory
        Service   Service    Service
          |          |          |
          +----------+----------+
                     |
                     v
              Event Platform
             Service Bus /
              Event Hubs
                     |
          +----------+----------+
          |                     |
          v                     v
      Delivery              Analytics
      Service                Platform
          |                     |
          v                     v
     Notifications          Fabric
                                |
                                v
                         AI Intelligence
```

## Microsoft technology mapping

| Capability | Microsoft technology |
|---|---|
| API management | Azure API Management |
| Application hosting | Azure Container Apps |
| Microservices | Azure Kubernetes Service |
| Messaging | Azure Service Bus |
| Event streaming | Azure Event Hubs |
| Operational database | Azure SQL / Cosmos DB |
| Analytics | Microsoft Fabric |
| AI applications | Azure AI Foundry |
| Enterprise retrieval | Azure AI Search |
| Development | GitHub Copilot |
| CI/CD | GitHub Actions |
| Security | Microsoft Defender for Cloud |
| Monitoring | Azure Monitor |

These are possible architectural choices, not mandatory dependencies for the workshop.

# 13. Step 9 – Digital Native Terminology

Understand the vocabulary used in engineering and business conversations.

| Term | Meaning |
|---|---|
| GMV | Gross Merchandise Value |
| Take Rate | Platform revenue as a percentage of transaction value |
| CAC | Customer Acquisition Cost |
| LTV | Lifetime Value |
| Churn | Customer attrition |
| Cohort | Group of users analysed over time |
| Dark Store | Local fulfilment centre |
| P99 Latency | 99th percentile request latency |
| Idempotency | Safe repetition of an operation |
| Reconciliation | Matching transaction records |
| Event-Driven Architecture | Architecture driven by published events |
| RAG | Retrieval-Augmented Generation |
| SLO | Service-Level Objective |
| Feature Flag | Mechanism to enable or disable functionality |

# 14. Step 10 – Workshop Challenges

Try these exercises after completing the demonstration.

### Challenge 1: Payment intelligence

Add a rule to identify payments pending for more than 5 minutes.

### Challenge 2: Delivery monitoring

Identify paid orders that have not been assigned to a delivery partner after 15 minutes.

### Challenge 3: Multiple exceptions

Ensure that an order can report multiple reasons for being at risk.

### Challenge 4: AI-powered operations

Design an AI assistant that:
- Reads order exception reports.
- Retrieves relevant operational runbooks.
- Explains the root cause.
- Recommends corrective action.
- Requests human approval before consequential actions.

### Challenge 5: Production readiness

Discuss how the application would change if QuickKart processed 100,000 orders per minute.

Consider:
- Horizontal scaling.
- Event streaming.
- Distributed transactions.
- Observability.
- Data partitioning.
- Security.
- Disaster recovery.

# 15. Step 11 – GitHub Repository

Initialise Git:

```powershell
git init

git add .

git commit -m "Initial QuickKart order intelligence application"
```

Create a repository on GitHub, then connect it:

```powershell
git branch -M main

git remote add origin https://github.com/YOUR-USERNAME/quickkart.git

git push -u origin main
```

Replace the repository URL with your own.

# 16. Final Learning Outcomes

After completing this workshop, participants should understand:

1. How Indian Digital Native companies structure their business models.
2. The terminology used by product and engineering teams.
3. How modern digital-native systems are architected.
4. How order, payment, inventory and delivery systems interact.
5. How Python can demonstrate business intelligence rules.
6. How unit testing supports rapid software development.
7. How GitHub Copilot can assist developers.
8. How Microsoft technologies map to industry challenges.
9. Where AI agents can add value to operational workflows.

---

## Final takeaway

Digital Natives do not simply use technology to automate existing processes.

They build their business models around software, data, APIs, automation and increasingly AI.

**Start with the business problem. Understand the systems. Follow the events and data. Then introduce the right technology.**
