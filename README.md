# Artificial Intelligence - Assignment 4: Local Search

## Context

This assignment focuses on applying different local search strategies to solve the traveling salesman problem (TSP). The TSP consists of finding the shortest possible path that visits a given set of cities and returns to the starting city. The cities are represented by 2D coordinates, and the distance between two cities is calculated as the Euclidean distance.

## Objectives

The objective of this assignment is to:
1. Implement the traveling salesman problem as a local search problem.
2. Implement and compare different local search strategies:
- Random search
- "onlyBest" search
- "randomBest" search
- Tabu search
- Tabu search with restarts
- Simulated annealing with restarts
3. Analyze and compare the results obtained by each strategy.

## Project Structure

The project is structured as follows:
- `local_search.py`: Contains the implementations of the different local search strategies.
- `test_local_search.py`: Test script to run the different strategies on a TSP instance and display the results.
- `inst0x_xx.tsp`: Files containing the coordinates of the cities for a TSP instance.

## Configuration

### Prerequisites

- Python 3.x
- Python Libraries: `numpy`, `matplotlib`

To install the necessary libraries, use the following command:

```sh
pip install numpy matplotlib
```

### File Structure

- `local_search.py`: Contains the `TSP` class and the local search functions.
- `test_local_search.py`: Test script to run the different local search strategies.
- `inst04_48.tsp` : TSP instance file containing city coordinates.

## Execution

To run the project, follow these steps:

1. **Run the test script** :
- Open a terminal or command prompt.
- Navigate to the directory containing the project files.
- Run the test script:

```sh
python test_local_search.py
```

## Results

The test script `test_local_search.py` displays the results for each local search strategy:
- **Length of the best tour found** : Displayed in the console.
- **Tour graph** : Displayed in a graph window using `matplotlib`.

### Example Output

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

## Interpreting Results

- **Tour Length**: The shorter the tour length, the better the solution. Compare the lengths displayed for each strategy to determine which one found the best solution.
- **Graphs**: Graphs allow you to visualize the tours found. This can help you understand how each strategy explores the search space and identify patterns or potential problems.

## Authors

- ATTOH James
- BIAOU Marius
- HOUESSOU Kenny
- YACOUBOU Masmoud
