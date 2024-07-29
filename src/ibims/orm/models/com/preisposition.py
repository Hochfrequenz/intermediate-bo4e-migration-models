import uuid as uuid_pkg
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.bdew_artikelnummer import BDEWArtikelnummer
from ibims.orm.models.enum.bemessungsgroesse import Bemessungsgroesse
from ibims.orm.models.enum.kalkulationsmethode import Kalkulationsmethode
from ibims.orm.models.enum.leistungstyp import Leistungstyp
from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.steuerkennzeichen import Steuerkennzeichen
from ibims.orm.models.enum.tarifzeit import Tarifzeit
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import (
    PreisblattDienstleistungpreispositionenLink,
    PreisblattHardwarepreispositionenLink,
    PreisblattKonzessionsabgabepreispositionenLink,
    PreisblattMessungpreispositionenLink,
    PreisblattNetznutzungpreispositionenLink,
    PreisblattpreispositionenLink,
    PreispositionpreisstaffelnLink,
    PreispositionzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.preisblatt import Preisblatt
    from ibims.orm.models.bo.preisblatt_dienstleistung import PreisblattDienstleistung
    from ibims.orm.models.bo.preisblatt_hardware import PreisblattHardware
    from ibims.orm.models.bo.preisblatt_konzessionsabgabe import PreisblattKonzessionsabgabe
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.bo.preisblatt_netznutzung import PreisblattNetznutzung
    from ibims.orm.models.com.preisstaffel import Preisstaffel
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Preisposition(SQLModel, table=True):
    """
    Preis für eine definierte Lieferung oder Leistung innerhalb eines Preisblattes

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preisposition.json>`_
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
    freimenge_blindarbeit: float | None = Field(
        default=None, alias="freimengeBlindarbeit", title="Freimengeblindarbeit"
    )
    """
    Der Anteil der Menge der Blindarbeit in Prozent von der Wirkarbeit, für die keine Abrechnung erfolgt
    """
    freimenge_leistungsfaktor: float | None = Field(
        default=None, alias="freimengeLeistungsfaktor", title="Freimengeleistungsfaktor"
    )
    """
    gruppenartikel_id: Optional[str] = None
    """
    gruppenartikel_id: str | None = Field(default=None, alias="gruppenartikelId", title="Gruppenartikelid")
    """
    Übergeordnete Gruppen-ID, die sich ggf. auf die Artikel-ID in der Preisstaffel bezieht
    """
    leistungsbezeichnung: str | None = Field(default=None, title="Leistungsbezeichnung")
    """
    Bezeichnung für die in der Position abgebildete Leistungserbringung
    """
    preisposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    preisblatt_preispositionen_link: List["Preisblatt"] = Relationship(
        back_populates="preispositionen", link_model=PreisblattpreispositionenLink
    )
    preisblattdienstleistung_preispositionen_link: List["PreisblattDienstleistung"] = Relationship(
        back_populates="preispositionen",
        link_model=PreisblattDienstleistungpreispositionenLink,
    )
    preisblatthardware_preispositionen_link: List["PreisblattHardware"] = Relationship(
        back_populates="preispositionen",
        link_model=PreisblattHardwarepreispositionenLink,
    )
    preisblattkonzessionsabgabe_preispositionen_link: List["PreisblattKonzessionsabgabe"] = Relationship(
        back_populates="preispositionen",
        link_model=PreisblattKonzessionsabgabepreispositionenLink,
    )
    preisblattmessung_preispositionen_link: List["PreisblattMessung"] = Relationship(
        back_populates="preispositionen",
        link_model=PreisblattMessungpreispositionenLink,
    )
    preisblattnetznutzung_preispositionen_link: List["PreisblattNetznutzung"] = Relationship(
        back_populates="preispositionen",
        link_model=PreisblattNetznutzungpreispositionenLink,
    )
    bdewArtikelnummer: BDEWArtikelnummer | None = Field(None)
    berechnungsmethode: Kalkulationsmethode | None = Field(None)
    bezugsgroesse: Mengeneinheit | None = Field(None)
    leistungstyp: Leistungstyp | None = Field(None)
    preiseinheit: Waehrungseinheit | None = Field(None)
    preisstaffeln: List["Preisstaffel"] = Relationship(
        back_populates="preisposition_preisstaffeln_link",
        link_model=PreispositionpreisstaffelnLink,
    )
    tarifzeit: Tarifzeit | None = Field(None)
    zeitbasis: Mengeneinheit | None = Field(None)
    zonungsgroesse: Bemessungsgroesse | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisposition_zusatzattribute_link",
        link_model=PreispositionzusatzAttributeLink,
    )
    steuersatz: Steuerkennzeichen = Field(None)
