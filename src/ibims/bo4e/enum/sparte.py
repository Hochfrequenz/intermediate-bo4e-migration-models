from enum import Enum


class Sparte(str, Enum):
    """
    UnterscheidungsmÃ¶glichkeiten fÃ¼r die Sparte.
    """

    STROM = "STROM"
    GAS = "GAS"
    FERNWAERME = "FERNWAERME"
    NAHWAERME = "NAHWAERME"
    WASSER = "WASSER"
    ABWASSER = "ABWASSER"
    STROM_UND_GAS = "STROM_UND_GAS"
