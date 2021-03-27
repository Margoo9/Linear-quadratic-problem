import matplotlib.pyplot as plt
import numpy as np
import random


class Algorithm:
    def __init__(self, population_size, generations_num):
        self.e = 0.15  # mutation factor
        self.population_size = population_size
        self.iterations = generations_num
        self.N = 45
        self.x_0 = 100  # initial state
        self.best_individuals = []
        self.bit_values = []
        # Initial population
        self.current_population = np.random.randint(0, 2, (population_size, 20 * self.N))

    def generate_population(self, curr_population):
        new_population_mutated = []
        # New individuals
        for individual in curr_population:
            new_individual = []
            for feature in individual:
                if random.random() > self.e:
                    new_individual.append(feature)
                else:
                    # biallelic coding
                    new_individual.append(int(not feature))
            new_population_mutated.append(new_individual)

        new_population_mutated = np.array(new_population_mutated)
        whole_population = np.concatenate((curr_population, new_population_mutated))
        fitness_array = self.fitness_function(whole_population)

        # Selection of better individuals
        population_fitness_array = zip(whole_population, fitness_array)
        population_fitness_array = sorted(population_fitness_array, key=lambda array: array[1])
        new_population = [item[0] for item in population_fitness_array[:len(population_fitness_array) // 2]]
        new_population = np.array(new_population)
        return new_population

    def fitness_function(self, population):
        fitness_array = []
        for individual in population:
            u = []
            allel_array = []
            x = self.x_0
            sum = 0
            individual = individual * self.bit_values
            # Decoding
            for i in range(self.N):
                allel_array.append(individual[i * 20:i * 20 + 20])
                u.append(np.sum(allel_array[i]))
            # Next states' calculation
            for j in range(self.N - 1):
                sum += x ** 2 + u[j] ** 2
                x += u[j]

            J = x ** 2 + sum
            fitness_array.append(J)
        self.best_individuals.append(min(fitness_array))
        return fitness_array

    def main_function(self):
        for i in range(20 * self.N):
            self.bit_values.append(random.uniform(-10, 10))
        print("Values to decode: ", self.bit_values)
        for i in range(self.iterations):
            self.current_population = self.generate_population(self.current_population)

    def print_data(self):
        print("Best individual: ", self.current_population[0])
        print("Best individual's fitness function: ", min(self.best_individuals))

    def plot_data(self):
        plt.plot(self.best_individuals)
        plt.title(f"Best individual's fitness function for N = {self.N}")
        plt.xlabel("Iterations number")
        plt.ylabel("Fitness")
        plt.show()


algo = Algorithm(70, 1000)
algo.main_function()
algo.print_data()
algo.plot_data()
