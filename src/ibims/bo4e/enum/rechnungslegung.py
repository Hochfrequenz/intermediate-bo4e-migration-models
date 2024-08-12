from enum import Enum


class Rechnungslegung(str, Enum):
    """
    AufzÃ¤hlung der MÃ¶glichkeiten zur Rechnungslegung in Ausschreibungen.
    """

    MONATSRECHN = "MONATSRECHN"
    ABSCHL_MONATSRECHN = "ABSCHL_MONATSRECHN"
    ABSCHL_JAHRESRECHN = "ABSCHL_JAHRESRECHN"
    MONATSRECHN_JAHRESRECHN = "MONATSRECHN_JAHRESRECHN"
    VORKASSE = "VORKASSE"
