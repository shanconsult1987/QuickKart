
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
        self.assertIn("Payment pending", result["reasons"])

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
