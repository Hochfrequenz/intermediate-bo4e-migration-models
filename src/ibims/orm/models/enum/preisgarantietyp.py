import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Preisgarantietyp(str, Enum):
    """
    Aufzählung der Möglichkeiten für die Vergabe von Preisgarantien
    """

    ALLE_PREISBESTANDTEILE_BRUTTO = "ALLE_PREISBESTANDTEILE_BRUTTO"
    ALLE_PREISBESTANDTEILE_NETTO = "ALLE_PREISBESTANDTEILE_NETTO"
    PREISBESTANDTEILE_OHNE_ABGABEN = "PREISBESTANDTEILE_OHNE_ABGABEN"
    NUR_ENERGIEPREIS = "NUR_ENERGIEPREIS"
