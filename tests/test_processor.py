import unittest

from continuum_payments import Direction, MessageFamily, PaymentEnvelope, PaymentProcessor, supported_routes


class PaymentProcessorTests(unittest.TestCase):
    def test_all_direction_and_family_combinations_are_explicit(self) -> None:
        self.assertEqual(len(supported_routes()), 10)
        self.assertIn("credit-transfer-inbound", supported_routes())
        self.assertIn("return-of-funds-outbound", supported_routes())

    def test_processing_is_deterministic(self) -> None:
        envelope = PaymentEnvelope(
            message_id="synthetic-message-001",
            family=MessageFamily.REQUEST_FOR_PAYMENT,
            direction=Direction.INBOUND,
            payload={"amount": "10.00", "currency": "USD"},
        )
        first = PaymentProcessor().process(envelope)
        second = PaymentProcessor().process(envelope)
        self.assertEqual(first, second)
        self.assertEqual(first.status, "validated")

    def test_blank_message_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PaymentEnvelope(
                message_id=" ",
                family=MessageFamily.PAYMENT_ACK,
                direction=Direction.OUTBOUND,
                payload={},
            )


if __name__ == "__main__":
    unittest.main()
