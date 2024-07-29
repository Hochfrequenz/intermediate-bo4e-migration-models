import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Mengenoperator(str, Enum):
    """
    Angabe, wie eine Menge in Bezug auf einen Wert zu bilden ist.
    """

    KLEINER_ALS = "KLEINER_ALS"
    GROESSER_ALS = "GROESSER_ALS"
    GLEICH = "GLEICH"
