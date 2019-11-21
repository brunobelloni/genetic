from __future__ import annotations

from .population import Population


class Genetic:
    def __init__(self, num_populations: int, num_chromosomes: int, crossover_rate: float, mutation_rate: float,
                 src_phrase: str):
        """
        :param src_phrase: phrase to be found
        :param mutation_rate: Probablity of chromosome mutation
        :param crossover_rate: Probablity of chromosome crossover
        :param num_populations: Number of populations
        :param num_chromosomes: Number of chromosomes in population (generation)
        """
        self.src_phrase = src_phrase
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.num_populations = num_populations
        self.num_chromosomes = num_chromosomes
        self.populations: list[Population] = list()

        self.initilize()

    def initilize(self):
        """
        Initialize the population list
        """
        for _ in range(self.num_populations):
            population = Population(num_chromosomes=self.num_chromosomes, genetic=self)
            self.populations.append(population)
