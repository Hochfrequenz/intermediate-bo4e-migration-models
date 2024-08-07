import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    AufAbschlagstaffelnLink,
    PreispositionpreisstaffelnLink,
    PreisstaffelzusatzAttributeLink,
    TarifpreispositionpreisstaffelnLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.com.auf_abschlag import AufAbschlag
    from ibims.orm.models.com.preisposition import Preisposition
    from ibims.orm.models.com.sigmoidparameter import Sigmoidparameter
    from ibims.orm.models.com.tarifpreisposition import Tarifpreisposition
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Preisstaffel(SQLModel, table=True):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preisstaffel.json>`_
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
    einheitspreis: float | None = Field(default=None, title="Einheitspreis")
    """
    Preis pro abgerechneter Mengeneinheit
    """
    staffelgrenze_bis: float | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    """
    Exklusiver oberer Wert, bis zu dem die Staffel gilt
    """
    staffelgrenze_von: float | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    """
    Inklusiver unterer Wert, ab dem die Staffel gilt
    """
    preisstaffel_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    aufabschlag_staffeln_link: List["AufAbschlag"] = Relationship(
        back_populates="staffeln", link_model=AufAbschlagstaffelnLink
    )
    preisposition_preisstaffeln_link: List["Preisposition"] = Relationship(
        back_populates="preisstaffeln", link_model=PreispositionpreisstaffelnLink
    )
    sigmoidparameter_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("sigmoidparameter.sigmoidparameter_sqlid", ondelete="SET NULL"),
        )
    )
    sigmoidparameter: "Sigmoidparameter" = Relationship(
        back_populates="preisstaffel_sigmoidparameter",
        sa_relationship_kwargs={"foreign_keys": "[Preisstaffel.sigmoidparameter_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisstaffel_zusatzattribute_link",
        link_model=PreisstaffelzusatzAttributeLink,
    )
    tarifpreisposition_preisstaffeln_link: List["Tarifpreisposition"] = Relationship(
        back_populates="preisstaffeln", link_model=TarifpreispositionpreisstaffelnLink
    )
