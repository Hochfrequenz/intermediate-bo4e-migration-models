from pydantic import BaseModel, ConfigDict, Field

from ..enum.kontaktart import Kontaktart
from ..zusatz_attribut import ZusatzAttribut


class Kontaktweg(BaseModel):
    """
    Die Komponente wird dazu verwendet, die Kontaktwege innerhalb des BOs Person darzustellen

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kontakt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kontakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Kontakt.json>`_
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
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Spezifikation, beispielsweise "Durchwahl", "Sammelnummer" etc.
    """
    ist_bevorzugter_kontaktweg: bool | None = Field(
        default=None, alias="istBevorzugterKontaktweg", title="Istbevorzugterkontaktweg"
    )
    """
    Gibt an, ob es sich um den bevorzugten Kontaktweg handelt.
    """
    kontaktart: Kontaktart | None = None
    """
    Gibt die Kontaktart des Kontaktes an.
    """
    kontaktwert: str | None = Field(default=None, title="Kontaktwert")
    """
    Die Nummer oder E-Mail-Adresse.
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
