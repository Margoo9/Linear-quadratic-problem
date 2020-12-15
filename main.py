import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.linalg
from scipy.stats import norm


class Algorithm:
    def __init__(self, population_size, epochs_num, generations_num):
        self.population_size = population_size
        self.iterations_num = epochs_num
        self.generations_num = generations_num
        self.epsilon = norm.rvs(loc=0, scale=1, size=(1, self.population_size))[0]

    def generate_first_population(self):
        return norm.rvs(loc=0, scale=1, size=(1, self.population_size))[0]

    def fitness_function(self):
        pass

    def fitness_computation(self):
        pass

    # non-adaptive mutation
    def modify_haploid(self, x, sigma):
        v = []
        for i in range(self.population_size):
            v[i] = np.transpose(v[i-1] + x[i] + sigma[i]*self.epsilon[i])
        return v

    def generate_new_population(self):
        pass

    def generate_child(self):
        pass


a = Algorithm(200, 10, 10)
a.generate_first_population()
