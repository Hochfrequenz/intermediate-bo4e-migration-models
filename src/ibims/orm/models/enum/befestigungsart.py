import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Befestigungsart(str, Enum):
    """
    Befestigungsart von Zählern
    """

    STECKTECHNIK = "STECKTECHNIK"
    DREIPUNKT = "DREIPUNKT"
    HUTSCHIENE = "HUTSCHIENE"
    EINSTUTZEN = "EINSTUTZEN"
    ZWEISTUTZEN = "ZWEISTUTZEN"
