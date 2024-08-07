import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Vertragsform(str, Enum):
    """
    Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen.
    """

    ONLINE = "ONLINE"
    DIREKT = "DIREKT"
    FAX = "FAX"
