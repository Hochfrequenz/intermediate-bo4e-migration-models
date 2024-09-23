import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class QuantitiesStatus(str, Enum):
    """
    QuantitiesStatus describes the possible states of a quantity
    """

    CANCELLED = "CANCELLED"
    DECISION = "DECISION"
    IGNORED = "IGNORED"
    OBJECTED = "OBJECTED"
    RECEIVED = "RECEIVED"
    VALID = "VALID"
