from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.geokoordinaten import Geokoordinaten
from ..com.katasteradresse import Katasteradresse
from ..com.messlokationszuordnung import Messlokationszuordnung
from ..com.verbrauch import Verbrauch
from ..com.zaehlwerk import Zaehlwerk
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.energierichtung import Energierichtung
from ..enum.gasqualitaet import Gasqualitaet
from ..enum.gebiettyp import Gebiettyp
from ..enum.kundentyp import Kundentyp
from ..enum.marktgebiet import Marktgebiet
from ..enum.messtechnische_einordnung import MesstechnischeEinordnung
from ..enum.netzebene import Netzebene
from ..enum.profiltyp import Profiltyp
from ..enum.prognosegrundlage import Prognosegrundlage
from ..enum.regelzone import Regelzone
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.variant import Variant
from ..enum.verbrauchsart import Verbrauchsart
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner


class Marktlokation(BaseModel):
    """
    Object containing information about a Marktlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Marktlokation.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.MARKTLOKATION, alias="_typ")
    """
    Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bilanzierungsgebiet: str | None = Field(default=None, title="Bilanzierungsgebiet")
    """
    Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes
    """
    bilanzierungsmethode: Bilanzierungsmethode | None = None
    """
    Die Bilanzierungsmethode, RLM oder SLP
    """
    endkunde: Geschaeftspartner | None = None
    """
    Geschäftspartner, dem diese Marktlokation gehört
    """
    energierichtung: Energierichtung | None = None
    """
    Kennzeichnung, ob Energie eingespeist oder entnommen (ausgespeist) wird
    """
    gasqualitaet: Gasqualitaet | None = None
    """
    Die Gasqualität in diesem Netzgebiet. H-Gas oder L-Gas. Im Falle eines Gas-Netzes
    """
    gebietstyp: Gebiettyp | None = None
    """
    Typ des Netzgebietes, z.B. Verteilnetz
    """
    geoadresse: Geokoordinaten | None = None
    """
    katasterinformation: Optional["Katasteradresse"] = None
    """
    grundversorgercodenr: str | None = Field(default=None, title="Grundversorgercodenr")
    """
    Codenummer des Grundversorgers, der für diese Marktlokation zuständig ist
    """
    ist_unterbrechbar: bool | None = Field(default=None, alias="istUnterbrechbar", title="Istunterbrechbar")
    """
    Gibt an, ob es sich um eine unterbrechbare Belieferung handelt
    """
    katasterinformation: Katasteradresse | None = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """
    kundengruppen: list[Kundentyp] | None = Field(default=None, title="Kundengruppen")
    """
    Kundengruppen der Marktlokation
    """
    lokationsadresse: Adresse | None = None
    """
    Die Adresse, an der die Energie-Lieferung oder -Einspeisung erfolgt
    """
    marktgebiet: Marktgebiet | None = None
    marktlokations_id: str = Field(..., alias="marktlokationsId", title="Marktlokationsid")
    """
    Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    """
    netzbetreibercodenr: str | None = Field(default=None, title="Netzbetreibercodenr")
    """
    Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation angeschlossen ist.
    """
    netzebene: Netzebene | None = None
    """
    Netzebene, in der der Bezug der Energie erfolgt.
    Bei Strom Spannungsebene der Lieferung, bei Gas Druckstufe.
    Beispiel Strom: Niederspannung Beispiel Gas: Niederdruck.
    """
    netzgebietsnr: str | None = Field(default=None, title="Netzgebietsnr")
    """
    Die ID des Gebietes in der ene't-Datenbank
    """
    regelzone: str | None = Field(default=None, title="Regelzone")
    """
    Kundengruppen der Marktlokation
    """
    sparte: Sparte
    """
    Sparte der Marktlokation, z.B. Gas oder Strom
    """
    verbrauchsart: Verbrauchsart | None = None
    """
    Verbrauchsart der Marktlokation.
    """
    verbrauchsmengen: list[Verbrauch] | None = Field(default=None, title="Verbrauchsmengen")
    zaehlwerke: list[Zaehlwerk] | None = Field(default=None, title="Zaehlwerke")
    """
    für Gas. Code vom EIC, https://www.entsog.eu/data/data-portal/codes-list
    """
    zaehlwerke_der_beteiligten_marktrolle: list[Zaehlwerk] | None = Field(
        default=None,
        alias="zaehlwerkeDerBeteiligtenMarktrolle",
        title="Zaehlwerkederbeteiligtenmarktrolle",
    )
    zugehoerige_messlokation: Messlokationszuordnung | None = Field(default=None, alias="zugehoerigeMesslokation")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    messtechnische_einordnung: MesstechnischeEinordnung = Field(..., alias="messtechnischeEinordnung")
    uebertragungsnetzgebiet: Regelzone | None = None
    variant: Variant
    community_id: str = Field(..., alias="communityId", title="Communityid")
    prognose_grundlage: Prognosegrundlage | None = Field(default=None, alias="prognoseGrundlage")
    prognose_grundlage_detail: Profiltyp | None = Field(default=None, alias="prognoseGrundlageDetail")
