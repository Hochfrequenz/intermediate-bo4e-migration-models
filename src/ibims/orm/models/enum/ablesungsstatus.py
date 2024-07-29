import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Ablesungsstatus(str, Enum):
    """
    State of the reading
    """

    GUELTIG = "GUELTIG"
    UNGUELTIG = "UNGUELTIG"
    ABGERECHNET = "ABGERECHNET"
