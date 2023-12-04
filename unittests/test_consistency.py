class TestConsistency:
    def test_datasets_importable(self):
        """
        Test that all models and datasets are importable.
        """
        # pylint: disable=import-outside-toplevel
        from ibims import datasets

        assert issubclass(datasets.TripicaCustomerLoaderDataSet, datasets.DataSetBaseModel)
