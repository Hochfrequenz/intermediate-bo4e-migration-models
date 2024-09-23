import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import StandorteigenschafteneigenschaftenStromLink, StandorteigenschaftenzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.standorteigenschaften_gas import StandorteigenschaftenGas
    from ibims.orm.models.com.standorteigenschaften_strom import StandorteigenschaftenStrom
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Standorteigenschaften(SQLModel, table=True):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Standorteigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Standorteigenschaften.json>`_
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
    standorteigenschaften_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.STANDORTEIGENSCHAFTEN)
    eigenschaftenGas_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "standorteigenschaftengas.standorteigenschaftengas_sqlid",
                ondelete="SET NULL",
            ),
        )
    )
    eigenschaftenGas: "StandorteigenschaftenGas" = Relationship(
        back_populates="standorteigenschaften_eigenschaftenGas",
        sa_relationship_kwargs={"foreign_keys": "[Standorteigenschaften.eigenschaftenGas_id]"},
    )
    eigenschaftenStrom: List["StandorteigenschaftenStrom"] = Relationship(
        back_populates="standorteigenschaften_eigenschaftenstrom_link",
        link_model=StandorteigenschafteneigenschaftenStromLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="standorteigenschaften_zusatzattribute_link",
        link_model=StandorteigenschaftenzusatzAttributeLink,
    )
