import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Sparte(str, Enum):
    """
    Unterscheidungsmöglichkeiten für die Sparte.
    """

    STROM = "STROM"
    GAS = "GAS"
    FERNWAERME = "FERNWAERME"
    NAHWAERME = "NAHWAERME"
    WASSER = "WASSER"
    ABWASSER = "ABWASSER"
    STROM_UND_GAS = "STROM_UND_GAS"
