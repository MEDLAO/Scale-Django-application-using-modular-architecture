import logging
from django.contrib import admin
from django.urls import path, include
from . import views

logger = logging.getLogger(__name__)


def trigger_error(request):
    division_by_zero = 1 / 0
    logger.error("ZeroDivisionErrorabc", exc_info=True)


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls', namespace='lettings')),
    path('', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

handler404 = 'oc_lettings_site.views.error_404_view'
handler500 = 'oc_lettings_site.views.error_500_view'
