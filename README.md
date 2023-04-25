Introduction du projet

Dans le cadre de ce projet, je m’intéresse au problème de surversement des eaux usées sur l'île de Montréal. Plusieurs substances chimiques et organiques se trouvent dans les eaux des égouts. Ces eaux sont traitées dans les usines d’épurations pour éliminer les substances toxiques et renvoyer de l’eau propre dans nos rivières. En temps normal, le système d’égout est capable de gérer les débits d’eau importants et a une capacité suffisante pour répondre à la demande. Cependant, lorsque le débit est élevé, comme en temps de pluies exceptionnelles, cela ne suffit pas et des surversements peuvent survenir où de l’eau non traitée est rejetée dans les rivières et cela affecte grandement l’écosystème.

Mon objectif dans ce projet est de construire un modèle prédictif pour la Ville de Montréal afin de prévenir la survenance des surversements d’eaux usées sur l’île de Montréal. Je me concentre davantage sur les évènements pluvieux de l’année c’est-à-dire les mois de mai à octobre inclusivement.

Installer Anaconda

- https://www.anaconda.com/download

Créer un environnement virtuel

- conda create --name MDD python=3.9

Activation de l'environnement virtuel

- conda activate MDD

Installation des packages

 - pip install -r requirements.txt

Si cela ne fonctionne pas, essayez cette étape :

    1- Allez dans la barre de menu et cliquez sur Terminal.
    2- Tapez : conda init
    3- Fermez ce terminal et ouvrez-en un nouveau
    4- Dans la nouvelle fenêtre de terminal, tapez conda info --envs
    5- (Votre environnement virtuel conda devrait être présent dans la liste)
    6- Tapez conda activate name_of_venv

Utilisation de tensorboard pour visualiser la courbe d'entrainement:

Ligne de commande a executer après l'entrainement du modèle:

    1- tensorboard dev upload --logdir ./lightning_logs

    2- Oui (pour la première connexion)

    3- Connectez-vous à votre compte Gmail

    4- Prenez le lien suggéré après