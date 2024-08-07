import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Lokationstyp(str, Enum):
    """
    Gibt an, ob es sich um eine Markt- oder Messlokation handelt.
    """

    MALO = "MALO"
    MELO = "MELO"
