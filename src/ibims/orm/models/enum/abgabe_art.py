import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class AbgabeArt(str, Enum):
    """
    Art der Konzessionsabgabe
    """

    KAS = "KAS"
    SA = "SA"
    SAS = "SAS"
    TA = "TA"
    TAS = "TAS"
    TK = "TK"
    TKS = "TKS"
    TS = "TS"
    TSS = "TSS"
