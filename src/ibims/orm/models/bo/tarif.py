import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kundentyp import Kundentyp
from ibims.orm.models.enum.registeranzahl import Registeranzahl
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.tarifmerkmal import Tarifmerkmal
from ibims.orm.models.enum.tariftyp import Tariftyp
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import TariftarifAufAbschlaegeLink, TariftarifpreiseLink, TarifzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.energiemix import Energiemix
    from ibims.orm.models.com.preisgarantie import Preisgarantie
    from ibims.orm.models.com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ibims.orm.models.com.tarifeinschraenkung import Tarifeinschraenkung
    from ibims.orm.models.com.tarifpreisposition_pro_ort import TarifpreispositionProOrt
    from ibims.orm.models.com.vertragskonditionen import Vertragskonditionen
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Tarif(SQLModel, table=True):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Tarif.json>`_
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
    anbietername: str | None = Field(default=None, title="Anbietername")
    """
    Der Name des Marktpartners, der den Tarif anbietet
    """
    anwendung_von: datetime | None = Field(default=None, alias="anwendungVon", title="Anwendungvon")
    """
    Angabe des inklusiven Zeitpunkts, ab dem der Tarif bzw. der Preis angewendet und abgerechnet wird,
    z.B. "2021-07-20T18:31:48Z"
    """
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    """
    Freitext
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Name des Tarifs
    """
    preisstand: datetime | None = Field(default=None, title="Preisstand")
    """
    Gibt an, wann der Preis zuletzt angepasst wurde
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite auf dem der Tarif zu finden ist
    """
    tarif_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.TARIF)
    anbieter_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktteilnehmer.marktteilnehmer_sqlid", ondelete="SET NULL"),
        )
    )
    anbieter: "Marktteilnehmer" = Relationship(
        back_populates="tarif_anbieter",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.anbieter_id]"},
    )
    berechnungsparameter_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "tarifberechnungsparameter.tarifberechnungsparameter_sqlid",
                ondelete="SET NULL",
            ),
        )
    )
    berechnungsparameter: "Tarifberechnungsparameter" = Relationship(
        back_populates="tarif_berechnungsparameter",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.berechnungsparameter_id]"},
    )
    energiemix_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("energiemix.energiemix_sqlid", ondelete="SET NULL"),
        )
    )
    energiemix: "Energiemix" = Relationship(
        back_populates="tarif_energiemix",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.energiemix_id]"},
    )
    kundentypen: List[Kundentyp] | None = Field(None, sa_column=Column(ARRAY(Enum(Kundentyp, name="kundentyp"))))
    preisgarantie_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("preisgarantie.preisgarantie_sqlid", ondelete="SET NULL"),
        )
    )
    preisgarantie: "Preisgarantie" = Relationship(
        back_populates="tarif_preisgarantie",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.preisgarantie_id]"},
    )
    registeranzahl: Registeranzahl | None = Field(None)
    sparte: Sparte | None = Field(None)
    tarifAufAbschlaege: List["AufAbschlagRegional"] = Relationship(
        back_populates="tarif_tarifaufabschlaege_link",
        link_model=TariftarifAufAbschlaegeLink,
    )
    tarifeinschraenkung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("tarifeinschraenkung.tarifeinschraenkung_sqlid", ondelete="SET NULL"),
        )
    )
    tarifeinschraenkung: "Tarifeinschraenkung" = Relationship(
        back_populates="tarif_tarifeinschraenkung",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.tarifeinschraenkung_id]"},
    )
    tarifmerkmale: List[Tarifmerkmal] | None = Field(
        None, sa_column=Column(ARRAY(Enum(Tarifmerkmal, name="tarifmerkmal")))
    )
    tarifpreise: List["TarifpreispositionProOrt"] = Relationship(
        back_populates="tarif_tarifpreise_link", link_model=TariftarifpreiseLink
    )
    tariftyp: Tariftyp | None = Field(None)
    vertragskonditionen_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragskonditionen.vertragskonditionen_sqlid", ondelete="SET NULL"),
        )
    )
    vertragskonditionen: "Vertragskonditionen" = Relationship(
        back_populates="tarif_vertragskonditionen",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.vertragskonditionen_id]"},
    )
    zeitlicheGueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    zeitlicheGueltigkeit: "Zeitraum" = Relationship(
        back_populates="tarif_zeitlicheGueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[Tarif.zeitlicheGueltigkeit_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarif_zusatzattribute_link", link_model=TarifzusatzAttributeLink
    )
