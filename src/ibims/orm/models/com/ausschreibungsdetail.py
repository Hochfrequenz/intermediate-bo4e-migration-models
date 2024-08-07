import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.zaehlertyp import Zaehlertyp
from ibims.orm.models.many import AusschreibungsdetailzusatzAttributeLink, AusschreibungsloslieferstellenLink

if TYPE_CHECKING:
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.ausschreibungslos import Ausschreibungslos
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Ausschreibungsdetail(SQLModel, table=True):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungsdetail.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Ausschreibungsdetail.json>`_
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
    ist_lastgang_vorhanden: bool | None = Field(
        default=None, alias="istLastgangVorhanden", title="Istlastgangvorhanden"
    )
    """
    Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    """
    kunde: str | None = Field(default=None, title="Kunde")
    """
    Bezeichnung des Kunden, der die Marktlokation nutzt
    """
    marktlokations_id: str | None = Field(default=None, alias="marktlokationsId", title="Marktlokationsid")
    """
    Identifikation einer ausgeschriebenen Marktlokation
    """
    marktlokationsbezeichnung: str | None = Field(default=None, title="Marktlokationsbezeichnung")
    """
    Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    """
    netzbetreiber: str | None = Field(default=None, title="Netzbetreiber")
    """
    Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    """
    netzebene_lieferung: str | None = Field(default=None, alias="netzebeneLieferung", title="Netzebenelieferung")
    """
    In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    """
    netzebene_messung: str | None = Field(default=None, alias="netzebeneMessung", title="Netzebenemessung")
    """
    In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    """
    zaehlernummer: str | None = Field(default=None, title="Zaehlernummer")
    """
    Die Bezeichnung des Zählers an der Marktlokation
    """
    ausschreibungsdetail_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    lieferzeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    lieferzeitraum: "Zeitraum" = Relationship(
        back_populates="ausschreibungsdetail_lieferzeitraum",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.lieferzeitraum_id]"},
    )
    marktlokationsadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    marktlokationsadresse: "Adresse" = Relationship(
        back_populates="ausschreibungsdetail_marktlokationsadresse",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.marktlokationsadresse_id]"},
    )
    prognoseArbeitLieferzeitraum_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    prognoseArbeitLieferzeitraum: "Menge" = Relationship(
        back_populates="ausschreibungsdetail_prognoseArbeitLieferzeitraum",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.prognoseArbeitLieferzeitraum_id]"},
    )
    prognoseJahresarbeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    prognoseJahresarbeit: "Menge" = Relationship(
        back_populates="ausschreibungsdetail_prognoseJahresarbeit",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.prognoseJahresarbeit_id]"},
    )
    prognoseLeistung_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    prognoseLeistung: "Menge" = Relationship(
        back_populates="ausschreibungsdetail_prognoseLeistung",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.prognoseLeistung_id]"},
    )
    rechnungsadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    rechnungsadresse: "Adresse" = Relationship(
        back_populates="ausschreibungsdetail_rechnungsadresse",
        sa_relationship_kwargs={"foreign_keys": "[Ausschreibungsdetail.rechnungsadresse_id]"},
    )
    zaehlertechnik: Zaehlertyp | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="ausschreibungsdetail_zusatzattribute_link",
        link_model=AusschreibungsdetailzusatzAttributeLink,
    )
    ausschreibungslos_lieferstellen_link: List["Ausschreibungslos"] = Relationship(
        back_populates="lieferstellen", link_model=AusschreibungsloslieferstellenLink
    )
