# Backend de weSplit

Ceci est le service backend de l'application **weSplit**. Il fournit des API et gère la logique métier pour le partage des dépenses entre utilisateurs.

## Fonctionnalités

- Authentification et gestion des utilisateurs
- Création et suivi des dépenses
- Répartition des dépenses entre les membres d'un groupe

## Technologies utilisées

- **Langage de programmation** : Python
- **Framework** : Django
- **Base de données** : SQLite (par défaut, peut être configurée pour MySQL ou PostgreSQL)

## Prise en main

### Prérequis

- Python 3.9 ou supérieur
- SQLite (par défaut) ou MySQL/PostgreSQL si configuré
- Docker (optionnel, pour un déploiement conteneurisé)

### Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/anas325/backend.git
    cd backend
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :
    Créez un fichier `.env` à la racine du projet et configurez les éléments suivants :
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3  # Par défaut, utilisez SQLite
    ```

5. Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

6. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

### Exécution avec Docker

1. Construisez l'image Docker :
    ```bash
    docker build -t wesplit-backend .
    ```

2. Exécutez le conteneur :
    ```bash
    docker run -p 8000:8000 --env-file .env wesplit-backend
    ```

## Contribution

Les contributions sont les bienvenues ! Veuillez forker le dépôt et soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.