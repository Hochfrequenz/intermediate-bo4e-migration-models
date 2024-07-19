from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..enum.angebotsstatus import Angebotsstatus
from ..zusatz_attribut import ZusatzAttribut
from .angebotsteil import Angebotsteil
from .betrag import Betrag
from .menge import Menge


class Angebotsvariante(BaseModel):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsvariante.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsvariante JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Angebotsvariante.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    angebotsstatus: Angebotsstatus | None = None
    """
    Gibt den Status eines Angebotes an.
    """
    bindefrist: datetime | None = Field(default=None, title="Bindefrist")
    """
    Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    """
    erstellungsdatum: datetime | None = Field(default=None, title="Erstellungsdatum")
    """
    Datum der Erstellung der Angebotsvariante
    """
    gesamtkosten: Betrag | None = None
    """
    Aufsummierte Kosten aller Angebotsteile
    """
    gesamtmenge: Menge | None = None
    """
    Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    """
    teile: list[Angebotsteil] | None = Field(default=None, title="Teile")
    """
    Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
