from enum import Enum


class Waehrungseinheit(str, Enum):
    """
    In diesem Enum werden die WÃ¤hrungen und ihre Untereinheiten definiert, beispielsweise fÃ¼r die Verwendung in Preisen.
    """

    EUR = "EUR"
    CT = "CT"
