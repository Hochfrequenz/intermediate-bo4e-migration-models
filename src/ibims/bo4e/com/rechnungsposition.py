from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..enum.bdew_artikelnummer import BDEWArtikelnummer
from ..enum.mengeneinheit import Mengeneinheit
from ..zusatz_attribut import ZusatzAttribut
from .betrag import Betrag
from .menge import Menge
from .preis import Preis
from .steuerbetrag import Steuerbetrag


class Rechnungsposition(BaseModel):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Rechnungsposition.json>`_
    """

    model_config = ConfigDict(
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
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    artikel_id: str | None = Field(default=None, alias="artikelId", title="Artikelid")
    """
    Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst
    """
    artikelnummer: BDEWArtikelnummer | None = None
    """
    Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW
    """
    einzelpreis: Preis | None = None
    """
    Der Preis für eine Einheit der energetischen Menge
    """
    lieferung_bis: datetime | None = Field(default=None, alias="lieferungBis", title="Lieferungbis")
    """
    Ende der Lieferung für die abgerechnete Leistung (exklusiv)
    """
    lieferung_von: datetime | None = Field(default=None, alias="lieferungVon", title="Lieferungvon")
    """
    Start der Lieferung für die abgerechnete Leistung (inklusiv)
    """
    lokations_id: str | None = Field(default=None, alias="lokationsId", title="Lokationsid")
    """
    Marktlokation, die zu dieser Position gehört
    """
    positions_menge: Menge = Field(..., alias="positionsMenge")
    """
    Die abgerechnete Menge mit Einheit
    """
    positionsnummer: int | None = Field(default=None, title="Positionsnummer")
    """
    Fortlaufende Nummer für die Rechnungsposition
    """
    positionstext: str | None = Field(default=None, title="Positionstext")
    """
    Bezeichung für die abgerechnete Position
    """
    teilrabatt_netto: Betrag | None = Field(default=None, alias="teilrabattNetto")
    """
    Nettobetrag für den Rabatt dieser Position
    """
    teilsumme_netto: Betrag = Field(..., alias="teilsummeNetto")
    """
    # the cross check in general doesn't work because Betrag and Preis use different enums to describe the currency
    # see https://github.com/Hochfrequenz/BO4E-python/issues/126

    #: Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag
    teilsumme_steuer: Optional["Steuerbetrag"] = None

    #: Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit
    zeiteinheit: Optional["Mengeneinheit"] = None

    #: Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW
    artikelnummer: Optional["BDEWArtikelnummer"] = None
    #: Marktlokation, die zu dieser Position gehört
    lokations_id: Optional[str] = None

    zeitbezogene_menge: Optional["Menge"] = None
    """
    teilsumme_steuer: Steuerbetrag = Field(..., alias="teilsummeSteuer")
    """
    Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag
    """
    zeitbezogene_menge: Menge | None = Field(default=None, alias="zeitbezogeneMenge")
    """
    Nettobetrag für den Rabatt dieser Position
    """
    zeiteinheit: Mengeneinheit | None = None
    """
    Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
