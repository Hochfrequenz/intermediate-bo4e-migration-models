import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Zaehlergroesse(str, Enum):
    """
    Auflistung möglicher Größen von Zählern
    """

    G2_KOMMA5 = "G2KOMMA5"
    G4 = "G4"
    G6 = "G6"
    G10 = "G10"
    G16 = "G16"
    G25 = "G25"
    G40 = "G40"
    G65 = "G65"
    G100 = "G100"
    G160 = "G160"
    G250 = "G250"
    G400 = "G400"
    G650 = "G650"
    G1000 = "G1000"
    G1600 = "G1600"
    G2500 = "G2500"
    G4000 = "G4000"
    G6500 = "G6500"
    G10000 = "G10000"
    G12500 = "G12500"
    G16000 = "G16000"
