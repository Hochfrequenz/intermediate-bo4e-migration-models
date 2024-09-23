import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Preistyp(str, Enum):
    """
    Aufschlüsselung der Preistypen in Tarifen.
    """

    GRUNDPREIS = "GRUNDPREIS"
    ARBEITSPREIS_EINTARIF = "ARBEITSPREIS_EINTARIF"
    ARBEITSPREIS_HT = "ARBEITSPREIS_HT"
    ARBEITSPREIS_NT = "ARBEITSPREIS_NT"
    LEISTUNGSPREIS = "LEISTUNGSPREIS"
    MESSPREIS = "MESSPREIS"
    ENTGELT_ABLESUNG = "ENTGELT_ABLESUNG"
    ENTGELT_ABRECHNUNG = "ENTGELT_ABRECHNUNG"
    ENTGELT_MSB = "ENTGELT_MSB"
    PROVISION = "PROVISION"
