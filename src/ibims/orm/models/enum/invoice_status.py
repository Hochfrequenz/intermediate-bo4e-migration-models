import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class InvoiceStatus(str, Enum):
    """
    InvoiceStatus describes the possible states of an invoice
    """

    RECEIVED = "received"
    IGNORED = "ignored"
    DECLINED = "declined"
    CANCELLED = "cancelled"
    ACCEPTED = "accepted"
    MANUAL_DECISION = "manual_decision"
