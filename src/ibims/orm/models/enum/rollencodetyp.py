import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Rollencodetyp(str, Enum):
    """
    Gibt den Codetyp einer Rolle, beispielsweise einer Marktrolle, an.
    """

    BDEW = "BDEW"
    DVGW = "DVGW"
    GLN = "GLN"
