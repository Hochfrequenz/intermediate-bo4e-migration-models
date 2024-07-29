import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Gueltigkeitstyp(str, Enum):
    """
    Übersicht der verschiedenen Gültigkeiten zur Umsetzung von Positiv- bzw. Negativlisten.
    """

    NUR_IN = "NUR_IN"
    NICHT_IN = "NICHT_IN"
    NUR_IN_KOMBINATION_MIT = "NUR_IN_KOMBINATION_MIT"
