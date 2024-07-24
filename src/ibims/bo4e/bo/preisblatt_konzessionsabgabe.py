from pydantic import BaseModel, ConfigDict, Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.kundengruppe_ka import KundengruppeKA
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .marktteilnehmer import Marktteilnehmer


class PreisblattKonzessionsabgabe(BaseModel):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/PreisblattKonzessionsabgabe.json>`_
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
        default=Typ.PREISBLATTKONZESSIONSABGABE,
        alias="_typ",
        description="Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist",
    )
    version: str | None = Field(
        default="v202401.2.1",
        alias="_version",
        description='Version der BO-Struktur aka "fachliche Versionierung"',
        title=" Version",
    )
    bezeichnung: str | None = Field(
        default=None, description="Eine Bezeichnung für das Preisblatt", title="Bezeichnung"
    )
    gueltigkeit: Zeitraum | None = Field(default=None, description="Der Zeitraum für den der Preis festgelegt ist")
    herausgeber: Marktteilnehmer | None = Field(
        default=None, description="Der Netzbetreiber, der die Preise veröffentlicht hat"
    )
    kundengruppe_ka: KundengruppeKA | None = Field(
        default=None,
        alias="kundengruppeKA",
        description="Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist",
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
