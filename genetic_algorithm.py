from random import random, randint, choice


def fitness(chromosome, goal):
    # Example: Simple fitness function calculating inverse of path length if goal reached
    if chromosome[-1] == goal:
        return 1 / len(chromosome)  # Higher fitness for shorter paths
    else:
        return 0  # No fitness if goal not reached

def crossover(parent1, parent2):
    # Simple one-point crossover
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(G, chromosome, mutation_rate=0.1):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            # Simple mutation: replace one node with a neighbor
            neighbors = list(G.neighbors(chromosome[i]))
            if neighbors:
                chromosome[i] = random.choice(neighbors)
    return chromosome


def random_walk(graph, start, steps=100):
    path = [start]
    current = start
    for _ in range(steps):
        neighbors = list(graph.neighbors(current))
        if not neighbors:
            break
        current = choice(neighbors)
        path.append(current)
    return path

import random

def tournament_selection(population, fitnesses, tournament_size=3):
    selected = []
    population_size = len(population)

    while len(selected) < population_size:
        # Randomly select individuals for the tournament
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        # Select the individual with the highest fitness in the tournament
        winner = max(tournament, key=lambda x: x[1])
        selected.append(winner[0])  # Append the winning individual's chromosome

    return selected



def genetic_algorithm(graph, start, goal, population_size=100, generations=100, tournament_size = 3):
    # Initialize population: random paths
    population = [random_walk(graph, start) for _ in range(population_size)]
    for gen in range(generations):
        # Evaluate fitness
        fitnesses = [fitness(individual, goal) for individual in population]
        # Selection
        selected = tournament_selection(population, fitnesses, tournament_size)
        # Crossover and mutation
        next_generation = []
        for i in range(0, len(selected), 2):
            child1, child2 = crossover(selected[i], selected[i+1])
            next_generation.extend([mutate(graph, child1), mutate(graph, child2)])
        population = next_generation
    # Choose best solution
    best_solution = max(population, key=lambda x: fitness(x, goal))
    return best_solution
