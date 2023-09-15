"""
Contains the dataset for the agent hint loader.
"""

from bo4e.bo.vertrag import Vertrag

from ibims.bo import GeschaeftspartnerErweitert
from lqtmapping.models.bo4e.custom.bo.hinweis import Hinweis
from lqtmapping.models.bo4e.datasets.base import DataSetBaseModel


class ED4AgentHintLoaderDataSet(DataSetBaseModel):
    """
    This is a bo4e data set that consists of
    * a GeschaeftspartnerErweitert
    * a Vertrag
    * a hint
    In the context of this package is may be used to create ED$ AgentHint Data.
    """

    geschaeftspartner_erw: GeschaeftspartnerErweitert
    """
    The following attribute needs to be filled for this DataSet:
    - externe_referenzen
        - customerID
    """

    vertrag: Vertrag
    """
    Each Vertrag needs the following Attribute:
    - vertragsnummer
    """

    hinweis: Hinweis
    """
    A hint to specialties in the contract
    """
