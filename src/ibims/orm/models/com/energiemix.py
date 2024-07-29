import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.oekolabel import Oekolabel
from ibims.orm.models.enum.oekozertifikat import Oekozertifikat
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.many import EnergiemixanteilLink, EnergiemixzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifinfo import Tarifinfo
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.energieherkunft import Energieherkunft
    from ibims.orm.models.com.regionaler_auf_abschlag import RegionalerAufAbschlag
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Energiemix(SQLModel, table=True):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energiemix.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Energiemix.json>`_
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
    atommuell: float | None = Field(default=None, title="Atommuell")
    """
    Höhe des erzeugten Atommülls in g/kWh
    """
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    """
    Bemerkung zum Energiemix
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Energiemix
    """
    co2_emission: float | None = Field(default=None, alias="co2Emission", title="Co2Emission")
    """
    Höhe des erzeugten CO2-Ausstosses in g/kWh
    """
    energiemixnummer: int | None = Field(default=None, title="Energiemixnummer")
    """
    Eindeutige Nummer zur Identifizierung des Energiemixes
    """
    gueltigkeitsjahr: int | None = Field(default=None, title="Gueltigkeitsjahr")
    """
    Jahr, für das der Energiemix gilt
    """
    ist_in_oeko_top_ten: bool | None = Field(default=None, alias="istInOekoTopTen", title="Istinoekotopten")
    """
    Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite, auf der die Strommixdaten veröffentlicht sind
    """
    energiemix_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_energiemix: List["Regionaltarif"] = Relationship(
        back_populates="energiemix",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.energiemix_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    tarif_energiemix: List["Tarif"] = Relationship(
        back_populates="energiemix",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.energiemix_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    tarifinfo_energiemix: List["Tarifinfo"] = Relationship(
        back_populates="energiemix",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifinfo.energiemix_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    tarifkosten_energiemix: List["Tarifkosten"] = Relationship(
        back_populates="energiemix",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifkosten.energiemix_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_energiemix: List["Tarifpreisblatt"] = Relationship(
        back_populates="energiemix",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.energiemix_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    aufabschlagregional_energiemixaenderung: List["AufAbschlagRegional"] = Relationship(
        back_populates="energiemixaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "AufAbschlagRegional.energiemixaenderung_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
    anteil: List["Energieherkunft"] = Relationship(
        back_populates="energiemix_anteil_link", link_model=EnergiemixanteilLink
    )
    energieart: Sparte | None = Field(None)
    oekolabel: List[Oekolabel] | None = Field(None, sa_column=Column(ARRAY(Enum(Oekolabel, name="oekolabel"))))
    oekozertifikate: List[Oekozertifikat] | None = Field(
        None, sa_column=Column(ARRAY(Enum(Oekozertifikat, name="oekozertifikat")))
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="energiemix_zusatzattribute_link",
        link_model=EnergiemixzusatzAttributeLink,
    )
    regionaleraufabschlag_energiemixaenderung: List["RegionalerAufAbschlag"] = Relationship(
        back_populates="energiemixaenderung",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalerAufAbschlag.energiemixaenderung_id==Energiemix.energiemix_sqlid",
            "lazy": "joined",
        },
    )
