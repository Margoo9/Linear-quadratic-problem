import matplotlib.pyplot as plt
import numpy as np
import random


class Algorithm:
    def __init__(self, population_size, generations_num):
        self.population_size = population_size
        self.generations_num = generations_num
        self.epsilon = norm.rvs(loc=0, scale=1, size=(1, self.population_size))[0]

    def generate_population(curr_population):
    new_population_mutated = []
    for individual in curr_population:
        new_individual = []
        for feature in individual:
            if random.random() > e:
                new_individual.append(feature)
            else:
                # biallelic coding
                new_individual.append(int(not feature))
        new_population_mutated.append(new_individual)

    new_population_mutated = np.array(new_population_mutated)
    whole_population = np.concatenate((curr_population, new_population_mutated))
    fitness_array = fitness_function(whole_population)

    population_fitness_array = zip(whole_population, fitness_array)
    population_fitness_array = sorted(population_fitness_array, key=lambda array: array[1])
    new_population = [item[0] for item in population_fitness_array[:len(population_fitness_array)//2]]
    new_population = np.array(new_population)
    return new_population


    def fitness_function(population):
    fitness_array = []
    for individual in population:
        u = []
        allel_array = []
        x = x_0
        sum = 0
        individual = individual * bit_values
        for i in range(N):
            allel_array.append(individual[i*20:i*20+20])
            u.append(np.sum(allel_array[i]))
        for j in range(N-1):
            sum += x ** 2 + u[j] ** 2
            x += u[j]

        J = x ** 2 + sum
        fitness_array.append(J)
    best_individuals.append(min(fitness_array))
    return fitness_array


e = 0.15  # mutation factor
population_size = 70  
iterations = 1000  
N = 45  
x_0 = 100  # initial state
best_individuals = []
bit_values = []

algo = Algorithm(population_size, iterations)

for i in range(20 * N):
    bit_values.append(random.uniform(-10, 10))
print("Values to decode: ", bit_values)

# Initial population
current_population = np.random.randint(0, 2, (population_size, 20*N))

for i in range(iterations):
    current_population = generate_population(current_population)

print("Best individual: ", current_population[0])
print("Best individual's fitness function: ", min(best_individuals))
plt.plot(best_individuals)
plt.title(f"Best individual's fitness function for N = {N}")
plt.xlabel("Iterations number")
plt.ylabel("Fitness")
plt.show()

