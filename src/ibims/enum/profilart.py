"""
Profilart ENUM
"""
from enum import StrEnum


class Profilart(StrEnum):
    """
    This enum specifies the forecast (Prognosegrundlage)
    """

    ART_STANDARDLASTPROFIL = "ART_STANDARDLASTPROFIL"
    """
    corresponds to Z02
    """
    ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL = "ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL"
    """
    corresponds to Z03
    """
    ART_LASTPROFIL = "ART_LASTPROFIL"
    """
    corresponds to Z12
    """
