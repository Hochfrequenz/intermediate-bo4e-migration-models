import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import BuendelvertragvertragskonditionenLink, VertragskonditionenzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.buendelvertrag import Buendelvertrag
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifinfo import Tarifinfo
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Vertragskonditionen(SQLModel, table=True):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragskonditionen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Vertragskonditionen.json>`_
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
    anzahl_abschlaege: float | None = Field(default=None, alias="anzahlAbschlaege", title="Anzahlabschlaege")
    """
    Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12
    """
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    """
    vertragskonditionen_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    buendelvertrag_vertragskonditionen_link: List["Buendelvertrag"] = Relationship(
        back_populates="vertragskonditionen",
        link_model=BuendelvertragvertragskonditionenLink,
    )
    regionaltarif_vertragskonditionen: List["Regionaltarif"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    tarif_vertragskonditionen: List["Tarif"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    tarifinfo_vertragskonditionen: List["Tarifinfo"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifinfo.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    tarifkosten_vertragskonditionen: List["Tarifkosten"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifkosten.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_vertragskonditionen: List["Tarifpreisblatt"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    vertrag_vertragskonditionen: List["Vertrag"] = Relationship(
        back_populates="vertragskonditionen",
        sa_relationship_kwargs={
            "primaryjoin": "Vertrag.vertragskonditionen_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlagregional_vertagskonditionsaenderung: List["AufAbschlagRegional"] = Relationship(
        back_populates="vertagskonditionsaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlagRegional.vertagskonditionsaenderung_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    regionaleraufabschlag_vertagskonditionsaenderung: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="vertagskonditionsaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalerAufAbschlag.vertagskonditionsaenderung_id==Vertragskonditionen.vertragskonditionen_sqlid",
            "lazy": "joined",
        },
    )
    abschlagszyklus_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    abschlagszyklus: "Zeitraum" = Relationship(
        back_populates="vertragskonditionen_abschlagszyklus",
        sa_relationship_kwargs={"foreign_keys": "[Vertragskonditionen.abschlagszyklus_id]"},
    )
    kuendigungsfrist_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    kuendigungsfrist: "Zeitraum" = Relationship(
        back_populates="vertragskonditionen_kuendigungsfrist",
        sa_relationship_kwargs={"foreign_keys": "[Vertragskonditionen.kuendigungsfrist_id]"},
    )
    vertragslaufzeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    vertragslaufzeit: "Zeitraum" = Relationship(
        back_populates="vertragskonditionen_vertragslaufzeit",
        sa_relationship_kwargs={"foreign_keys": "[Vertragskonditionen.vertragslaufzeit_id]"},
    )
    vertragsverlaengerung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    vertragsverlaengerung: "Zeitraum" = Relationship(
        back_populates="vertragskonditionen_vertragsverlaengerung",
        sa_relationship_kwargs={"foreign_keys": "[Vertragskonditionen.vertragsverlaengerung_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="vertragskonditionen_zusatzattribute_link",
        link_model=VertragskonditionenzusatzAttributeLink,
    )
