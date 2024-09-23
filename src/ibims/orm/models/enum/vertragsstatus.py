import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Vertragsstatus(str, Enum):
    """
    Abbildung einer Statusinformation für Verträge.
    """

    IN_ARBEIT = "IN_ARBEIT"
    UEBERMITTELT = "UEBERMITTELT"
    ANGENOMMEN = "ANGENOMMEN"
    AKTIV = "AKTIV"
    ABGELEHNT = "ABGELEHNT"
    WIDERRUFEN = "WIDERRUFEN"
    STORNIERT = "STORNIERT"
    GEKUENDIGT = "GEKUENDIGT"
    BEENDET = "BEENDET"
