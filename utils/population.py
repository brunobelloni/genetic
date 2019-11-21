from __future__ import annotations

from utils.chromosome import Chromosome


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

    def initilize(self):
        """
        Initialize the population
        """
        for _ in range(self.num_chromosomes):
            chromosome = Chromosome(population=self)
            self.chromosomes.append(chromosome)

    def selection(self):
        """
        Select the top two chromosomes in the population
        """
        list_fit: List[Chromosome] = [chromosome for chromosome in self.chromosomes]
        list_fit.sort(key=lambda chromosome: chromosome.fitness(), reverse=True)
        return list_fit[0], list_fit[1]

    def crossover(self):
        """
        crosses two chromosomes
        """
        chromosome1, chromosome2 = self.selection()
        chromosome1.crossover(chromosome2)
