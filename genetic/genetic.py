from __future__ import annotations

from .chromosome import Chromosome
from .population import Population


class Genetic:
    def __init__(self, num_populations: int, num_chromosomes: int, mutation_rate: float, src_phrase: str):
        """
        Class that manages various populations

        :param src_phrase: phrase to be found
        :param mutation_rate: Probablity of chromosome mutation
        :param num_populations: Number of populations
        :param num_chromosomes: Number of chromosomes in population (generation)
        """
        self.src_phrase = src_phrase
        self.mutation_rate = mutation_rate
        self.num_populations = num_populations
        self.num_chromosomes = num_chromosomes

        self.populations: list[Population] = list()
        self.best_chromosome: Chromosome = None
        self.initilize()

    def initilize(self) -> None:
        """
        Initialize the population list
        """
        for _ in range(self.num_populations):
            population = Population(num_chromosomes=self.num_chromosomes, genetic=self)
            self.populations.append(population)
        self.update_best_chromosome()  # fit the generation

    def log(self, generation: int) -> None:
        """
        logs the current state of each generation
        """
        self.update_best_chromosome()  # fit each generation

        print(f'best match: {self.best_chromosome.fitness:.2f}% = {self.best_chromosome.get_phrase}')
        print(f'total generations: {generation}')
        print(f'avarage fitness: {(self.avarage_fitness):.2f}%')
        print(f'total population: {self.num_populations}')
        print(f'mutation rate: {self.mutation_rate}%')

    def update_best_chromosome(self):
        """
        selects the best chromosome from the best chromosomes in each population
        """
        chromosomes: list[Chromosome] = list()

        for population in self.populations:
            chromosomes.append(population.get_best_chromosome())

        self.best_chromosome = max(chromosomes, key=lambda cromossomo: cromossomo.fitness)

    @property
    def avarage_fitness(self):
        """
        calculates the average fitness the best chromosomes
        """
        sum: float = 0

        for population in self.populations:
            sum += population.get_best_chromosome().fitness

        return sum / self.num_populations
