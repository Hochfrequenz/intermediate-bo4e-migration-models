"""
Prognosegrundlagedetail enum
"""
from enum import StrEnum


class PrognosegrundlageDetail(StrEnum):
    """
    This enum specifies the forecast (Prognosegrundlage)
    """

    STANDARD = "STANDARD"
    """
    corresponds to SLP/SEP (Standardlastprofil/Standardeinspeiseprofile)
    """
    TAGESPARAMETERABHAENGIG = "TAGESPARAMETERABHAENGIG"
    """
    corresponds to TLP/TEP (Tagesparameterabhängige Lastprofile)
    """
