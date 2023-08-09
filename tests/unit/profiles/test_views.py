from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


def test_profiles_index_view(profiles_fixture):

    """
    In the first assert, we are testing if our get request returns 200 (OK) status code.
    For the second assert,
    we are making sure that our view returns the profiles_index.html template.
    And for the third assert, we check that the 'expected_content' is in 'content'.
    """

    path = reverse('profiles:profiles_index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "username_test"

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles_index.html')
    assert expected_content in content


def test_profile_view(profiles_fixture):

    """
   In the first assert, we are testing if our get request returns 200 (OK) status code.
   For the second assert,
   we are making sure that our view returns the profile.html template.
   And for the third assert, we check that the 'expected_content' is in 'content'.
   """

    path = reverse('profiles:profile', kwargs={'username': 'username_test'})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p><strong>Favorite city :</strong> favorite_city_test</p>"

    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')
    assert expected_content in content
