from django.urls import reverse, resolve
from lettings.views import lettings_index, letting


def test_lettings_index_url():

    """ Testing if the 'lettings_index' route maps to our 'lettings_index' view """

    url = reverse('lettings:lettings_index')
    assert resolve(url).view_name == 'lettings:lettings_index'
    assert resolve(url).func, lettings_index


def test_letting_url():

    """ Testing if the 'letting' route maps to our 'letting' view """

    url = reverse('lettings:letting', kwargs={'letting_id': 1})
    assert resolve(url).view_name == 'lettings:letting'
    assert resolve(url).func, letting
