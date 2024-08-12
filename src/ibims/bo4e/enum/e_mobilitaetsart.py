from enum import Enum


class EMobilitaetsart(str, Enum):
    """
    Art der E-MobilitÃ¤t
    """

    WALLBOX = "WALLBOX"
    E_MOBILITAETSLADESAEULE = "E_MOBILITAETSLADESAEULE"
    LADEPARK = "LADEPARK"
