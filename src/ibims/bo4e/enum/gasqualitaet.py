from enum import Enum


class Gasqualitaet(str, Enum):
    """
    Unterscheidung fÃ¼r hoch- und niedrig-kalorisches Gas.
    """

    H_GAS = "H_GAS"
    L_GAS = "L_GAS"
