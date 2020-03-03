# Lieux et horaires des collectes de don du sang (EFS)
Le script récupère les données via le point d'entrée AJAX utilisé par la carte et le moteur de recherche présent sur le site de l'EFS : https://dondesang.efs.sante.fr/trouver-une-collecte

Son principal intérêt est d'automatiser la sauvegarde des données téléchargées vers https://www.data.gouv.fr/fr/datasets/don-du-sang-lieux-et-horaires-des-collectes/ régulièrement.

Pour cela, il faut une clef API de data.gouv.fr (qui est secrète). Le mode d'emploi est :

* créer un fichier `params.py`au même niveau que le code `main.py`
* dans ce fichier, saisir la clef au format `X_API_KEY = "ma_clef_api"`

Configurer ensuite son serveur pour exécuter le script périodiquement.

## Installation

Sur Ubuntu 18.04, Python3 et Git sont déjà installés.

```shell
sudo apt-get update
sudo apt-get upgrade
cd /srv
git clone https://github.com/lou-dupont/EFS.git
```

Créer le fichier de paramètres, puis lancer avec

```shell
python3 main.py
```

Pour une exécution toutes les heures, ajouter la ligne suivante au fichier `/etc/crontab` 
```
0 * * * * python3 /srv/EFS/main.py >/dev/null 2>&1
```
