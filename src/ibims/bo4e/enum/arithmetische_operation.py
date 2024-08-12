from enum import Enum


class ArithmetischeOperation(str, Enum):
    """
    Mit dieser AufzÃ¤hlung kÃ¶nnen arithmetische Operationen festgelegt werden.
    """

    ADDITION = "ADDITION"
    SUBTRAKTION = "SUBTRAKTION"
    MULTIPLIKATION = "MULTIPLIKATION"
    DIVISION = "DIVISION"
