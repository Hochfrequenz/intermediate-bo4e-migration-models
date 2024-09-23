"""
Contains the dataset for the resource loader.
It also contains the validation logic for the resource loader dataset.
"""

from ibims.orm.datasets import DataSetBaseModel
from ibims.orm.models import Marktlokation, Messlokation, Vertrag, Zaehler


class TripicaResourceLoaderDataSet(DataSetBaseModel):
    """
    This is a bo4e data set that consists of
    * a Vertrag
    * a Marktlokation
    * a Messlokation
    * a Zaehler.
    In the context of this package is may be used to create Tripica Resources.
    """

    marktlokation: Marktlokation
    messlokation: Messlokation
    vertrag: Vertrag
    zaehler: Zaehler
