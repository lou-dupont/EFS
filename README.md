# Lieux et horaires des collectes de don du sang (EFS)

Le script récupère les données via l'API https://api.efs.sante.fr/carto-api/swagger/ mise à disposition par l'EFS.

Son principal intérêt est d'automatiser la sauvegarde des données téléchargées vers https://www.data.gouv.fr/fr/datasets/don-du-sang-lieux-et-horaires-des-collectes/ régulièrement afin de les rendre accessibles à un public non informaticien, et même en cas d'indisponibilité du serveur de l'EFS.

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

Installation du module **pandas** (pour faciliter la génération du fichier Excel).

```bash
sudo apt-get install python3-pip
sudo pip3 install pandas
sudo pip3 install openpyxl
```

Créer le fichier de paramètres, puis lancer avec

```shell
python3 main.py
```

Pour une exécution toutes les heures, ajouter la ligne suivante au fichier `/etc/crontab` 
```
01 *    * * *   root    python3 /srv/EFS/main.py >/dev/null 2>&1
```
