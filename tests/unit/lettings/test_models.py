from django.test import Client


client = Client()


def test_letting_model(lettings_fixture):

    """
    Testing whether Letting's __str__ method is implemented properly
    """
    address_obj, letting_obj = lettings_fixture
    expected_value = f'{address_obj.number} {address_obj.street}'
    assert str(address_obj) == expected_value


def test_address_model(lettings_fixture):

    """
    Testing whether Address's __str__ method is implemented properly
    """

    address_obj, letting_obj = lettings_fixture
    expected_value = letting_obj.title
    assert str(letting_obj) == expected_value
