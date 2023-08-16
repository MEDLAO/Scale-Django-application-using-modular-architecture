from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

client = Client()


def test_index():

    """

    In the first assert, we are testing if our get request returns 200 (OK) status code.
    For the second assert, we are making sure that our view returns the index.html template

    """

    response = client.get(reverse('index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
