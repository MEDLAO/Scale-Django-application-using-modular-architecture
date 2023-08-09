import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client
from django.contrib import auth
from django.contrib.auth.views import LoginView


@pytest.mark.django_db
def test_login_route():

    client = Client()

 #GET the index page :

    temp_user = client.post(reverse('signup'), credentials)

    #Connecter cet utilisateur avec la vue `login`
    response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    #Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 302
    assert response.url == reverse('home')

    #Vérifier que l’utilisateur est bien authentifié
    user = auth.get_user(client)
    assert user.is_authenticated