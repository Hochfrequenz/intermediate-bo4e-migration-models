import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Preismodell(str, Enum):
    """
    Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung.
    """

    FESTPREIS = "FESTPREIS"
    TRANCHE = "TRANCHE"
