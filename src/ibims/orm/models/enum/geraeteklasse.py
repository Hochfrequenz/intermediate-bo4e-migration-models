import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Geraeteklasse(str, Enum):
    """
    Auflistung möglicher übergreifenden Geräteklassen.
    """

    WANDLER = "WANDLER"
    KOMMUNIKATIONSEINRICHTUNG = "KOMMUNIKATIONSEINRICHTUNG"
    TECHNISCHE_STEUEREINRICHTUNG = "TECHNISCHE_STEUEREINRICHTUNG"
    MENGENUMWERTER = "MENGENUMWERTER"
    SMARTMETER_GATEWAY = "SMARTMETER_GATEWAY"
    STEUERBOX = "STEUERBOX"
    ZAEHLEINRICHTUNG = "ZAEHLEINRICHTUNG"
