<div align="center">
<!-- TABLE DES MATIÈRES -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#synopsis">Synopsis</a>
    <li>
      <a href="#built-with">Built-with</a>
      </ul>
    <li>
      <a href="#pour commencer">Pour commencer</a>
      <ul>
        <li><a href="#Pré-requis">Pré-requis</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#démarrage">Démarrage</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#coordonnées">Coordonnées</a></li>
    <li><a href="#remerciements">Remerciements</a></li>
  </ol>
</details>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="./Capture.PNG" alt="Logo" width="350" height="200">
  </a>

<!-- SYNOPSIS -->
## Synopsis

Dans le cadre de ce projet, je m’intéresse au problème de surversement des eaux usées sur l'île de Montréal. Plusieurs substances chimiques et organiques se trouvent dans les eaux des égouts. Ces eaux sont traitées dans les usines d’épurations pour éliminer les substances toxiques et renvoyer de l’eau propre dans nos rivières. En temps normal, le système d’égout est capable de gérer les débits d’eau importants et a une capacité suffisante pour répondre à la demande. Cependant, lorsque le débit est élevé, comme en temps de pluies exceptionnelles, cela ne suffit pas et des surversements peuvent survenir où de l’eau non traitée est rejetée dans les rivières et cela affecte grandement l’écosystème.

Mon objectif dans ce projet est de construire un modèle prédictif pour la Ville de Montréal afin de prévenir la survenance des surversements d’eaux usées sur l’île de Montréal. Je me concentre davantage sur les évènements pluvieux de l’année c’est-à-dire les mois de mai à octobre inclusivement.

Note***: Le Notebook "Modelisation_de_debordement_notebook" est l'ancienne version de mon projet. La nouvelle version est maintenant sans notebook et contient des améliorations dans le code. Cependant, pour plus de détails concernant les étapes du projet, le notebook reste pertinent. C'est pour cette raison il est inséré dans la nouvelle version du projet.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* <a href="https://pytorch.org/"><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="PyTorch" style="width:100px;height:50px;"></a>

* <a href="https://pytorch.org/"><img src="https://pytorch.org/assets/images/pytorch-logo.png" alt="PyTorch" style="width:100px;height:50px;"></a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center">

## Pour commencer

<div align="left">

### Pré-requis

* Anaconda

### Installation

Créer un environnement virtuel
```
conda create --name MDD python=3.9
```
Activation de l'environnement virtuel
```
- conda activate MDD
```
Installation des packages
```
 - pip install -r requirements.txt
```
Si cela ne fonctionne pas, essayez cette étape :

  1. Allez dans la barre de menu et cliquez sur Terminal.
  2. Entrer: 
  ```
  conda init
  ```
  3. Fermez ce terminal et ouvrez-en un nouveau
  4. Dans la nouvelle fenêtre de terminal, tapez:
  ```
   conda info --envs
  ```
  5. L'environnement virtuel conda devrait être présent dans la liste
Entrer:
 ```
 conda activate name_of_venv
 ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<div align="center">

## Usage

<div align="left">
Utilisation de tensorboard pour visualiser la courbe d'entrainement:

  ```
  tensorboard dev upload --logdir ./lightning_logs
  ```
Première utilisation, veuillez suivre ces étapes dans le terminal :

  ```
  tensorboard dev upload --logdir ./lightning_logs
  ```
  
  - Choisir "Oui" (pour la première connexion)

  - Connectez-vous à votre compte Gmail

  - Prenez le lien suggéré après

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center">

## Coordonnées

<div align="left">

Christopher-Junior Paul - www.linkedin.com/in christopher-junior-paul-565a3217a

Lien du projet: https://github.com/cjupaul/Modele-predictif-de-debordements-des-egouts-sur-l-Ile-de-Montreal

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python-url]: https://www.python.org/  



