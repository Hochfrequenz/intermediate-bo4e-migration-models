import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Kostenklasse(str, Enum):
    """
    Kostenklassen bilden die oberste Ebene der verschiedenen Kosten.
    In der Regel werden die Gesamtkosten einer Kostenklasse in einer App berechnet.
    """

    FREMDKOSTEN = "FREMDKOSTEN"
    BESCHAFFUNG = "BESCHAFFUNG"
    SELBSTKOSTEN = "SELBSTKOSTEN"
    MARGEN = "MARGEN"
    ENERGIEVERSORGUNGSKOSTEN = "ENERGIEVERSORGUNGSKOSTEN"
