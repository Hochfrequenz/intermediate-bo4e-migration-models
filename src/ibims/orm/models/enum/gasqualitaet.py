import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Gasqualitaet(str, Enum):
    """
    Unterscheidung für hoch- und niedrig-kalorisches Gas.
    """

    H_GAS = "H_GAS"
    L_GAS = "L_GAS"
