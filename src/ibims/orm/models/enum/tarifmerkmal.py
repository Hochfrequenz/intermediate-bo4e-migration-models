import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Tarifmerkmal(str, Enum):
    """
    Produktmerkmale im Zusammenhang mit der Tarifdefinition.
    """

    STANDARD = "STANDARD"
    VORKASSE = "VORKASSE"
    PAKET = "PAKET"
    KOMBI = "KOMBI"
    FESTPREIS = "FESTPREIS"
    BAUSTROM = "BAUSTROM"
    HAUSLICHT = "HAUSLICHT"
    HEIZSTROM = "HEIZSTROM"
    ONLINE = "ONLINE"
