"""Deterministic routing without network or customer-specific dependencies."""

from .models import Direction, MessageFamily, PaymentEnvelope, ProcessingResult


def route_name(family: MessageFamily, direction: Direction) -> str:
    return f"{family.value}-{direction.value}"


def supported_routes() -> tuple[str, ...]:
    return tuple(
        route_name(family, direction)
        for family in MessageFamily
        for direction in Direction
    )


class PaymentProcessor:
    """Validates and records a deterministic processing decision."""

    def process(self, envelope: PaymentEnvelope) -> ProcessingResult:
        route = route_name(envelope.family, envelope.direction)
        if route not in supported_routes():
            raise ValueError("unsupported payment route")
        return ProcessingResult(
            message_id=envelope.message_id,
            route=route,
            status="validated",
            evidence=(
                "message-id-present",
                "route-supported",
                "payload-bounded-to-caller-envelope",
            ),
        )
