import json
from datetime import UTC, datetime
from pathlib import Path

from bo4e_generator.parser import get_bo4e_data_model_types, monkey_patch_relative_import
from datamodel_code_generator import DataModelType, PythonVersion
from datamodel_code_generator.model import get_data_model_types
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from pydantic import BaseModel

from ibims.bo4e import SepaInfo


class TestConsistency:
    def test_bo4e_generator(self):
        """
        Test that the bo4e generator can be imported.
        """
        from bo4e_generator.__main__ import generate_bo4e_schemas

        generate_bo4e_schemas(
            input_directory=Path(__file__).parents[1] / "tmp/bo4e_schemas",
            output_directory=Path(__file__).parents[1] / "tmp/bo4e_schemas",
            pydantic_v1=False,
            clear_output=True,
            target_version="v202401.2.1",
        )

    def test_pydantic_json(self):
        class A(BaseModel):
            a: str = "hallo"
            b: int = 1
            c: str
            d: str | None = None

        json_schema = json.dumps(A.model_json_schema(), indent=2)
        print(json_schema)
        data_model_types = data_model_types = get_data_model_types(
            DataModelType.PydanticV2BaseModel, target_python_version=PythonVersion.PY_311
        )
        monkey_patch_relative_import()
        parser = JsonSchemaParser(
            json_schema,
            data_model_type=data_model_types.data_model,
            data_model_root_type=data_model_types.root_model,
            data_model_field_type=data_model_types.field_model,
            data_type_manager_type=data_model_types.data_type_manager,
            dump_resolve_reference_action=data_model_types.dump_resolve_reference_action,
            # use_annotated=not pydantic_v1,
            use_double_quotes=True,
            use_schema_description=True,
            use_subclass_enum=True,
            use_standard_collections=True,
            use_union_operator=True,
            set_default_enum_member=True,
            snake_case_field=True,
            field_constraints=True,
            capitalise_enum_members=True,
            # base_path=input_directory,
            remove_special_field_name_prefix=True,
            allow_extra_fields=False,
            allow_population_by_field_name=True,
            use_default_kwarg=True,
            strict_nullable=True,
        )
        parse_result = parser.parse()
        print(parse_result)

    def test_datasets_importable(self):
        """
        Test that all models and datasets are importable.
        """
        # pylint: disable=import-outside-toplevel
        from ibims import datasets

        assert issubclass(datasets.TripicaCustomerLoaderDataSet, datasets.DataSetBaseModel)

    def test_sepa_info_construction_population_by_field_name(self):
        sepa_info_obj = SepaInfo(sepa_id="", sepa_zahler=True, gueltig_seit=datetime(2200, 1, 1, tzinfo=UTC))
        assert sepa_info_obj.sepa_id == ""
