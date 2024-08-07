import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Waermenutzung(str, Enum):
    """
    Wärmenutzung Marktlokation
    """

    SPEICHERHEIZUNG = "SPEICHERHEIZUNG"
    WAERMEPUMPE = "WAERMEPUMPE"
    DIREKTHEIZUNG = "DIREKTHEIZUNG"
