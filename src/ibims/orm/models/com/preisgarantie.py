import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.preisgarantietyp import Preisgarantietyp
from ibims.orm.models.many import PreisgarantiezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Preisgarantie(SQLModel, table=True):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preisgarantie.json>`_
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
    creation_date: datetime | None = Field(default=None, alias="creationDate", title="Creationdate")
    preisgarantie_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    tarif_preisgarantie: List["Tarif"] = Relationship(
        back_populates="preisgarantie",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.preisgarantie_id==Preisgarantie.preisgarantie_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_preisgarantie: List["Tarifpreisblatt"] = Relationship(
        back_populates="preisgarantie",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.preisgarantie_id==Preisgarantie.preisgarantie_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlagregional_garantieaenderung: List["AufAbschlagRegional"] = Relationship(
        back_populates="garantieaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlagRegional.garantieaenderung_id==Preisgarantie.preisgarantie_sqlid",
            "lazy": "joined",
        },
    )
    preisgarantietyp: Preisgarantietyp | None = Field(None)
    zeitlicheGueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    zeitlicheGueltigkeit: "Zeitraum" = Relationship(
        back_populates="preisgarantie_zeitlicheGueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[Preisgarantie.zeitlicheGueltigkeit_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisgarantie_zusatzattribute_link",
        link_model=PreisgarantiezusatzAttributeLink,
    )
    regionaleraufabschlag_garantieaenderung: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="garantieaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalerAufAbschlag.garantieaenderung_id==Preisgarantie.preisgarantie_sqlid",
            "lazy": "joined",
        },
    )
