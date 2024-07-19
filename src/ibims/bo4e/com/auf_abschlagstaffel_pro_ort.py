from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut


class AufAbschlagstaffelProOrt(BaseModel):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/AufAbschlagstaffelProOrt.json>`_
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
    staffelgrenze_bis: float | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    """
    Oberer Wert, bis zu dem die Staffel gilt.
    """
    staffelgrenze_von: float | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    """
    Unterer Wert, ab dem die Staffel gilt.
    """
    wert: float | None = Field(default=None, title="Wert")
    """
    Der Wert für den Auf- oder Abschlag.
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
