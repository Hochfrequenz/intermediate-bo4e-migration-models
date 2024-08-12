from enum import Enum


class Vertragsform(str, Enum):
    """
    AufzÃ¤hlung der MÃ¶glichkeiten zu Vertragsformen in Ausschreibungen.
    """

    ONLINE = "ONLINE"
    DIREKT = "DIREKT"
    FAX = "FAX"
