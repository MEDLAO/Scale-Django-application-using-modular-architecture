from django.urls import reverse, resolve
from oc_lettings_site.views import index


def test_index_url():

    """ Testing if the 'index' route maps to our 'index' view """

    url = reverse('index')
    assert resolve(url).view_name == 'index'
    assert resolve(url).func, index
