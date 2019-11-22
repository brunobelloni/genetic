from __future__ import annotations

from .chromosome import Chromosome


class Population:
    def __init__(self, num_chromosomes: int, genetic: Genetic):
        """
        Population contains several instances of different chromosomes.
        It is just a collection of different feature subsets.

        :param genetic: reference to the class that manages populations
        :param num_chromosomes: amount of chromosomes in the population
        """
        self.genetic = genetic
        self.num_chromosomes = num_chromosomes
        self.chromosomes: list[Chromosome] = list()

        self.initilize()

    def initilize(self) -> None:
        """
        Initialize the population
        """
        for _ in range(self.num_chromosomes):
            chromosome = Chromosome(population=self)
            self.chromosomes.append(chromosome)

    def selection(self, quant: int = 2, reverse=True) -> list[utils.chromosome.Chromosome]:
        """
        Select chromosomes in the population
        :param quant: number of chromosomes to select
        :param reverse: reverse chromosome list
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
        """
        mutates all chromosomes in this population
        """
        for chromosome in self.chromosomes:
            chromosome.mutation()

    def eliminate_less_fit(self) -> None:
        """
        eliminates less fit chromosomes
        the cutoff margin is the number of chromosomes defined
        """
        chromosomes_to_remove = self.selection(quant=len(self.chromosomes) - self.num_chromosomes, reverse=False)
        for chromosome in chromosomes_to_remove:
            self.chromosomes.remove(chromosome)

    def get_best_chromosome(self) -> Chromosome:
        """
        returns the best chromosome in this population
        """
        return max(self.chromosomes, key=lambda chromosome: chromosome.fitness)
