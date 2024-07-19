from datetime import UTC, datetime

from ibims.bo4e import SepaInfo


class TestConsistency:
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
