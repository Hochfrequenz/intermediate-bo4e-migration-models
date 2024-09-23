import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Gebiettyp(str, Enum):
    """
    List of possible Gebiettypen.
    """

    REGELZONE = "REGELZONE"
    MARKTGEBIET = "MARKTGEBIET"
    BILANZIERUNGSGEBIET = "BILANZIERUNGSGEBIET"
    VERTEILNETZ = "VERTEILNETZ"
    TRANSPORTNETZ = "TRANSPORTNETZ"
    REGIONALNETZ = "REGIONALNETZ"
    AREALNETZ = "AREALNETZ"
    GRUNDVERSORGUNGSGEBIET = "GRUNDVERSORGUNGSGEBIET"
    VERSORGUNGSGEBIET = "VERSORGUNGSGEBIET"
