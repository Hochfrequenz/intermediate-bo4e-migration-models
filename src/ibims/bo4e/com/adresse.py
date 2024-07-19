from pydantic import BaseModel, ConfigDict, Field

from ..enum.landescode import Landescode
from ..zusatz_attribut import ZusatzAttribut


class Adresse(BaseModel):
    """
    Contains an address that can be used for most purposes.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Adresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Adresse.json>`_
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
    adresszusatz: str | None = Field(default=None, title="Adresszusatz")
    """
    Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    """
    co_ergaenzung: str | None = Field(default=None, alias="coErgaenzung", title="Coergaenzung")
    """
    Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    """
    hausnummer: str | None = Field(default=None, title="Hausnummer")
    """
    Hausnummer inkl. Zusatz; z.B. "3", "4a"
    """
    landescode: Landescode | None = Landescode.DE
    """
    Offizieller ISO-Landescode
    """
    ort: str = Field(..., title="Ort")
    """
    Bezeichnung der Stadt; z.B. "Hückelhoven"
    """
    ortsteil: str | None = Field(default=None, title="Ortsteil")
    """
    Bezeichnung des Ortsteils; z.B. "Mitte"
    """
    postfach: str | None = Field(default=None, title="Postfach")
    """
    Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    """
    postleitzahl: str = Field(..., title="Postleitzahl")
    """
    Die Postleitzahl; z.B: "41836"
    """
    strasse: str | None = Field(default=None, title="Strasse")
    """
    Bezeichnung der Straße; z.B. "Weserstraße"
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
