from enum import Enum


class Preismodell(str, Enum):
    """
    Bezeichnung der Preismodelle in Ausschreibungen fÃ¼r die Energielieferung.
    """

    FESTPREIS = "FESTPREIS"
    TRANCHE = "TRANCHE"
