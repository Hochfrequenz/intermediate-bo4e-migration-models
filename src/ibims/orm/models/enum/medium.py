import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Medium(str, Enum):
    """
    Gibt ein physikalisches Medium an.
    """

    STROM = "STROM"
    GAS = "GAS"
    WASSER = "WASSER"
    DAMPF = "DAMPF"
