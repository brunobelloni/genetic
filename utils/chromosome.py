from __future__ import annotations

from functools import reduce

from .gene import Gene
import random


class Chromosome:
    def __init__(self, population: Population, initialize: bool = True):
        """
        The chromosome contains information which feature is included and which is excluded.

        :param population: contains a reference to the chromosome population
        :param initialize: defines if chromosome should be randomly initialized
        """
        self.genes: list[Gene] = list()
        self.population: Population = population

        if initialize:
            self.initilize()

    def initilize(self) -> None:
        """
        Initialize the chromosome
        """
        src_phrase = self.population.genetic.src_phrase
        for _ in range(len(src_phrase)):
            gene = Gene(chromosome=self)
            self.genes.append(gene)

    @property
    def fitness(self) -> float:
        """
        Evaluates the chromosome with a note. Note 100 means that the sentence is correct.
        """
        fit = 0
        src_phrase = self.population.genetic.src_phrase
        for gene, letter in zip(self.genes, src_phrase):
            if gene.letter == letter:
                fit += 1
        return 100 * fit / len(src_phrase)

    def mutation(self):
        """
        apply a mutation possibility to all chromosome genes
        """
        new_chromosome = Chromosome(population=self.population, initialize=False)
        new_chromosome.set_phrase(self.get_phrase)

        for gene in new_chromosome.genes:
            if random.random() * 100 < self.population.genetic.mutation_rate:
                gene.initilize()  # draws a new value for the chromosome

        if self.fitness < new_chromosome.fitness:
            self.population.chromosomes.append(new_chromosome)

    def crossover(self, chromosome: Chromosome) -> tuple[Chromosome, Chromosome]:
        """
        crosses two chromosomes
        :param chromosome: chromosome that will be crossed with self
        """

        phrase_len = len(self.population.genetic.src_phrase)
        middle_point = random.randint(1, phrase_len - 2)

        new_chromosome1 = Chromosome(population=self.population, initialize=False)
        start_half = self.get_start_half(middle_point)
        end_half = chromosome.get_end_half(middle_point)
        new_chromosome1.set_phrase(phrase=start_half + end_half)

        new_chromosome2 = Chromosome(population=self.population, initialize=False)
        start_half = chromosome.get_start_half(middle_point)
        end_half = self.get_end_half(middle_point)
        new_chromosome2.set_phrase(phrase=start_half + end_half)

        return new_chromosome1, new_chromosome2

    def get_start_half(self, half) -> str:
        return self.get_phrase[:half]

    def get_end_half(self, half) -> str:
        return self.get_phrase[half:]

    @property
    def get_phrase(self) -> str:
        return ''.join(map(lambda gene: gene.letter, self.genes))

    def set_phrase(self, phrase: str):
        self.genes.clear()
        for letter in phrase:
            gene = Gene(letter=letter, chromosome=self)
            self.genes.append(gene)

    def __str__(self):
        return f'{self.fitness:.2f}% = {self.get_phrase}'

    def __repr__(self):
        return self.__str__()
