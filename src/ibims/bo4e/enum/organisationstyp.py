from enum import Enum


class Organisationstyp(str, Enum):
    """
    Hier wird festgelegt, ob der GeschÃ¤ftspartner eine Person, eine Firma oder etwas anderes ist.
    """

    PRIVATPERSON = "PRIVATPERSON"
    UNTERNEHMEN = "UNTERNEHMEN"
    KOMMUNALE_EINRICHTUNG = "KOMMUNALE_EINRICHTUNG"
    STAATLICHE_BEHOERDE = "STAATLICHE_BEHOERDE"
