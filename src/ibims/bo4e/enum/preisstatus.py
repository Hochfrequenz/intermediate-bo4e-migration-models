from enum import Enum


class Preisstatus(str, Enum):
    """
    Statusinformation fÃ¼r Preise
    """

    VORLAEUFIG = "VORLAEUFIG"
    ENDGUELTIG = "ENDGUELTIG"
