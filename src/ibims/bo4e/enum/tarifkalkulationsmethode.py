from enum import Enum


class Tarifkalkulationsmethode(str, Enum):
    """
    Auflistung der verschiedenen Berechnungsmethoden fÃ¼r ein Preisblatt.
    """

    KEINE = "KEINE"
    STAFFELN = "STAFFELN"
    ZONEN = "ZONEN"
    BESTABRECHNUNG_STAFFEL = "BESTABRECHNUNG_STAFFEL"
    PAKETPREIS = "PAKETPREIS"
