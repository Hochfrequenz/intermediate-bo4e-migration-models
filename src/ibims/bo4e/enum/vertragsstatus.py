from enum import Enum


class Vertragsstatus(str, Enum):
    """
    Abbildung einer Statusinformation fÃ¼r VertrÃ¤ge.
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
