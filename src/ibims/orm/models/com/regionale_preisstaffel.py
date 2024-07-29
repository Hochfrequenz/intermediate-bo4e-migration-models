import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    RegionalePreisstaffelzusatzAttributeLink,
    RegionalerAufAbschlagstaffelnLink,
    RegionaleTarifpreispositionpreisstaffelnLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.com.regionale_gueltigkeit import RegionaleGueltigkeit
    from ibims.orm.models.com.regionale_tarifpreisposition import RegionaleTarifpreisposition
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.com.sigmoidparameter import Sigmoidparameter
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class RegionalePreisstaffel(SQLModel, table=True):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/RegionalePreisstaffel.json>`_
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
    regionalepreisstaffel_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaleGueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalegueltigkeit.regionalegueltigkeit_sqlid", ondelete="SET NULL"),
        )
    )
    regionaleGueltigkeit: "RegionaleGueltigkeit" = Relationship(
        back_populates="regionalepreisstaffel_regionaleGueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[RegionalePreisstaffel.regionaleGueltigkeit_id]"},
    )
    sigmoidparameter_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("sigmoidparameter.sigmoidparameter_sqlid", ondelete="SET NULL"),
        )
    )
    sigmoidparameter: "Sigmoidparameter" = Relationship(
        back_populates="regionalepreisstaffel_sigmoidparameter",
        sa_relationship_kwargs={"foreign_keys": "[RegionalePreisstaffel.sigmoidparameter_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="regionalepreisstaffel_zusatzattribute_link",
        link_model=RegionalePreisstaffelzusatzAttributeLink,
    )
    regionaleraufabschlag_staffeln_link: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="staffeln", link_model=RegionalerAufAbschlagstaffelnLink
    )
    regionaletarifpreisposition_preisstaffeln_link: List["RegionaleTarifpreisposition"] = Relationship(
        back_populates="preisstaffeln",
        link_model=RegionaleTarifpreispositionpreisstaffelnLink,
    )
