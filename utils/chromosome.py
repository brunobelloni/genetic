from __future__ import annotations

from .gene import Gene
import random
from copy import deepcopy


class Chromosome:
    def __init__(self, population: Population, initialize: bool = True):
        """
        The chromosome contains information which feature is included and which is excluded.
        """
        self.genes: list[Gene] = list()
        self.population = population

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

    def fitness(self) -> float:
        """
        Evaluates the chromosome with a note.
        Note 100 means that the sentence is correct.
        """
        fit = 0
        src_phrase = self.population.genetic.src_phrase
        for gene, letter in zip(self.genes, src_phrase):
            if gene.letter == letter:
                fit += 1
        return (100 * fit) / len(src_phrase)

    def mutation(self):
        save = Chromosome(population=self.population, initialize=False)
        save.set_phrase(self.get_phrase)
        random_int = random.randint(0, len(self.genes) - 1)
        save.genes[random_int].initilize()

        if self.fitness() < save.fitness():
            self = save

    def crossover(self, chromosome: Chromosome) -> tuple[Chromosome, Chromosome]:
        """
        crosses two chromosomes
        """
        new_chromosome1 = Chromosome(population=self.population, initialize=False)
        new_chromosome1.set_start_half(self.get_start_half())
        new_chromosome1.set_end_half(chromosome.get_end_half())

        new_chromosome2 = Chromosome(population=self.population, initialize=False)
        new_chromosome2.set_start_half(chromosome.get_start_half())
        new_chromosome2.set_end_half(self.get_end_half())

        return new_chromosome1, new_chromosome2

    def get_start_half(self) -> str:
        """
        first half of chromosome
        """
        return self.get_phrase[:int(len(self.get_phrase) / 2)]

    def set_start_half(self, start_half: str):
        """
        sets the first part of chromosome
        #NOTE needs to be used before method set_end_half
        """
        for letter in start_half:
            gene = Gene(letter=letter, chromosome=self)
            self.genes.append(gene)

    def get_end_half(self) -> str:
        """
        second half of chromosome
        """
        return self.get_phrase[int(len(self.get_phrase) / 2):]

    def set_end_half(self, end_half: str):
        """
        sets the second part of chromosome
        #NOTE needs to be used after method set_start_half
        """
        for letter in end_half:
            gene = Gene(letter=letter, chromosome=self)
            self.genes.append(gene)

    @property
    def get_phrase(self) -> str:
        return ''.join(map(lambda gene: gene.letter, self.genes))

    def set_phrase(self, phrase: str):
        self.genes.clear()
        for letter in phrase:
            gene = Gene(letter=letter, chromosome=self)
            self.genes.append(gene)

    def __str__(self):
        return f'{self.fitness():.2f}% = {self.get_phrase}'

    def __repr__(self):
        return self.__str__()
