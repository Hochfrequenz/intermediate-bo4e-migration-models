from pydantic import BaseModel, ConfigDict, Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.dienstleistungstyp import Dienstleistungstyp
from ..enum.netzebene import Netzebene
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geraet import Geraet
from .marktteilnehmer import Marktteilnehmer


class PreisblattHardware(BaseModel):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für zusätzliche Hardware

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattHardware.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattHardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/PreisblattHardware.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(
        default=None,
        alias="_id",
        description="Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)",
        title=" Id",
    )
    typ: Typ | None = Field(
        default=Typ.PREISBLATTHARDWARE,
        alias="_typ",
        description="Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode",
    )
    version: str | None = Field(
        default="v202401.2.1",
        alias="_version",
        description='Version der BO-Struktur aka "fachliche Versionierung"',
        title=" Version",
    )
    basisgeraet: Geraet | None = Field(
        default=None, description="Der Preis betriftt das hier angegebene Gerät, z.B. ein Tarifschaltgerät"
    )
    bezeichnung: str | None = Field(
        default=None, description="Eine Bezeichnung für das Preisblatt", title="Bezeichnung"
    )
    bilanzierungsmethode: Bilanzierungsmethode | None = Field(
        default=None, description="Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode"
    )
    gueltigkeit: Zeitraum | None = Field(default=None, description="Der Zeitraum für den der Preis festgelegt ist")
    herausgeber: Marktteilnehmer | None = Field(
        default=None, description="Der Netzbetreiber, der die Preise veröffentlicht hat"
    )
    inklusive_dienstleistungen: list[Dienstleistungstyp] | None = Field(
        default=None,
        alias="inklusiveDienstleistungen",
        description="Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung",
        title="Inklusivedienstleistungen",
    )
    inklusive_geraete: list[Geraet] | None = Field(
        default=None,
        alias="inklusiveGeraete",
        description="Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler",
        title="Inklusivegeraete",
    )
    messebene: Netzebene | None = Field(
        default=None, description="Die Preise gelten für Messlokationen in der angebebenen Netzebene"
    )
    preispositionen: list[Preisposition] | None = Field(
        default=None,
        description="Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc",
        title="Preispositionen",
    )
    preisstatus: Preisstatus | None = Field(
        default=None, description="Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt"
    )
    sparte: Sparte | None = Field(default=None, description="Preisblatt gilt für angegebene Sparte")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
