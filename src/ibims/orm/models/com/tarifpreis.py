import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.preisstatus import Preisstatus
from ibims.orm.models.enum.preistyp import Preistyp
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import TarifberechnungsparameterzusatzpreiseLink, TarifpreiszusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Tarifpreis(SQLModel, table=True):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Tarifpreis.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
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
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    """
    wert: float | None = Field(default=None, title="Wert")
    """
    Gibt die nominale Höhe des Preises an.
    """
    tarifpreis_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    tarifberechnungsparameter_zusatzpreise_link: List["Tarifberechnungsparameter"] = Relationship(
        back_populates="zusatzpreise",
        link_model=TarifberechnungsparameterzusatzpreiseLink,
    )
    bezugswert: Mengeneinheit | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    preistyp: Preistyp | None = Field(None)
    status: Preisstatus | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarifpreis_zusatzattribute_link",
        link_model=TarifpreiszusatzAttributeLink,
    )
