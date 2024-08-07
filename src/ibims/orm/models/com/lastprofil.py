import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.profiltyp import Profiltyp
from ibims.orm.models.many import BilanzierunglastprofileLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.bilanzierung import Bilanzierung


class Lastprofil(SQLModel, table=True):
    """
    This is not part of the official BO4E standard, but is implemented in the c# and go versions:
    https://github.com/Hochfrequenz/BO4E-dotnet/blob/9bdc151170ddba5c9d7535e863d5a396fe7fec52/BO4E/COM/Lastprofil.cs
    https://github.com/Hochfrequenz/go-bo4e/blob/708b39de0dcea8a9448ed4e7341a2687f6bf7c11/com/lastprofil.go
    Fields, which are not needed for migrations, are omitted and the field "profilart" is modelled as Profiltyp ENUM.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    einspeisung: bool | None = Field(default=False, title="Einspeisung")
    lastprofil_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    bilanzierung_lastprofile_link: List["Bilanzierung"] = Relationship(
        back_populates="lastprofile", link_model=BilanzierunglastprofileLink
    )
    profilart: Profiltyp | None = Field(None)
