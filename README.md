# Lieux et horaires des collectes de don du sang (EFS)
Le script récupère les données via le point d'entrée AJAX utilisé par la carte et le moteur de recherche présent sur le site de l'EFS : https://dondesang.efs.sante.fr/trouver-une-collecte

Son principal intérêt est d'automatiser la sauvegarde des données téléchargées vers https://www.data.gouv.fr/fr/datasets/don-du-sang-lieux-et-horaires-des-collectes/ régulièrement.

Pour cela, il faut une clef API de data.gouv.fr (qui est secrète). Le mode d'emploi est :

* créer un fichier `params.py`au même niveau que le code `main.py`
* dans ce fichier, saisir la clef au format `X_API_KEY = "ma_clef_api"`

Configurer ensuite son serveur pour exécuter le script périodiquement.