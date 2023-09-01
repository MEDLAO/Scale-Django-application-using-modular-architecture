.. Mettez à l'échelle une application Django en utilisant une architecture modulaire documentation master file, created by
   sphinx-quickstart on Thu Aug 24 18:58:07 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Mettez à l'échelle une application Django en utilisant une architecture modulaire
=============================================================================================================

Description du projet
========================

Orange County Lettings, une start-up en pleine croissance spécialisée dans la location immobilière,
élargit son champ d'action aux États-Unis. En tant que membre de l'équipe de développement,
mon rôle revêt une importance cruciale pour optimiser le site, couvrant à la fois le code et le
processus de déploiement.

Sous la supervision de Dominique, le directeur technique, une évaluation approfondie des
technologies actuellement utilisées dans le code de l'application a été entreprise.
Cette évaluation a mis en évidence plusieurs problématiques qui me sont attribuées pour résolution.
Mon expertise sera mise à contribution pour aborder ces problèmes identifiés, visant à garantir
la performance et la pérennité du site.

Les domaines du site et du déploiement à améliorer et/ou à ajouter :

1. Refonte de **l'architecture modulaire** dans le repository GitHub

2. Réduction de diverses **dettes techniques** sur le projet

3. Ajout d'un **pipeline CI/CD** ainsi que son déploiement

4. Surveillance de l’application et **suivi des erreurs** via Sentry

5. Création de la documentation technique de l’application avec Read The Docs et Sphinx.

Les instructions sur l’installation du projet
=============================================

 `Cf. README.me <https://github.com/MEDLAO/Scale-Django-application-using-modular-architecture.git>`_

Un guide de démarrage rapide
============================

Pour accéder à l'application en local,

* il faut récupérer l'image Docker de l'application depuis Docker Hub en tapant la commande suivante dans un terminal :

.. code-block::

   docker pull medlao/project-13-sml

* puis lancer le conteneur associé à cette image :

.. code-block::

   docker run -p 8000:8000 medlao/project-13-sml

* une fois que le serveur est lancé, accéder au site via l'url indiqué.


Les technologies et les langages de programmation à utiliser
=============================================================

* Python 3
* Linux
* Windows
* MacOS
* Docker


Modules utilisés
================

* alabaster 0.7.13
* asgiref 3.7.2
* Babel 2.12.1
* certifi 2023.7.22
* charset-normalizer 3.2.0
* coverage 7.3.0
* Django 3.0
* docutils 0.20.1
* entrypoints 0.3
* exceptiongroup 1.1.2
* flake8 3.7.0
* idna 3.4
* imagesize 1.4.1
* iniconfig 2.0.0
* Jinja2 3.1.2
* MarkupSafe 2.1.3
* mccabe 0.6.1
* packaging 23.1
* pluggy 1.2.0
* pycodestyle 2.5.0
* pyflakes 2.1.1
* Pygments 2.16.1
* pytest 7.4.0
* pytest-django 3.9.0
* python-dotenv 1.0.0
* pytz 2023.3
* requests 2.31.0
* sentry-sdk 1.29.2
* six 1.16.0
* snowballstemmer 2.2.0
* Sphinx 7.2.3
* sphinxcontrib-applehelp 1.0.7
* sphinxcontrib-devhelp 1.0.5
* sphinxcontrib-htmlhelp 2.0.4
* sphinxcontrib-jsmath 1.0.1
* sphinxcontrib-qthelp 1.0.6
* sphinxcontrib-serializinghtml 1.1.9
* sqlparse 0.4.4
* tomli 2.0.1
* typing_extensions 4.7.1
* urllib3 2.0.4
* whitenoise 6.5.0


Description de la structure de la base de données et des modèles de données
============================================================================

Le back-end de ce projet Django est constitué de deux applications :

* **lettings** : contenant deux classes liées entre elles par une relation one-to-one :

  * **Address**
  * **Letting**

* **profiles** : contenant une classe liée à la classe User de Django par une relation one-to-one :

  * **Profile**


Concernant le stockage des données, une base de données **SQLite** a été utilisé.


Un guide d’utilisation
======================

Cette application web possède **une page d'accueil** contenant un **menu** :

* *Profiles* : donne accès à la **liste des profils** enregistrés dans la base de données.

  * Il est également possible d'accéder aux **détails** (nom, prénom, email, etc) d'un **profil** en particulier.

* *Lettings* : donne accès à la **liste des locations**.

  * Il est possible d'accéder aux **détails** (ville, adresse, etc) d'une **location** en particulier.


Déploiement et gestion de l'application
========================================

Le déploiement de cette application web a été réalisé avec l'outil **DigitalOcean** via un **pipeline CI/CD** mis en place avec l'outil **GitLab**.

La version déployée du site : `Orange County Lettings <http://159.89.16.25/>`_