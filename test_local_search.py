import numpy as np
import matplotlib.pyplot as plt
from local_search import TSP, random_search, only_best_search, random_best_search, tabu_search, tabu_search_with_restarts, simulated_annealing_with_restarts, exp_schedule

# Fonction pour lire les instances TSP
def read_tsp_instance(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_cities = int(lines[0].strip())
        cities = []
        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) == 3:
                _, x, y = parts
                cities.append((float(x), float(y)))
        return cities

# Fonction pour tracer les résultats
def plot_tsp_solution(cities, tour):
    tour_coords = [cities[i] for i in tour]
    tour_coords.append(cities[tour[0]])  # Revenir au point de départ
    x, y = zip(*tour_coords)
    plt.plot(x, y, 'bo-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('TSP Solution')
    plt.show()

# Lire l'instance TSP
cities = read_tsp_instance('inst04_48.tsp')
tsp = TSP(cities)

# Tester les différentes stratégies
steps = 100

# Stratégie aléatoire
best_tour, best_length = random_search(tsp, steps)
print(f"Random Search: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)

# Stratégie onlyBest
best_tour, best_length = only_best_search(tsp, steps)
print(f"Only Best Search: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)

# Stratégie randomBest
best_tour, best_length = random_best_search(tsp, steps)
print(f"Random Best Search: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)

# Recherche taboue
tabu_length = 5
best_tour, best_length = tabu_search(tsp, steps, tabu_length)
print(f"Tabu Search: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)

# Recherche taboue avec redémarrages
max_restarts = 5
best_tour, best_length = tabu_search_with_restarts(tsp, steps, tabu_length, max_restarts)
print(f"Tabu Search with Restarts: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)

# Recuit simulé avec redémarrages
best_tour, best_length = simulated_annealing_with_restarts(tsp, exp_schedule(), steps, max_restarts)
print(f"Simulated Annealing with Restarts: Best tour length = {best_length}")
plot_tsp_solution(cities, best_tour)
