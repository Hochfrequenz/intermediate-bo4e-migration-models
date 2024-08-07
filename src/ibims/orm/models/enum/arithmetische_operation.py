import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class ArithmetischeOperation(str, Enum):
    """
    Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
    """

    ADDITION = "ADDITION"
    SUBTRAKTION = "SUBTRAKTION"
    MULTIPLIKATION = "MULTIPLIKATION"
    DIVISION = "DIVISION"
