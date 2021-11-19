# DSaster
- [DSaster](#dsaster)
- [A propos](#a-propos)
- [Installation](#installation)
  - [Git](#git)
- [Description des composants](#description-des-composants)
  - [api](#api)
  - [front](#front)
  - [robot](#robot)
  - [setup](#setup)
  - [volumes](#volumes)
  - [Keycloak](#keycloak)
  - [Kong](#kong)
  - [Docker](#docker)
- [Utilisation](#utilisation)

# A propos
DSaster est une application permettant de découvrir les derniers tremblements de terre recensés par
[USGS](https://www.usgs.gov/) en accédant à une interface personnalisée selon votre compte.

L'application prend en compte différents principe du développement *full-stack* grâce aux composants
suivants :
- Authentification avec ***Keycloak***
- L'API avec ***FastAPI (Python)***
- Base de données pour les tremblements de terre avec ***MongoDB***
- Service de *gateway* avec ***Kong***
- Base de données pour les services d'authentification et *gateway* avec ***PostgreSQL***
- Un script ***Python*** qui appelle l'API de **USGS** pour récupérer et sauvegarder les données

**Remarque**
: Seul l'API a été ajouté comme service avec ***Kong*** sur le gateway.

# Installation

## Git
L'application peut être téléchargé sur **GitHub** en appuyant sur le bouton *Code/Download ZIP* ou 
en faisant en utilisant les autres méthodes avec *https*, *ssh* ou *GitHub-CLI*.

# Description des composants
## api
Le dossier *api* contient le code **Python** pour l'API de l'application pour faire les requêtes
d'insertion, de récupération et d'opérations sur ou à partir des données.
L'API est accessible depuis *[localhost:8000](http://localhost:8000)* ou *[0.0.0.0:8000](http://0.0.0.0:8000)*.

## front
Le dossier *front* se présente sous la forme d'un projet **React**, celui sert à générer l'interface web
et permet la liaison entre l'interface web avec le système d'authentification **Keycloak**.
L'interface web est accessible depuis *[localhost:3000](http://localhost:3000)* ou *[0.0.0.0:3000](http://0.0.0.0:3000)*.

## robot
Le dossier *robot* contient le code **Python** pour l'automatisation de l'appel sur l'API de USGS pour récupérer
les tremblements de terre à des intervalles de temps réguliers.

## setup
Le dossier *setup* contient :
- le code **Python** pour automatiser la mise en place du service de l'API sur **Kong** ave le fichier
  *services.json*
- le fichier *docker_postgres_init.sql* pour initialiser la base de données **PostgreSQL** pour
  **Keycloak** et **Kong**
- le fichier *dsaster-realm.json* pour initialiser le dsaster *realm* de **Keycloak**

## volumes
Le dossier qui permettra de garder les données en local et non pas sur les *containers* **Docker**
uniquement.

## Keycloak
Le composant **Keycloak** pour l'authentification est accessible depuis *[localhost:8080](http://localhost:8080)* 
ou *[0.0.0.0:8080](http://0.0.0.0:8080)*.

## Kong
Le composant **Kong** en tant que *gatexay* est accessible depuis *[localhost:8001](http://localhost:8001)*, 
*[0.0.0.0:8001](http://0.0.0.0:8001)*, *[localhost:80002](http://localhost:8002)* et *[0.0.0.0:8002](http://0.0.0.0:8002)*.
Ici le port *8001* est pour l'admin et le port *8002* pour la consommation des *services*.

## Docker
l'application a besoin de **Docker** et **Docker Compose** pour pouvoir être lancé, peu importe votre
système d'exploitation. Attention, il faudra la **Docker Compose v1.29.2** pour que l'application soit
sûr de fonctionner.

# Utilisation

**Veulliez patienter 5 minutes environ par précaution le temps que tous les composants se mettent en place.**

Pour lancer l'application, veuillez suivre les indications suivantes :

1. Créer une instance de *Terminal | Command Prompt | Power Shell* au sein du dossier du projet 
2. Exécuter la commande suivante
```shell
docker-compose up
```
3. Patienter 2-5 minutes jusqu'à ce que les *containers* suivants soient stoppés :
    - **gateway-setup**
    - **gateway-prep**
4. Se rendre sur [localhost:3000](http://localhost:3000) ou [0.0.0.0:3000](http://0.0.0.0:3000) pour utiliser l'application.
"# Application_Full_Stack_Data" 
"# Application_Full_Stack_Data" 
"# Application_Full_Stack_Data" 
"# Application_Full_Stack_Data" 
"# Application_Full_Stack_Data" 
"# Application_Full_Stack_Data" 
