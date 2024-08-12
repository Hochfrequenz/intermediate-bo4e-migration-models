from enum import Enum


class Ausschreibungstyp(str, Enum):
    """
    AufzÃ¤hlung fÃ¼r die Typisierung von Ausschreibungen.
    """

    PRIVATRECHTLICH = "PRIVATRECHTLICH"
    OEFFENTLICHRECHTLICH = "OEFFENTLICHRECHTLICH"
    EUROPAWEIT = "EUROPAWEIT"
