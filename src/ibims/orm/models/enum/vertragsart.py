import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Vertragsart(str, Enum):
    """
    Aufzählung der Vertragsarten.
    """

    ENERGIELIEFERVERTRAG = "ENERGIELIEFERVERTRAG"
    NETZNUTZUNGSVERTRAG = "NETZNUTZUNGSVERTRAG"
    BILANZIERUNGSVERTRAG = "BILANZIERUNGSVERTRAG"
    MESSSTELLENBETRIEBSVERTRAG = "MESSSTELLENBETRIEBSVERTRAG"
    BUENDELVERTRAG = "BUENDELVERTRAG"
