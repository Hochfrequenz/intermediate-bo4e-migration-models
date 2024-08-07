import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Organisationstyp(str, Enum):
    """
    Hier wird festgelegt, ob der Geschäftspartner eine Person, eine Firma oder etwas anderes ist.
    """

    PRIVATPERSON = "PRIVATPERSON"
    UNTERNEHMEN = "UNTERNEHMEN"
    KOMMUNALE_EINRICHTUNG = "KOMMUNALE_EINRICHTUNG"
    STAATLICHE_BEHOERDE = "STAATLICHE_BEHOERDE"
