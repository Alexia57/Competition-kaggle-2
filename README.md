# Projet Kaggle - Classification d'Images

### Auteurs
Alexia Prevot et Tanias Mendes Dias

## Introduction
Ce projet vise à résoudre la tâche de classification d'images dans le cadre de la compétition Kaggle. Nous avons implémenté plusieurs modèles, dont un classificateur de forêts aléatoires, un réseau de neurones convolutif (CNN), ainsi que d'autres modèles tels que Adaboost et XGBoost.

## Contenu du Projet
- Analyse des Données (analyse_donnees.ipynb): Ce notebook contient l'analyse initiale des données effectuée au début de la compétition pour obtenir une vue d'ensemble du problème.

- Random Forest From Scratch (rd_forest_1.ipynb, rd_forest_2.ipynb): Ces fichiers présentent notre implémentation de l'algorithme Random Forest à partir de zéro, avec différentes itérations et tests.

- Random Forest avec scikit-learn (rd_forest_sklearn.ipynb): Ce fichier utilise la bibliothèque scikit-learn pour implémenter le classificateur de forêts aléatoires.

- CNN (model_cnn.ipynb): Ce notebook présente notre implémentation d'un réseau de neurones convolutif (CNN) pour la classification d'images.

- XGBoost (xgboost.ipynb): Ce fichier contient l'implémentation et les tests du modèle XGBoost.

- Adaboost (adaboost.ipynb): Ce notebook contient l'implémentation et les tests du modèle Adaboost.

- Soumission des Résultats (submit_result.py): Ce fichier contient des fonctions qui ont été utilisées pour créer la soumission finale dans le bon format requis pour la compétition Kaggle.

- Tests Supplémentaires (tests.ipynb): Ce notebook contient d'autres tests qui ont été réalisés ou des idées qui n'ont pas abouti.

## Instructions d'Exécution
Pour exécuter le code, veuillez suivre ces étapes :

- Téléchargez les données de la compétition Kaggle dans un dossier data/.
- Ouvrez chaque fichier notebook dans Jupyter Notebook ou un autre environnement compatible.
- Exécutez les cellules de code une par une dans l'ordre chronologique.
- Assurez-vous d'avoir les dépendances nécessaires installées, telles que numpy, pandas, scikit-learn, etc.
- Certains notebooks peuvent avoir des sections spécifiques pour l'entraînement des modèles, veuillez suivre les instructions à l'intérieur de chaque notebook.
