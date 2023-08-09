from django.urls import reverse, resolve
from profiles.views import profiles_index, profile


def test_profiles_index_url():

    """ Testing if the 'profiles_index' route maps to our 'profiles_index' view """

    url = reverse('profiles:profiles_index')
    assert resolve(url).view_name == 'profiles:profiles_index'
    assert resolve(url).func, profiles_index


def test_profile_url(profiles_fixture):

    """ Testing if the 'profile' route maps to our 'profile' view """

    path = reverse('profiles:profile', kwargs={'username': 'username_test'})

    assert path == "/profiles/username_test/"
    assert resolve(path).view_name == 'profiles:profile'
    assert resolve(path).func, profile
