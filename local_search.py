#! /usr/bin/env python

import math
import random
import sys
import numpy as np

################### slightly modified code from the book ####################
def exp_schedule(k=20, lam=0.005, limit=1000):
    "One possible schedule function for simulated annealing"
    return lambda t: k * math.exp(-lam * t) if t < limit else 0

def probability(p):
    "Return true with probability p."
    return p > random.uniform(0.0, 1.0)

def argmin(seq, fn):
    "Return an element with lowest fn(seq[i]) score; tie goes to first one."
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def expand(self, problem):
        "Return a list of nodes reachable from this node."
        return [Node(next_state, self, act,
                     problem.path_cost(self.path_cost, self.state, act, next_state))
                for (act, next_state) in problem.successor(self.state)]

    def value(self):
        return self.state.value()

def simulated_annealing(problem, schedule, max_steps):
    current = problem.initial()
    for t in range(max_steps):
        T = schedule(t)
        if T == 0:
            return current
        next_state = problem.random_neighbor(current)
        delta_e = problem.value(next_state) - problem.value(current)
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / T):
            current = next_state
    return current

def simulated_annealing_with_restarts(problem, schedule, max_steps, max_restarts):
    best_global = None
    restarts = 0
    while restarts < max_restarts:
        best = simulated_annealing(problem, schedule, max_steps)
        if best_global is None or problem.value(best) < problem.value(best_global):
            best_global = best
        restarts += 1
    return best_global, problem.value(best_global)

def hill_climbing(problem):
    current = Node(problem.initial_solution())
    while True:
        neighbors = current.expand(problem)
        neighbor = argmin(neighbors, lambda node: problem.value(node.state))
        if problem.value(neighbor.state) >= problem.value(current.state):
            return current.state
        current = neighbor

class TSP:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)

    def initial(self):
        # Retourne une solution initiale (par exemple, une tournée aléatoire)
        return list(np.random.permutation(self.num_cities))

    def random_neighbor(self, current):
        # Retourne un voisin aléatoire de la solution actuelle
        neighbor = current[:]
        i, j = np.random.choice(self.num_cities, 2, replace=False)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def value(self, state):
        # Calcule la longueur totale de la tournée
        total_distance = 0
        for i in range(self.num_cities):
            city1 = self.cities[state[i]]
            city2 = self.cities[state[(i + 1) % self.num_cities]]
            total_distance += np.linalg.norm(np.array(city1) - np.array(city2))
        return total_distance

    def calculate_distance_matrix(self):
        matrix = np.zeros((self.num_cities, self.num_cities))
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    matrix[i, j] = np.linalg.norm(np.array(self.cities[i]) - np.array(self.cities[j]))
        return matrix

    def tour_length(self, tour):
        if len(tour) != self.num_cities:
            raise ValueError(f"Tour length ({len(tour)}) does not match the number of cities ({self.num_cities}).")
        print(f"Calculating tour length for tour: {tour}")
        length = sum(self.distance_matrix[tour[i], tour[i + 1]] for i in range(self.num_cities - 1))
        length += self.distance_matrix[tour[-1], tour[0]]
        print(f"Tour length: {length}")
        return length

    def get_neighbors(self, tour):
        neighbors = []
        for i in range(1, self.num_cities - 1):
            for j in range(i + 1, self.num_cities):
                neighbor = tour[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def initial_solution(self):
        return list(range(self.num_cities))

    def successor(self, tour):
        successors = []
        for i in range(1, self.num_cities - 1):
            for j in range(i + 1, self.num_cities):
                neighbor = tour[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                successors.append((f"swap({i}, {j})", neighbor))
        return successors


#Stratégies de recherhes locales 
# Stratégie aléatoire
def random_search(problem, steps):
    current = problem.initial_solution()
    best = current
    for _ in range(steps):
        neighbors = problem.get_neighbors(current)
        if neighbors:
            current = random.choice(neighbors)
            if problem.value(current) < problem.value(best):
                best = current
    return best, problem.value(best)

# Stratégie onlyBest
def only_best_search(problem, steps):
    current = problem.initial_solution()
    best = current
    for _ in range(steps):
        neighbors = problem.get_neighbors(current)
        if neighbors:
            neighbors.sort(key=lambda tour: problem.value(tour))
            current = neighbors[0]
            if problem.value(current) < problem.value(best):
                best = current
    return best, problem.value(best)

# Stratégie randomBest
def random_best_search(problem, steps):
    current = problem.initial_solution()
    best = current
    for _ in range(steps):
        neighbors = problem.get_neighbors(current)
        if neighbors:
            neighbors.sort(key=lambda tour: problem.value(tour))
            current = random.choice(neighbors[:5])
            if problem.value(current) < problem.value(best):
                best = current
    return best, problem.value(best)

# Recherche taboue
def tabu_search(problem, steps, tabu_length):
    current = problem.initial_solution()
    best = current
    tabu_list = []
    for _ in range(steps):
        neighbors = problem.get_neighbors(current)
        if neighbors:
            neighbors.sort(key=lambda tour: problem.value(tour))
            best_neighbor = None
            for neighbor in neighbors:
                if neighbor not in tabu_list:
                    best_neighbor = neighbor
                    break
            if best_neighbor:
                current = best_neighbor
                tabu_list.append(current)
                if len(tabu_list) > tabu_length:
                    tabu_list.pop(0)
                if problem.value(current) < problem.value(best):
                    best = current
    return best, problem.value(best)

# Recherche taboue avec redémarrages
def tabu_search_with_restarts(problem, steps, tabu_length, max_restarts):
    best_global = None
    restarts = 0
    while restarts < max_restarts:
        best, best_value = tabu_search(problem, steps, tabu_length)
        if best_global is None or best_value < problem.value(best_global):
            best_global = best
        restarts += 1
    return best_global, problem.value(best_global)
