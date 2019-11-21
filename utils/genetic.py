from __future__ import annotations

from utils.chromosome import Chromosome
from .population import Population


class Genetic:
    def __init__(self, num_populations: int, num_chromosomes: int, mutation_rate: float, src_phrase: str):
        """
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

        self.best_match: str = ''
        self.initilize()

    def initilize(self) -> None:
        """
        Initialize the population list
        """
        for _ in range(self.num_populations):
            population = Population(num_chromosomes=self.num_chromosomes, genetic=self)
            self.populations.append(population)

    def logs(self, generation: int):
        print(f'best match: {self.best_match}')
        print(f'total geneartions: {generation}')
        print(f'avarage fitness: {self.avarage_fitness}%')
        print(f'total population: {self.num_populations}')
        print(f'mutation rate: {self.mutation_rate}%')

    def update_best_match(self):
        best_fitness, best_phrase = 0.0, ''
        for population in self.populations:
            for chromosome in population.chromosomes:
                fitness = chromosome.fitness()
                if fitness >= best_fitness:
                    best_fitness, best_phrase = fitness, chromosome.get_phrase
        self.best_match = f'{best_fitness:.2f}% = {best_phrase}'

    @property
    def avarage_fitness(self):
        sum_fitness: float = 0
        total: int = 0
        for population in self.populations:
            for chromosome in population.chromosomes:
                sum_fitness += chromosome.fitness()
                total += 100
        return f'{(sum_fitness / total):.2f}'
