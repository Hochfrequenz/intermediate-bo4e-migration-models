import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Verbrauchsart(str, Enum):
    """
    Verbrauchsart einer Marktlokation.
    """

    KL = "KL"
    KLW = "KLW"
    KLWS = "KLWS"
    W = "W"
    WS = "WS"
