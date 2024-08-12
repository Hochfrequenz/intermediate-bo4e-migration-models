from enum import Enum


class Registeranzahl(str, Enum):
    """
    Die Registeranzahl wird verwendet zur Charakterisierung von ZÃ¤hlern und daraus resultierenden Tarifen.
    """

    EINTARIF = "EINTARIF"
    ZWEITARIF = "ZWEITARIF"
    MEHRTARIF = "MEHRTARIF"
