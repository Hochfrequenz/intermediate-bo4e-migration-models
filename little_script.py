import json
import re
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

import requests
from bo4e_generator.__main__ import generate_bo4e_schemas
from bost.__main__ import main as bost_main
from pydantic import BaseModel, TypeAdapter
from requests import Response

from ibims.bo.bilanzierung import Bilanzierung
from ibims.bo.dokument import Dokument
from ibims.bo.file import File
from ibims.bo.geschaeftspartner import GeschaeftspartnerErweitert
from ibims.bo.hinweis import Hinweis
from ibims.bo.kampagne import Kampagne
from ibims.bo.marktlokation_erweitert import MarktlokationErweitert, Variant
from ibims.bo.rechnung import RechnungErweitert
from ibims.bo.zaehler import ZaehlerErweitert, ZaehlerGas
from ibims.com.adresse import AdresseErweitert
from ibims.com.bankverbindung import Bankverbindung
from ibims.com.concessionfee import ConcessionFee
from ibims.com.lastprofil import Lastprofil
from ibims.com.preisgarantie import PreisgarantieErweitert
from ibims.com.preisposition import PreispositionErweitert
from ibims.com.rechnungsposition import RechnungspositionErweitert
from ibims.com.sepa_info import SepaInfo
from ibims.com.steuerbetrag import SteuerbetragErweitert
from ibims.com.verbrauch import AblesendeRolle, Ablesungsstatus, VerbrauchErweitert
from ibims.com.vertragskonto import Vertragskonto, VertragskontoCBA, VertragskontoMBA
from ibims.com.zaehlpunkt import Zaehlpunkt
from ibims.com.zaehlwerk import ZaehlwerkErweitert
from ibims.enum.abgabeart import Abgabeart
from ibims.enum.aggregationsverantwortung import Aggregationsverantwortung
from ibims.enum.bdewartikelnummer import BDEWArtikelnummerErweitert
from ibims.enum.botyp import BoTypErweitert
from ibims.enum.hinweisthema import HinweisThema
from ibims.enum.messtechnische_einordnung import MesstechnischeEinordnung
from ibims.enum.messwerterfassung import Messwerterfassung
from ibims.enum.messwertstatus import Messwertstatus
from ibims.enum.profiltyp import Profiltyp
from ibims.enum.prognosegrundlage import Prognosegrundlage
from ibims.enum.rechnung_erweitert import RechnungstypErweitert
from ibims.enum.regelzone import Marktgebiet, Regelzone
from ibims.enum.zaehlertyp_erweitert import ZaehlerTypErweitert

REF_REGEX = re.compile(r"^#/\$defs/(\w+)$")


def update_reference(field: dict[str, str], own_module: str, namespace: dict[str, str], cur_class: str):
    """
    Update a reference to a schema file by replacing a URL reference with a relative path.
    Example of the old reference:
    https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/v0.6.1-rc13/src/bo4e_schemas/enum/AbgabeArt.json
    """
    match = REF_REGEX.search(field["$ref"])
    if match is None:
        return
    reference_name = match.group(1) if not match.group(1).endswith("Erweitert") else match.group(1)[: -len("Erweitert")]
    if reference_name == "ZaehlerTyp":
        reference_name = "Zaehlertyp"
    if reference_name not in namespace:
        raise ValueError(f"Unknown class reference inside {cur_class}: {reference_name}")

    if own_module == namespace[reference_name]:
        field["$ref"] = f"{reference_name}.json#"
    else:
        field["$ref"] = f"../{namespace[reference_name]}/{reference_name}.json#"


def update_references(
    obj: dict[str, Any] | list[Any], own_module: str, namespace: dict[str, str], class_name: Optional[str] = None
):
    """
    Update all references in a schema object. Iterates through the whole structure and calls `update_reference`
    on every Reference object.
    """
    if class_name is None:
        class_name = obj["title"]

    def update_or_iter(_object: dict[str, Any] | list[Any]):
        if isinstance(_object, dict):
            iter_dict(_object)
            if "$ref" in _object:
                update_reference(_object, own_module, namespace, class_name)
            # if "allOf" in _object:
            #     _object["anyOf"] = _object["allOf"]
            #     del _object["allOf"]
        elif isinstance(_object, list):
            iter_list(_object)

    def iter_dict(_object: dict[str, Any]):
        for prop in _object.values():
            update_or_iter(prop)

    def iter_list(_object: list[Any]):
        for prop in _object:
            update_or_iter(prop)

    update_or_iter(obj)


OWNER = "Hochfrequenz"
REPO = "BO4E-Schemas"
TIMEOUT = 10  # in seconds


@lru_cache(maxsize=None)
def _github_tree_query(pkg: str, version: str) -> Response:
    """
    Query the github tree api for a specific package and version.
    """
    return requests.get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/contents/src/bo4e_schemas/{pkg}?ref={version}", timeout=TIMEOUT
    )


def bo4e_namespace(version: str) -> dict[str, str]:
    """
    Get all files from the BO4E-Schemas repository.
    This generator function yields tuples of class name and SchemaMetadata objects containing various information about
    the schema.
    """
    namespace = {}
    for pkg in ("bo", "com", "enum"):
        response = _github_tree_query(pkg, version)
        for file in response.json():
            if not file["name"].endswith(".json"):
                continue
            class_name = Path(file["path"]).stem
            namespace[class_name] = pkg
    return namespace


def main():
    OUTPUT_PATH = Path(__file__).parent / "bo4e/models"
    additional_models = {
        "bo": [
            Bilanzierung,
            Dokument,
            File,
            Hinweis,
            Kampagne,
            ZaehlerGas,
            ZaehlerErweitert,
            RechnungErweitert,
            MarktlokationErweitert,
            GeschaeftspartnerErweitert,
        ],
        "com": [
            AdresseErweitert,
            Bankverbindung,
            ConcessionFee,
            Lastprofil,
            PreisgarantieErweitert,
            PreispositionErweitert,
            RechnungspositionErweitert,
            SepaInfo,
            SteuerbetragErweitert,
            VerbrauchErweitert,
            Vertragskonto,
            VertragskontoCBA,
            VertragskontoMBA,
            Zaehlpunkt,
            ZaehlwerkErweitert,
        ],
        "enum": [
            Abgabeart,
            AblesendeRolle,
            Ablesungsstatus,
            Aggregationsverantwortung,
            BDEWArtikelnummerErweitert,
            BoTypErweitert,
            HinweisThema,
            MesstechnischeEinordnung,
            Messwerterfassung,
            Messwertstatus,
            Profiltyp,
            Prognosegrundlage,
            RechnungstypErweitert,
            Marktgebiet,
            Regelzone,
            Variant,
            ZaehlerTypErweitert,
        ],
    }
    namespace = bo4e_namespace("v0.6.1")
    # namespace["BoTyp"] = "enum"
    # namespace["Tarifart"] = "enum"
    # namespace["Geraetemerkmal"] = "enum"
    for module, models in additional_models.items():
        for model in models:
            if model.__name__.endswith("Erweitert"):
                continue
            namespace[model.__name__] = module
    for module, models in additional_models.items():
        if module == "enum":
            continue
        for model in models:
            if not model.__name__.endswith("Erweitert"):
                continue
            original_name = model.__name__[: -len("Erweitert")]
            out_file = OUTPUT_PATH / module / f"{original_name}_extension.json"
            out_file.parent.mkdir(parents=True, exist_ok=True)
            schema = model.model_json_schema()
            output = []
            for key, value in schema["properties"].items():
                assert issubclass(model.__base__, BaseModel)
                if any(
                    key == field_info.alias if field_info.alias is not None else key == field_name
                    for field_name, field_info in model.__base__.model_fields.items()
                ):
                    continue
                output.append({"pattern": f"{module}\\.{original_name}", "fieldName": key, "fieldDef": value})
            update_references(output, module, namespace, class_name=original_name)
            json.dump(output, out_file.open("w"), indent=2)
    for module, models in additional_models.items():
        for model in models:
            if model.__name__.endswith("Erweitert"):
                continue
            out_file = OUTPUT_PATH / module / f"{model.__name__}.json"
            out_file.parent.mkdir(parents=True, exist_ok=True)
            if issubclass(model, BaseModel):
                schema = model.model_json_schema()
            elif issubclass(model, Enum):
                schema = TypeAdapter(model).json_schema()
            else:
                raise ValueError(f"Unknown model type: {model}")

            if "$defs" in schema:
                del schema["$defs"]
            update_references(schema, module, namespace)
            json.dump(schema, out_file.open("w"), indent=2)


if __name__ == "__main__":
    main()
    bost_main(
        output=Path("tmp/bo4e_schemas"),
        target_version="v0.6.1",
        config_file=Path("bo4e/bo4e_config.json"),
        update_refs=True,
        set_default_version=True,
    )
    generate_bo4e_schemas(Path("tmp/bo4e_schemas"), Path("src/ibims/bo4e"))
