from enum import Enum


class Anrede(str, Enum):
    """
    Ãœbersicht mÃ¶glicher Anreden, z.B. eines GeschÃ¤ftspartners.
    """

    HERR = "HERR"
    FRAU = "FRAU"
    EHELEUTE = "EHELEUTE"
    FIRMA = "FIRMA"
    FAMILIE = "FAMILIE"
    ERBENGEMEINSCHAFT = "ERBENGEMEINSCHAFT"
    GRUNDSTUECKSGEMEINSCHAFT = "GRUNDSTUECKSGEMEINSCHAFT"
