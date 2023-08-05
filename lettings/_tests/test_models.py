import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Address, Letting

client = Client()


@pytest.mark.django_db
def test_letting():
    """
       In the first assert, we are testing if our get request returns 200 (OK) status code.
       For the second assert,
       we are making sure that our view returns the letting.html template.
       And for the third assert, we check that the 'expected_content' is in 'content'.
       """
    address_obj = Address.objects.create(
        number=1234,
        street='address_test',
        city='city_test',
        state='state_test',
        zip_code=12345,
        country_iso_code=123
    )
    Letting.objects.create(
        title='title_test',
        address=address_obj.id
    )
    path = reverse('letting', kwargs={'letting_id': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_value = "1234 address_test"

    assert str(address_obj) == expected_value
