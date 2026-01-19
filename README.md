# Demo App Python

Une application simple pour démontrer la conteneurisation.

## Lancement avec Docker (Recommandé)

1. Construire l'image :
   docker build -t python-demo .

2. Lancer le conteneur :
   docker run -p 5000:5000 python-demo

3. Accéder à l'application :
   http://localhost:5000