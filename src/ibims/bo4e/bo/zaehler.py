from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.befestigungsart import Befestigungsart
from ..enum.messwerterfassung import Messwerterfassung
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.zaehlerauspraegung import Zaehlerauspraegung
from ..enum.zaehlergroesse import Zaehlergroesse
from ..enum.zaehlertyp import Zaehlertyp
from ..enum.zaehlertyp_spezifikation import ZaehlertypSpezifikation

if TYPE_CHECKING:
    from ..com.zaehlwerk import Zaehlwerk
    from ..com.zeitraum import Zeitraum
    from ..zusatz_attribut import ZusatzAttribut
    from .geraet import Geraet
    from .geschaeftspartner import Geschaeftspartner


class Zaehler(BaseModel):
    """
    Object containing information about a meter/"Zaehler".

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehler.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehler JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/bo/Zaehler.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Hier kÃ¶nnen IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.ZAEHLER, alias="_typ")
    """
    Typisierung des ZÃ¤hlers
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    befestigungsart: Optional[Befestigungsart] = None
    """
    Besondere Spezifikation des ZÃ¤hlers
    """
    eichung_bis: Optional[datetime] = Field(default=None, alias="eichungBis", title="Eichungbis")
    """
    ZÃ¤hlerkonstante auf dem ZÃ¤hler
    """
    geraete: Optional[list["Geraet"]] = Field(default=None, title="Geraete")
    """
    GrÃ¶ÃŸe des ZÃ¤hlers
    """
    ist_fernschaltbar: Optional[bool] = Field(default=None, alias="istFernschaltbar", title="Istfernschaltbar")
    """
    Der Hersteller des ZÃ¤hlers
    """
    letzte_eichung: Optional[datetime] = Field(default=None, alias="letzteEichung", title="Letzteeichung")
    """
    Bis zu diesem Datum (exklusiv) ist der ZÃ¤hler geeicht.
    """
    messwerterfassung: Optional[Messwerterfassung] = Field(default=None, title="Messwerterfassung")
    registeranzahl: Optional[Registeranzahl] = None
    """
    Spezifikation bezÃ¼glich unterstÃ¼tzter Tarif
    """
    sparte: Sparte
    """
    Nummerierung des ZÃ¤hlers,vergeben durch den Messstellenbetreiber
    """
    zaehlerauspraegung: Optional[Zaehlerauspraegung] = None
    """
    Strom oder Gas
    """
    zaehlergroesse: Optional[Zaehlergroesse] = None
    """
    Befestigungsart
    """
    zaehlerhersteller: Optional["Geschaeftspartner"] = None
    """
    Der Hersteller des ZÃ¤hlers
    """
    zaehlerkonstante: Optional[Decimal] = Field(default=None, title="Zaehlerkonstante")
    """
    Spezifikation bezÃ¼glich unterstÃ¼tzter Tarif
    """
    zaehlernummer: str = Field(..., title="Zaehlernummer")
    """
    Nummerierung des ZÃ¤hlers,vergeben durch den Messstellenbetreiber
    """
    zaehlertyp: Optional[Zaehlertyp] = None
    """
    Spezifikation die Richtung des ZÃ¤hlers betreffend
    """
    zaehlertyp_spezifikation: Optional[ZaehlertypSpezifikation] = Field(default=None, alias="zaehlertypSpezifikation")
    """
    Messwerterfassung des ZÃ¤hlers
    """
    zaehlwerke: list["Zaehlwerk"] = Field(..., title="Zaehlwerke")
    """
    Typisierung des ZÃ¤hlers
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    nachstes_ablesedatum: Optional[datetime] = Field(
        default=None, alias="nachstesAblesedatum", title="Nachstesablesedatum"
    )
    aktiver_zeitraum: Optional["Zeitraum"] = Field(default=None, alias="aktiverZeitraum")
