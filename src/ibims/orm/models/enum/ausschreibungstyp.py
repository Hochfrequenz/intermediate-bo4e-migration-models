import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Ausschreibungstyp(str, Enum):
    """
    Aufzählung für die Typisierung von Ausschreibungen.
    """

    PRIVATRECHTLICH = "PRIVATRECHTLICH"
    OEFFENTLICHRECHTLICH = "OEFFENTLICHRECHTLICH"
    EUROPAWEIT = "EUROPAWEIT"
