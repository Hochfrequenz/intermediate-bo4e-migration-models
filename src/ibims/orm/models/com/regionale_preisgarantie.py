import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.preisgarantietyp import Preisgarantietyp
from ibims.orm.models.many import RegionalePreisgarantiezusatzAttributeLink, RegionaltarifpreisgarantienLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.com.regionale_gueltigkeit import RegionaleGueltigkeit
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class RegionalePreisgarantie(SQLModel, table=True):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/RegionalePreisgarantie.json>`_
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
    Freitext zur Beschreibung der Preisgarantie.
    """
    regionalepreisgarantie_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_preisgarantien_link: List["Regionaltarif"] = Relationship(
        back_populates="preisgarantien", link_model=RegionaltarifpreisgarantienLink
    )
    preisgarantietyp: Preisgarantietyp | None = Field(None)
    regionaleGueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("regionalegueltigkeit.regionalegueltigkeit_sqlid", ondelete="SET NULL"),
        )
    )
    regionaleGueltigkeit: "RegionaleGueltigkeit" = Relationship(
        back_populates="regionalepreisgarantie_regionaleGueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[RegionalePreisgarantie.regionaleGueltigkeit_id]"},
    )
    zeitlicheGueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    zeitlicheGueltigkeit: "Zeitraum" = Relationship(
        back_populates="regionalepreisgarantie_zeitlicheGueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[RegionalePreisgarantie.zeitlicheGueltigkeit_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="regionalepreisgarantie_zusatzattribute_link",
        link_model=RegionalePreisgarantiezusatzAttributeLink,
    )
