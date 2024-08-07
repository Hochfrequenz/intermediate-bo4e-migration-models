import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Registeranzahl(str, Enum):
    """
    Die Registeranzahl wird verwendet zur Charakterisierung von Zählern und daraus resultierenden Tarifen.
    """

    EINTARIF = "EINTARIF"
    ZWEITARIF = "ZWEITARIF"
    MEHRTARIF = "MEHRTARIF"
