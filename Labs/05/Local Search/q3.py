import random

# STEP 1: Configuration
num_cities = 10
population_size = 100
mutation_rate = 0.1
max_generations = 1000

# STEP 2: Create a Distance Matrix
def create_distance_matrix(num_cities):
    matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(10, 100)
            matrix[i][j] = distance
            matrix[j][i] = distance  # Symmetric property
    return matrix 

# STEP 3: Initialize Population
def initialize_population(population_size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(population_size)]

# STEP 4: Fitness Function (Lower is Better)
def evaluate_fitness(route, distance_matrix):
    return sum(distance_matrix[a][b] for a, b in zip(route, route[1:] + [route[0]]))

# STEP 5: Selection (Top 50%)
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    return sorted_population[:len(population) // 2]

# STEP 6: Crossover (Single-point crossover)
def crossover(parent1, parent2):
    point = random.randint(0, num_cities - 1)
    child = parent1[:point] + [city for city in parent2 if city not in parent1[:point]]
    return child

# STEP 7: Mutation (Swap 2 Cities)
def mutate(route, mutation_rate=0.3):
    if random.random() < mutation_rate:
        city1, city2 = random.sample(range(num_cities), 2)
        route[city1], route[city2] = route[city2], route[city1]
    return route    

# STEP 8: Genetic Algorithm Loop
def GA():
    # Step 8.1: Create Distance Matrix & Generate Population
    distance_matrix = create_distance_matrix(num_cities)
    population = initialize_population(population_size, num_cities)
    
    # Step 8.2: Evolution Process
    for generation in range(max_generations):
        fitness_scores = [evaluate_fitness(route, distance_matrix) for route in population]
        best_fitness = min(fitness_scores)
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
        
        # Step 8.3: Selection - Pick the top 50% as parents
        parents = select_parents(population, fitness_scores)
        
        # Step 8.4: Create New Population via Crossover and Mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        # Update the population for the next generation
        population = new_population
    
    # Step 8.5: Identify and Display the Best Route
    fitness_scores = [evaluate_fitness(route, distance_matrix) for route in population]
    best_fitness = min(fitness_scores)
    best_route = population[fitness_scores.index(best_fitness)]
    print("\nBest Route:", best_route)
    print("Total Distance:", best_fitness)

# Run the Genetic Algorithm
GA()
