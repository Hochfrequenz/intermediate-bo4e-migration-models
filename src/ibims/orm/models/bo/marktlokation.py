import uuid as uuid_pkg
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.bilanzierungsmethode import Bilanzierungsmethode
from ibims.orm.models.enum.energierichtung import Energierichtung
from ibims.orm.models.enum.gasqualitaet import Gasqualitaet
from ibims.orm.models.enum.gebiettyp import Gebiettyp
from ibims.orm.models.enum.kundentyp import Kundentyp
from ibims.orm.models.enum.marktgebiet import Marktgebiet
from ibims.orm.models.enum.messtechnische_einordnung import MesstechnischeEinordnung
from ibims.orm.models.enum.netzebene import Netzebene
from ibims.orm.models.enum.profiltyp import Profiltyp
from ibims.orm.models.enum.prognosegrundlage import Prognosegrundlage
from ibims.orm.models.enum.regelzone import Regelzone
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.enum.variant import Variant
from ibims.orm.models.enum.verbrauchsart import Verbrauchsart
from ibims.orm.models.many import (
    AngebotsteillieferstellenangebotsteilLink,
    MarktlokationverbrauchsmengenLink,
    MarktlokationzaehlwerkeDerBeteiligtenMarktrolleLink,
    MarktlokationzaehlwerkeLink,
    MarktlokationzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.lastgang import Lastgang
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.angebotsteil import Angebotsteil
    from ibims.orm.models.com.geokoordinaten import Geokoordinaten
    from ibims.orm.models.com.katasteradresse import Katasteradresse
    from ibims.orm.models.com.messlokationszuordnung import Messlokationszuordnung
    from ibims.orm.models.com.verbrauch import Verbrauch
    from ibims.orm.models.com.zaehlwerk import Zaehlwerk
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Marktlokation(SQLModel, table=True):
    """
    Object containing information about a Marktlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Marktlokation.json>`_
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
    bilanzierungsgebiet: str | None = Field(default=None, title="Bilanzierungsgebiet")
    """
    Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes
    """
    grundversorgercodenr: str | None = Field(default=None, title="Grundversorgercodenr")
    """
    Codenummer des Grundversorgers, der für diese Marktlokation zuständig ist
    """
    ist_unterbrechbar: bool | None = Field(default=None, alias="istUnterbrechbar", title="Istunterbrechbar")
    """
    Gibt an, ob es sich um eine unterbrechbare Belieferung handelt
    """
    marktlokations_id: str | None = Field(default=None, alias="marktlokationsId", title="Marktlokationsid")
    """
    Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    """
    netzbetreibercodenr: str | None = Field(default=None, title="Netzbetreibercodenr")
    """
    Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation angeschlossen ist.
    """
    netzgebietsnr: str | None = Field(default=None, title="Netzgebietsnr")
    """
    Die ID des Gebietes in der ene't-Datenbank
    """
    regelzone: str | None = Field(default=None, title="Regelzone")
    """
    Kundengruppen der Marktlokation
    """
    community_id: str = Field(..., alias="communityId", title="Communityid")
    marktlokation_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    lastgang_marktlokation: List["Lastgang"] = Relationship(
        back_populates="marktlokation",
        sa_relationship_kwargs={
            "primaryjoin": "Lastgang.marktlokation_id==Marktlokation.marktlokation_sqlid",
            "lazy": "joined",
        },
    )
    typ: Typ | None = Field(Typ.MARKTLOKATION)
    bilanzierungsmethode: Bilanzierungsmethode | None = Field(None)
    endkunde_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    endkunde: "Geschaeftspartner" = Relationship(
        back_populates="marktlokation_endkunde",
        sa_relationship_kwargs={"foreign_keys": "[Marktlokation.endkunde_id]"},
    )
    energierichtung: Energierichtung | None = Field(None)
    gasqualitaet: Gasqualitaet | None = Field(None)
    gebietstyp: Gebiettyp | None = Field(None)
    geoadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geokoordinaten.geokoordinaten_sqlid", ondelete="SET NULL"),
        )
    )
    geoadresse: "Geokoordinaten" = Relationship(
        back_populates="marktlokation_geoadresse",
        sa_relationship_kwargs={"foreign_keys": "[Marktlokation.geoadresse_id]"},
    )
    katasterinformation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("katasteradresse.katasteradresse_sqlid", ondelete="SET NULL"),
        )
    )
    katasterinformation: "Katasteradresse" = Relationship(
        back_populates="marktlokation_katasterinformation",
        sa_relationship_kwargs={"foreign_keys": "[Marktlokation.katasterinformation_id]"},
    )
    kundengruppen: List[Kundentyp] | None = Field(None, sa_column=Column(ARRAY(Enum(Kundentyp, name="kundentyp"))))
    lokationsadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    lokationsadresse: "Adresse" = Relationship(
        back_populates="marktlokation_lokationsadresse",
        sa_relationship_kwargs={"foreign_keys": "[Marktlokation.lokationsadresse_id]"},
    )
    marktgebiet: Marktgebiet | None = Field(None)
    netzebene: Netzebene | None = Field(None)
    sparte: Sparte | None = Field(None)
    verbrauchsart: Verbrauchsart | None = Field(None)
    verbrauchsmengen: List["Verbrauch"] = Relationship(
        back_populates="marktlokation_verbrauchsmengen_link",
        link_model=MarktlokationverbrauchsmengenLink,
    )
    zaehlwerke: List["Zaehlwerk"] = Relationship(
        back_populates="marktlokation_zaehlwerke_link",
        link_model=MarktlokationzaehlwerkeLink,
    )
    zaehlwerkeDerBeteiligtenMarktrolle: List["Zaehlwerk"] = Relationship(
        back_populates="marktlokation_zaehlwerkederbeteiligtenmarktrolle_link",
        link_model=MarktlokationzaehlwerkeDerBeteiligtenMarktrolleLink,
    )
    zugehoerigeMesslokation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey(
                "messlokationszuordnung.messlokationszuordnung_sqlid",
                ondelete="SET NULL",
            ),
        )
    )
    zugehoerigeMesslokation: "Messlokationszuordnung" = Relationship(
        back_populates="marktlokation_zugehoerigeMesslokation",
        sa_relationship_kwargs={"foreign_keys": "[Marktlokation.zugehoerigeMesslokation_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="marktlokation_zusatzattribute_link",
        link_model=MarktlokationzusatzAttributeLink,
    )
    messtechnischeEinordnung: MesstechnischeEinordnung = Field(None)
    uebertragungsnetzgebiet: Regelzone | None = Field(None)
    variant: Variant = Field(None)
    prognoseGrundlage: Prognosegrundlage | None = Field(None)
    prognoseGrundlageDetail: Profiltyp | None = Field(None)
    rechnung_marktlokation: List["Rechnung"] = Relationship(
        back_populates="marktlokation",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.marktlokation_id==Marktlokation.marktlokation_sqlid",
            "lazy": "joined",
        },
    )
    angebotsteil_lieferstellenangebotsteil_link: List["Angebotsteil"] = Relationship(
        back_populates="lieferstellenangebotsteil",
        link_model=AngebotsteillieferstellenangebotsteilLink,
    )
