# Modèle prédictif de débordements des égouts sur l’île de Montréal 

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="autres\Capture.PNG" alt="Logo" width="350" height="200">
  </a>


<!-- TABLE DES MATIÈRES -->
<details div align="left">
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#synopsis">Synopsis</a>
    <li>
      <a href="#outils">Outils</a>
      </ul>
    <li>
      <a href="#pour commencer">Pour commencer</a>
      <ul>
        <li><a href="#Prérequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#exemple">Exemple</a></li>
      </ul>
    </li>
    <li><a href="#usage complémentaire">Usage complémentaire</a></li>
    <li><a href="#coordonnées">Coordonnées</a></li>
    <li><a href="#bibliographie">Bibliographie</a></li>
  </ol>
</details>

<!-- SYNOPSIS -->
## Synopsis

Dans le cadre de ce projet, je m’intéresse au problème de débordements des eaux usées sur l'île de Montréal. Plusieurs substances chimiques et organiques se trouvent dans les eaux des égouts. Ces eaux sont traitées dans les usines d’épurations pour éliminer les substances toxiques et renvoyer de l’eau propre dans nos rivières. En temps normal, le système d’égout est capable de gérer les débits d’eau importants et a une capacité suffisante pour répondre à la demande. Cependant, lorsque le débit est élevé, comme en temps de pluies exceptionnelles, cela ne suffit pas et des surversements peuvent se produire lors desquels l’eau non traitée est rejetée dans les rivières, ce qui affecte grandement l’écosystème.

Mon objectif dans ce projet est de construire un modèle prédictif pour la Ville de Montréal afin de prévenir les surversements d’eaux usées sur l’île de Montréal. Plus précisément, je me concentre sur les évènements pluvieux de l’année 2020, c’est-à-dire du mois de mai à octobre inclusivement.

*Note : J'ai apporté plusieurs amélioration à mon projet. Le notebook présent dans le repo correspond à la première version de celui-ci. Toujours pertinent, il précise la démarche complète du projet.



## Outils

<a href="https://www.python.org/"><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python" style="width:75px;height:35px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://pytorch.org/"><img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="PyTorch" style="width:75px;height:35px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.pytorchlightning.ai/index.html"><img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/PyTorch_Lightning_Logo.png" alt="PyTorch" style="width:75px;height:35px;"></a>



<div align="center">

## Pour commencer

<div align="left">

### Prérequis

* Anaconda

### Installation

Créez un environnement virtuel
```
conda create --name MDD python=3.9
```
Activez l'environnement virtuel
```
- conda activate MDD
```
Installez les packages
```
 - pip install -r requirements.txt
```
Si cela ne fonctionne pas, essayez cette étape :

  1. Allez dans la barre de menu et cliquez sur le terminal. Entrez : 
  ```
  conda init
  ```
  2. Fermez ce terminal et ouvrez un nouveau
  3. Dans la nouvelle fenêtre le terminal, entrez :
  ```
   conda info --envs
  ```
  4. L'environnement virtuel conda devrait être présent dans la liste. Entrez :
 ```
 conda activate name_of_venv
 ```



<div align="center">

## Exemple

<div align="left">

L'execution du script « main.py » permet le déroulement de plusieurs étapes du projet. Au choix, le script « parameters.py » permet d'activer ou désactiver certaines étapes. De plus, il permet le choix des paramètres utilisés pour le modèle. 

  1. Le dossier « data » execute le preprocessing des données -->
  - > « data_preprocessing_outputs »
  2. Le dossier « lstm » execute l'entrainement, l'inférence et l'évaluation du modèle  -->
  - > « model_outputs », « inference_outputs », « metrics_outputs » 
  3. Le dossier « map » execute la visualisation de la carte géographique -->
  - > « map_outputs »
  4. Le dossier « sweep » permet l'optimisation des hyperparamètres si souhaité -->
  - > Mettre à « True » dans le script « parameters.py »

*Note : Chaque dossier « data, lstm, map, sweep » sont indépendants ainsi, il est possible d'executer chacun individuellement.

```
python main.py
```


<div align="center">

## Usage complémentaire

<div align="left">

Utilisation de tensorboard pour visualiser la courbe d'entrainement :

  ```
  tensorboard dev upload --logdir ./lightning_logs
  ```
Première utilisation, veuillez suivre ces étapes dans le terminal :

  ```
  tensorboard dev upload --logdir ./lightning_logs
  ```
  
  - Choisissez "Oui" (pour la première connexion)

  - Connectez-vous à votre compte Gmail

  - Prenez le lien suggéré après



<div align="center">

## Coordonnées

<div align="left">

Christopher-Junior Paul - https://www.linkedin.com/in/christopher-junior-paul-565a3217a/

Lien du projet: https://github.com/cjupaul/Modele-predictif-de-debordements-des-egouts-sur-l-Ile-de-Montreal



<div align="center">

## Bibliographie

<div align="left">

Climate Data Canada. *STATION DATA* [Base de données] Récupéré de https://climatedata.ca/download/#station-download

Udemy. (2020) Le Deep Learning de A à Z. Récupéré de https://www.udemy.com/course/le-deep-learning-de-a-a-z/?fbclid=IwAR1Oj14E_C8xyFab5YDxVMGJ4ONdvKzXZeFhjR4cQG42tY8O4-yxIxyc_D4

Rapport de données horaires pour le 15 mai 2022. Gouvernement du Canada. Récupéré de https://climat.meteo.gc.ca/climate_data/hourly_data_f.html?hlyRange=2008-01-08%7C2022-05-15&dlyRange=2002-12-23%7C2022-05-15&mlyRange=%7C&StationID=30165&Prov=QC&urlExtension=_f.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2022&selRowPerPage=25&Line=17&searchMethod=contains&Month=5&Day=15&txtStationName=Montreal&timeframe=1&Year=2022

Débordements d'égouts. Kaggle. Récupéré de https://www.kaggle.com/competitions/surverses/overview

Données ouvertes, Montréal. (2016-). *Ouvrages de surverse* [Base de données] Récupéré de https://donnees.montreal.ca/ville-de-montreal/ouvrage-surverse

Données ouvertes, Montréal. (2016-). *Débordements* [Base de données] Récupéré de https://donnees.montreal.ca/ville-de-montreal/debordement

Venelin Valkov. « Multivariate Time Series Classification Tutorial with LSTM in PyTorch, PyTorch Lightning and Python » YouTube. 6 avril 2021. https://www.youtube.com/watch?v=PCgrgHgy26c&t=275s

Sequence Classification Using Deep Learning. Récupéré de https://www.mathworks.com/help/deeplearning/ug/classify-sequence-data-using-lstm-networks.html

Understanding of LSTM Networks. Récupéré de https://www.geeksforgeeks.org/understanding-of-lstm-networks/

Venelin Valkov. « Multivariate Time Series Forecasting with LSTM using PyTorch and PyTorch Lightning (ML Tutorial) » YouTube. 30 mars 2021. https://www.youtube.com/watch?v=ODEGJ_kh2aA&t=1098s

Venelin Valkov. « Multivariate Time Series Data Preprocessing with Pandas in Python | Machine Learning Tutorial » YouTube. 20 mars 2021. https://www.youtube.com/watch?v=jR0phoeXjrc&t=1050s

How to use TensorBoard with PyTorch. Récupéré de https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-use-tensorboard-with-pytorch.md

DATASETS & DATALOADERS. Récupéré de https://pytorch.org/tutorials/beginner/basics/data_tutorial.html

TORCH.UTILS.DATA. Récupéré de phttps://pytorch.org/docs/stable/data.html

