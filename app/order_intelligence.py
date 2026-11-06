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
