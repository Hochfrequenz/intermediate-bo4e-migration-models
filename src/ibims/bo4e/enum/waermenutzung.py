from enum import Enum


class Waermenutzung(str, Enum):
    """
    WÃ¤rmenutzung Marktlokation
    """

    SPEICHERHEIZUNG = "SPEICHERHEIZUNG"
    WAERMEPUMPE = "WAERMEPUMPE"
    DIREKTHEIZUNG = "DIREKTHEIZUNG"
