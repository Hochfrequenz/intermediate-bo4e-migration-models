class TestConsistency:
    def test_datasets_importable(self):
        """
        Test that all models and datasets are importable.
        """
        from ibims import datasets

        assert issubclass(datasets.TripicaCustomerLoaderDataSet, datasets.DataSetBaseModel)
