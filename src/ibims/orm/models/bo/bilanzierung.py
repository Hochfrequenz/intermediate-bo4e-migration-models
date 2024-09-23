import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, String
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.aggregationsverantwortung import Aggregationsverantwortung
from ibims.orm.models.enum.profiltyp import Profiltyp
from ibims.orm.models.enum.prognosegrundlage import Prognosegrundlage
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import BilanzierunglastprofileLink, BilanzierungzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.lastprofil import Lastprofil
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Bilanzierung(SQLModel, table=True):
    """
    Bilanzierung is a business object used for balancing. This object is no BO4E standard and a complete go
    implementation can be found at
    https://github.com/Hochfrequenz/go-bo4e/blob/3414a1eac741542628df796d6beb43eaa27b0b3e/bo/bilanzierung.go
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    id: str | None = Field(default=None, alias="_id", title=" Id")
    bilanzierungsbeginn: datetime = Field(..., title="Bilanzierungsbeginn")
    bilanzierungsende: datetime = Field(..., title="Bilanzierungsende")
    bilanzkreis: str | None = Field(default=None, title="Bilanzkreis")
    bilanzierung_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ = Field(Typ.BILANZIERUNG)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="bilanzierung_zusatzattribute_link",
        link_model=BilanzierungzusatzAttributeLink,
    )
    aggregationsverantwortung: Aggregationsverantwortung | None = Field(None)
    lastprofile: List["Lastprofil"] = Relationship(
        back_populates="bilanzierung_lastprofile_link",
        link_model=BilanzierunglastprofileLink,
    )
    prognosegrundlage: Prognosegrundlage | None = Field(None)
    detailsPrognosegrundlage: Profiltyp | None = Field(None)
    lastprofilNamen: List[str] | None = Field(None, title="lastprofilNamen", sa_column=Column(ARRAY(String)))
