import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class AufAbschlagstyp(str, Enum):
    """
    Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt.
    """

    RELATIV = "RELATIV"
    ABSOLUT = "ABSOLUT"
