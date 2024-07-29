import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Netzebene(str, Enum):
    """
    Auflistung möglicher Netzebenen innerhalb der Energiearten Strom und Gas.
    """

    NSP = "NSP"
    MSP = "MSP"
    HSP = "HSP"
    HSS = "HSS"
    MSP_NSP_UMSP = "MSP_NSP_UMSP"
    HSP_MSP_UMSP = "HSP_MSP_UMSP"
    HSS_HSP_UMSP = "HSS_HSP_UMSP"
    HD = "HD"
    MD = "MD"
    ND = "ND"
