import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.lokationstyp import Lokationstyp
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import EnergiemengeenergieverbrauchLink, EnergiemengezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.verbrauch import Verbrauch
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Energiemenge(SQLModel, table=True):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Energiemenge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Energiemenge.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    lokations_id: str | None = Field(default=None, alias="lokationsId", title="Lokationsid")
    """
    Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört
    """
    energiemenge_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.ENERGIEMENGE)
    energieverbrauch: List["Verbrauch"] = Relationship(
        back_populates="energiemenge_energieverbrauch_link",
        link_model=EnergiemengeenergieverbrauchLink,
    )
    lokationstyp: Lokationstyp | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="energiemenge_zusatzattribute_link",
        link_model=EnergiemengezusatzAttributeLink,
    )
