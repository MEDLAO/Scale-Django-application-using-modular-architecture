from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


def test_lettings_index_view(lettings_fixture):

    """
    In the first assert, we are testing if our get request returns 200 (OK) status code.
    For the second assert,
    we are making sure that our view returns the lettings_index.html template.
    And for the third assert, we check that the 'expected_content' is in 'content'.
    """

    path = reverse('lettings:lettings_index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "title_test"

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings_index.html')
    assert expected_content in content


def test_letting_view(lettings_fixture):

    """
   In the first assert, we are testing if our get request returns 200 (OK) status code.
   For the second assert,
   we are making sure that our view returns the letting.html template.
   And for the third assert, we check that the 'expected_content' is in 'content'.
   """

    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p>1234 address_test</p>"

    assert response.status_code == 200
    assertTemplateUsed(response, 'letting.html')
    assert expected_content in content
