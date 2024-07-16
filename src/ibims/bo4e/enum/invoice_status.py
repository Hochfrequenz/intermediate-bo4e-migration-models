from enum import Enum


class InvoiceStatus(str, Enum):
    """
    QuantitiesStatus describes the possible states of a quantity
    """

    RECEIVED = "received"
    IGNORED = "ignored"
    DECLINED = "declined"
    CANCELLED = "cancelled"
    ACCEPTED = "accepted"
    MANUAL_DECISION = "manual_decision"
