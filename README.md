# rank-api

## Description

Ce projet utilise FastAPI pour créer une API simple avec un point de terminaison de vérification de l'état.

## Structure du projet

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/cayel/rank-api.git
    cd rank-api
    ```

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

Pour lancer l'API en local, exécutez la commande suivante :
```sh
uvicorn api.main:app --reload