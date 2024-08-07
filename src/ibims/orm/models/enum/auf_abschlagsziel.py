import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class AufAbschlagsziel(str, Enum):
    """
    Der Preis, auf den sich ein Auf- oder Abschlag bezieht.
    """

    ARBEITSPREIS_EINTARIF = "ARBEITSPREIS_EINTARIF"
    ARBEITSPREIS_HT = "ARBEITSPREIS_HT"
    ARBEITSPREIS_NT = "ARBEITSPREIS_NT"
    ARBEITSPREIS_HT_NT = "ARBEITSPREIS_HT_NT"
    GRUNDPREIS = "GRUNDPREIS"
    GESAMTPREIS = "GESAMTPREIS"
