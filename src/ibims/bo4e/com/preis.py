from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preisstatus import Preisstatus
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut


class Preis(BaseModel):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preis.json>`_
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
    bezugswert: Mengeneinheit | None = None
    """
    Angabe, für welche Bezugsgröße der Preis gilt. Z.B. kWh.
    """
    einheit: Waehrungseinheit | None = None
    """
    Währungseinheit für den Preis, z.B. Euro oder Ct.
    """
    status: Preisstatus | None = None
    """
    Gibt den Status des veröffentlichten Preises an
    """
    wert: float | None = Field(default=None, title="Wert")
    """
    Gibt die nominale Höhe des Preises an.
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
