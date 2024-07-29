import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Variant(str, Enum):
    """
    gridUsageBilling.variant (Netznutzungsabrechnungsvariante)
        Z14: WorkPriceBasicPrice (Arbeitspreis/Grundpreis)
        Z15: WorkPricePerformancePrice (Arbeitspreis/Leistungspreis)
    """

    Z14 = "Z14"
    Z15 = "Z15"
