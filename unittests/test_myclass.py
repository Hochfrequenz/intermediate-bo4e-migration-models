from ibims.mymodule import MyClass


class TestMyClass:
    """
    A class with pytest unit tests.
    """

    def test_something(self):
        my_class = MyClass()
        assert my_class.do_something() == "abc"

    def test_datasets_importable(self):
        from ibims import datasets

        assert issubclass(datasets.TripicaCustomerLoaderDataSet, datasets.DataSetBaseModel)
