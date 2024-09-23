import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Marktrolle(str, Enum):
    """
    Diese Rollen kann ein Marktteilnehmer einnehmen.
    """

    BTR = "BTR"
    BIKO = "BIKO"
    BKV = "BKV"
    DP = "DP"
    EIV = "EIV"
    ESA = "ESA"
    KN = "KN"
    LF = "LF"
    MGV = "MGV"
    MSB = "MSB"
    NB = "NB"
    RB = "RB"
    UENB = "UENB"
