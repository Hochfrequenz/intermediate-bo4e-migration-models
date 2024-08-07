import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Rechnungslegung(str, Enum):
    """
    Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen.
    """

    MONATSRECHN = "MONATSRECHN"
    ABSCHL_MONATSRECHN = "ABSCHL_MONATSRECHN"
    ABSCHL_JAHRESRECHN = "ABSCHL_JAHRESRECHN"
    MONATSRECHN_JAHRESRECHN = "MONATSRECHN_JAHRESRECHN"
    VORKASSE = "VORKASSE"
