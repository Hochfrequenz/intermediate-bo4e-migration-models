from pydantic import BaseModel, ConfigDict, Field

from ..bo.marktlokation import Marktlokation
from ..zusatz_attribut import ZusatzAttribut
from .angebotsposition import Angebotsposition
from .betrag import Betrag
from .menge import Menge
from .zeitraum import Zeitraum


class Angebotsteil(BaseModel):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Angebotsteil.json>`_
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
    anfrage_subreferenz: str | None = Field(default=None, alias="anfrageSubreferenz", title="Anfragesubreferenz")
    """
    Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    """
    gesamtkostenangebotsteil: Betrag | None = None
    """
    Summe der Jahresenergiekosten aller in diesem Angebotsteil enthaltenen Lieferstellen
    """
    gesamtmengeangebotsteil: Menge | None = None
    """
    Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    """
    lieferstellenangebotsteil: list[Marktlokation] | None = Field(default=None, title="Lieferstellenangebotsteil")
    """
    Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    """
    lieferzeitraum: Zeitraum | None = None
    """
    Hier kann der Belieferungszeitraum angegeben werden, für den dieser Angebotsteil gilt
    """
    positionen: list[Angebotsposition] | None = Field(default=None, title="Positionen")
    """
    Einzelne Positionen, die zu diesem Angebotsteil gehören
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
