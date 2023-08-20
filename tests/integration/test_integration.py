from pytest_django.asserts import assertTemplateUsed
from django.test import Client


client = Client()


def test_from_index_to_lettings(lettings_fixture, profiles_fixture):

    # Get the index page :
    response_index = client.get('/')

    # Check the get request to the index page succeeds :
    assert response_index.status_code == 200
    assertTemplateUsed(response_index, 'index.html')

    # Then get the lettings list page :
    response_lettings = client.get('/lettings/')

    # And check if I can consult the lettings list :
    assert response_lettings.status_code == 200
    assertTemplateUsed(response_lettings, 'lettings_index.html')


def test_from_index_to_profiles(lettings_fixture, profiles_fixture):

    # Get the index page :
    response_index = client.get('/')

    # Check the get request to the index page succeeds :
    assert response_index.status_code == 200
    assertTemplateUsed(response_index, 'index.html')

    # Then get the profiles list page :
    response_profiles = client.get('/profiles/')

    # And check if I can consult the profiles list :
    assert response_profiles.status_code == 200
    assertTemplateUsed(response_profiles, 'profiles_index.html')
