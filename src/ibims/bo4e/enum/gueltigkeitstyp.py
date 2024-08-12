from enum import Enum


class Gueltigkeitstyp(str, Enum):
    """
    Ãœbersicht der verschiedenen GÃ¼ltigkeiten zur Umsetzung von Positiv- bzw. Negativlisten.
    """

    NUR_IN = "NUR_IN"
    NICHT_IN = "NICHT_IN"
    NUR_IN_KOMBINATION_MIT = "NUR_IN_KOMBINATION_MIT"
