from __future__ import annotations

import random

import utils.chromosome


class Population:
    def __init__(self, num_chromosomes: int, genetic: Genetic):
        """
        Population contains several instances of different chromosomes.
        It is just a collection of different feature subsets.
        """
        self.num_chromosomes = num_chromosomes
        self.chromosomes: list[Chromosome] = list()
        self.genetic = genetic

        self.initilize()

    def initilize(self) -> None:
        """
        Initialize the population
        """
        for _ in range(self.num_chromosomes):
            chromosome = utils.chromosome.Chromosome(population=self)
            self.chromosomes.append(chromosome)

    def selection(self, quant: int = 2, reverse=True) -> list[utils.chromosome.Chromosome]:
        """
        Select the top two chromosomes in the population
        """
        list_fit: List[utils.chromosome.Chromosome] = [chromosome for chromosome in self.chromosomes]
        list_fit.sort(key=lambda chromosome: chromosome.fitness, reverse=reverse)
        return list_fit[:quant]

    def crossover(self) -> None:
        """
        crosses two chromosomes
        """
        chromosome1, chromosome2 = self.selection()
        new_chromosome1, new_chromosome2 = chromosome1.crossover(chromosome2)

        self.chromosomes.append(new_chromosome1)
        self.chromosomes.append(new_chromosome2)

    def mutation(self) -> None:
        for chromosome in self.chromosomes:
            chromosome.mutation()

    def eliminate_less_fit(self) -> None:
        chromosomes_to_remove = self.selection(quant=len(self.chromosomes) - self.num_chromosomes, reverse=False)
        for chromosome in chromosomes_to_remove:
            self.chromosomes.remove(chromosome)
