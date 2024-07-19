from pydantic import BaseModel, ConfigDict, Field

from ..enum.bdew_artikelnummer import BDEWArtikelnummer
from ..enum.bemessungsgroesse import Bemessungsgroesse
from ..enum.kalkulationsmethode import Kalkulationsmethode
from ..enum.leistungstyp import Leistungstyp
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.steuerkennzeichen import Steuerkennzeichen
from ..enum.tarifzeit import Tarifzeit
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut
from .preisstaffel import Preisstaffel


class Preisposition(BaseModel):
    """
    Preis für eine definierte Lieferung oder Leistung innerhalb eines Preisblattes

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Preisposition.json>`_
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
    bdew_artikelnummer: BDEWArtikelnummer | None = Field(default=None, alias="bdewArtikelnummer")
    """
    Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden
    """
    berechnungsmethode: Kalkulationsmethode | None = None
    """
    Das Modell, das der Preisbildung zugrunde liegt
    """
    bezugsgroesse: Mengeneinheit | None = None
    """
    Hier wird festgelegt, auf welche Bezugsgrösse sich der Preis bezieht, z.B. kWh oder Stück
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
    leistungstyp: Leistungstyp | None = None
    """
    Standardisierte Bezeichnung für die abgerechnete Leistungserbringung
    """
    preiseinheit: Waehrungseinheit | None = None
    """
    Festlegung, mit welcher Preiseinheit abgerechnet wird, z.B. Ct. oder €
    """
    preisstaffeln: list[Preisstaffel] = Field(..., title="Preisstaffeln")
    """
    Preisstaffeln, die zu dieser Preisposition gehören
    """
    tarifzeit: Tarifzeit | None = None
    """
    Festlegung, für welche Tarifzeit der Preis hier festgelegt ist
    """
    zeitbasis: Mengeneinheit | None = None
    """
    Festlegung, für welche Tarifzeit der Preis hier festgelegt ist
    """
    zonungsgroesse: Bemessungsgroesse | None = None
    """
    Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    steuersatz: Steuerkennzeichen
