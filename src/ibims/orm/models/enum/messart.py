import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Messart(str, Enum):
    """
    Gibt an, auf welche Art gemessen wurde.
    """

    AKTUELLERWERT = "AKTUELLERWERT"
    MITTELWERT = "MITTELWERT"
    MAXIMALWERT = "MAXIMALWERT"
