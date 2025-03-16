import random

'''
You are required to optimize the function:

f(x) = 2x² - 1, where x is within the range [0, 31].
Each individual in the population should be represented as a 6-bit binary string (since 2^6 = 64).
The algorithm should:
1. Generate an initial random population of binary-encoded values
2. Evaluate the fitness of each individual using f(x).
3. Select parents using tournament selection to ensure diversity.
4. Perform uniform crossover instead of single-point crossover for variation.
5. Apply a mutation operator with adaptive probability to avoid local optima.
6. Run for a fixed number of generations and return the best solution found.
'''

# Step 1: Configuration
population_size = 20
mutation_rate = 0.1
max_generations = 50
chromosome_length = 6  # 6-bit binary strings for values 0-31

# Step 2: Fitness
def fitness(x):
    return (2 * (x ** 2) - 1)

# Step 3: Binary Conversion Functions
def binary_to_decimal(binary_string):
    return int(binary_string, 2)  # The second argument (2) tells Python that the given string is in base-2 (binary).

def decimal_to_binary(decimal_val):
    return format(decimal_val, '06b')  # 6-bit binary format
    # The format() function converts the given decimal number into a binary string.
    # The format specifier '06b' does two things:
        # 'b' → Converts the number to binary.
        # '06' → Ensures the result is 6 bits long by adding leading zeros if needed.

# Step 4: Initial Population
def initialize_population(population_size):
    return [decimal_to_binary(random.randint(0, 31)) for _ in range(population_size)]

# Step 5: Selection (Tournament Selection)
def select_parents(population, fitness_scores):
    selected_parents = []
    for _ in range(len(population) // 2):  # Select half the population
        # Randomly pick 3 individuals for the tournament
        tournament = random.sample(list(zip(population, fitness_scores)), 3)
        # Select the best individual from the tournament
        winner = max(tournament, key=lambda x: x[1])  # Maximizing fitness function
        selected_parents.append(winner[0])  # Append only the individual's binary string
    return selected_parents

# Step 6: Crossover (Uniform Crossover)
def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):# Since both parents are the same length, iterating through len(parent1) is enough.
        if random.random() < 0.5:  # Creates a 50% chance condition.
            child.append(parent1[i])
        else:  # Step 4: Remaining 50% chance to pick gene from parent2
            child.append(parent2[i])
    return ''.join(child)

# Step 7: Mutation (Adaptive Mutation)
def mutate(individual, mutation_rate):
    mutated_individual = []
    for bit in individual:
        if random.random() < mutation_rate:  # Step 1: Check mutation condition
            mutated_individual.append('1' if bit == '0' else '0')  # Step 2: Flip the bit
        else:
            mutated_individual.append(bit)  # Step 3: Keep the bit unchanged
    return ''.join(mutated_individual)  # Step 4: Join the list back into a string

# STEP 8: Genetic Algorithm Loop
def GA():
    # Step 8.1: Initialize Population
    population = initialize_population(population_size)

    # Step 8.2: Evolution Process
    for generation in range(max_generations):
        # Step 8.2.1: Evaluate Fitness for Each Individual
        fitness_scores = [fitness(binary_to_decimal(individual)) for individual in population]

        # Step 8.2.2: Identify the Best Fitness
        best_fitness = max(fitness_scores)
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

        # Step 8.3: Selection - Pick the top 50% as parents
        parents = select_parents(population, fitness_scores)
        parents = parents * 2  # Ensure sufficient parents for crossover

        # Step 8.4: Create New Population via Crossover and Mutation
        new_population = []
        while len(new_population) < population_size:
            # Step 8.4.1: Select Two Random Parents
            parent1, parent2 = random.sample(parents, 2)
            # Step 8.4.2: Perform Crossover
            child = crossover(parent1, parent2)
            # Step 8.4.3: Perform Mutation
            child = mutate(child, mutation_rate)
            # Step 8.4.4: Add New Child to Population
            new_population.append(child)

        # Step 8.5: Update Population for Next Generation
        population = new_population

    # Step 8.6: Identify and Display the Best Solution Found
    fitness_scores = [fitness(binary_to_decimal(individual)) for individual in population]
    best_fitness = max(fitness_scores)
    best_solution = population[fitness_scores.index(best_fitness)]
    print("\nBest Solution:", best_solution)
    print("Best Fitness Value:", best_fitness)

# Run the Genetic Algorithm
GA()
