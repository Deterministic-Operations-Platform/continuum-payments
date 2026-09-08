"""Vendor-neutral payment workflow domain models."""

from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType
from typing import Any, Mapping


class Direction(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class MessageFamily(str, Enum):
    CREDIT_TRANSFER = "credit-transfer"
    PAYMENT_ACK = "payment-ack"
    PAYMENT_RETURN = "payment-return"
    REQUEST_FOR_PAYMENT = "request-for-payment"
    RETURN_OF_FUNDS = "return-of-funds"


@dataclass(frozen=True, slots=True)
class PaymentEnvelope:
    message_id: str
    family: MessageFamily
    direction: Direction
    payload: Mapping[str, Any]

    def __post_init__(self) -> None:
        if not self.message_id.strip():
            raise ValueError("message_id is required")
        object.__setattr__(self, "payload", MappingProxyType(dict(self.payload)))


@dataclass(frozen=True, slots=True)
class ProcessingResult:
    message_id: str
    route: str
    status: str
    evidence: tuple[str, ...]
