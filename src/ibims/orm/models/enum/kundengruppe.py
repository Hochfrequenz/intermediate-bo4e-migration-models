import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Kundengruppe(str, Enum):
    """
    Kundengruppe für eine Marktlokation (orientiert sich an den Standard-Lastprofilen).
    """

    RLM = "RLM"
    RLM_KOMMUNAL = "RLM_KOMMUNAL"
    SLP_KOMMUNAL = "SLP_KOMMUNAL"
    SLP_S_G0 = "SLP_S_G0"
    SLP_S_G1 = "SLP_S_G1"
    SLP_S_G2 = "SLP_S_G2"
    SLP_S_G3 = "SLP_S_G3"
    SLP_S_G4 = "SLP_S_G4"
    SLP_S_G5 = "SLP_S_G5"
    SLP_S_G6 = "SLP_S_G6"
    SLP_S_G7 = "SLP_S_G7"
    SLP_S_L0 = "SLP_S_L0"
    SLP_S_L1 = "SLP_S_L1"
    SLP_S_L2 = "SLP_S_L2"
    SLP_S_H0 = "SLP_S_H0"
    SLP_S_SB = "SLP_S_SB"
    SLP_S_HZ = "SLP_S_HZ"
    SLP_S_WP = "SLP_S_WP"
    SLP_S_EM = "SLP_S_EM"
    SLP_S_HZ_GEM = "SLP_S_HZ_GEM"
    SLP_G_GKO = "SLP_G_GKO"
    SLP_G_STANDARD = "SLP_G_STANDARD"
    SLP_G_GHA = "SLP_G_GHA"
    SLP_G_GMK = "SLP_G_GMK"
    SLP_G_GBD = "SLP_G_GBD"
    SLP_G_GGA = "SLP_G_GGA"
    SLP_G_GBH = "SLP_G_GBH"
    SLP_G_GBA = "SLP_G_GBA"
    SLP_G_GWA = "SLP_G_GWA"
    SLP_G_GGB = "SLP_G_GGB"
    SLP_G_GPD = "SLP_G_GPD"
    SLP_G_GMF = "SLP_G_GMF"
    SLP_G_HEF = "SLP_G_HEF"
    SLP_G_HMF = "SLP_G_HMF"
    SLP_G_HKO = "SLP_G_HKO"
