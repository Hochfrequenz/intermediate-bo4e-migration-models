import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Tarifkalkulationsmethode(str, Enum):
    """
    Auflistung der verschiedenen Berechnungsmethoden für ein Preisblatt.
    """

    KEINE = "KEINE"
    STAFFELN = "STAFFELN"
    ZONEN = "ZONEN"
    BESTABRECHNUNG_STAFFEL = "BESTABRECHNUNG_STAFFEL"
    PAKETPREIS = "PAKETPREIS"
