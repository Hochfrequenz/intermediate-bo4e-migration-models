from enum import Enum


class Titel(str, Enum):
    """
    Ãœbersicht mÃ¶glicher Titel, z.B. eines GeschÃ¤ftspartners.
    """

    DR = "DR"
    PROF = "PROF"
    PROF_DR = "PROF_DR"
