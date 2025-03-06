
#  Intelligence Artificielle - Devoir 4 : Recherche Locale

## Contexte

Ce devoir porte sur l'application de différentes stratégies de recherche locale pour résoudre le problème du voyageur de commerce (TSP). Le TSP consiste à trouver le plus court chemin possible qui visite un ensemble donné de villes et revient à la ville de départ. Les villes sont représentées par des coordonnées 2D, et la distance entre deux villes est calculée comme la distance euclidienne.

## Objectifs

L'objectif de ce devoir est de :
1. Implémenter le problème du voyageur de commerce comme un problème de recherche locale.
2. Mettre en œuvre et comparer différentes stratégies de recherche locale :
   - Recherche aléatoire
   - Recherche "onlyBest"
   - Recherche "randomBest"
   - Recherche taboue
   - Recherche taboue avec redémarrages
   - Recuit simulé avec redémarrages
3. Analyser et comparer les résultats obtenus par chaque stratégie.

## Structure du Projet

Le projet est structuré comme suit :
- `local_search.py` : Contient les implémentations des différentes stratégies de recherche locale.
- `test_local_search.py` : Script de test pour exécuter les différentes stratégies sur une instance TSP et afficher les résultats.
- `inst0x_xx.tsp` : Fichiers contenant les coordonnées des villes pour une instance TSP.

## Configuration

### Prérequis

- Python 3.x
- Bibliothèques Python : `numpy`, `matplotlib`

Pour installer les bibliothèques nécessaires, utilisez la commande suivante :

```sh
pip install numpy matplotlib
```

### Structure des Fichiers

- `local_search.py` : Contient la classe `TSP` et les fonctions de recherche locale.
- `test_local_search.py` : Script de test pour exécuter les différentes stratégies de recherche locale.
- `inst04_48.tsp` : Fichier d'instance TSP contenant les coordonnées des villes.

## Exécution

Pour exécuter le projet, suivez ces étapes :


1. **Exécuter le script de test** :
   - Ouvrez un terminal ou une invite de commande.
   - Naviguez jusqu'au répertoire contenant les fichiers du projet.
   - Exécutez le script de test :

     ```sh
     python test_local_search.py
     ```

## Résultats

Le script de test `test_local_search.py` affiche les résultats pour chaque stratégie de recherche locale :
- **Longueur de la meilleure tournée trouvée** : Affichée dans la console.
- **Graphique de la tournée** : Affiché dans une fenêtre graphique utilisant `matplotlib`.

### Exemple de Sortie

```
Calculating tour length for tour: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
Tour length: 1234.567
Random Search: Best tour length = 1234.567
Only Best Search: Best tour length = 1123.456
Random Best Search: Best tour length = 1098.765
Tabu Search: Best tour length = 1054.321
Tabu Search with Restarts: Best tour length = 1043.210
Simulated Annealing with Restarts: Best tour length = 1032.100
```

## Interprétation des Résultats

- **Longueur de la tournée** : Plus la longueur de la tournée est courte, meilleure est la solution. Comparez les longueurs affichées pour chaque stratégie pour déterminer laquelle a trouvé la meilleure solution.
- **Graphiques** : Les graphiques vous permettent de visualiser les tournées trouvées. Cela peut vous aider à comprendre comment chaque stratégie explore l'espace de recherche et à identifier des schémas ou des problèmes potentiels.

## Auteurs

- ATTOH James
- BIAOU Marius
- HOUESSOU Kenny
- YACOUBOU Masmoud
