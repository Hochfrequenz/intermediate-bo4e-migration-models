import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Wertermittlungsverfahren(str, Enum):
    """
    Gibt an, ob es sich um eine Prognose oder eine Messung handelt, beispielsweise bei der Abbildung eines Verbrauchs.
    """

    PROGNOSE = "PROGNOSE"
    MESSUNG = "MESSUNG"
