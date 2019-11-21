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

    def initilize(self) -> None:
        """
        Initialize the population
        """
        for _ in range(self.num_chromosomes):
            chromosome = Chromosome(population=self)
            self.chromosomes.append(chromosome)

    def selection(self) -> tuple[Chromosome, Chromosome]:
        """
        Select the top two chromosomes in the population
        """
        list_fit: List[Chromosome] = [chromosome for chromosome in self.chromosomes]
        list_fit.sort(key=lambda chromosome: chromosome.fitness(), reverse=True)
        return list_fit[0], list_fit[1]

    def crossover(self) -> None:
        """
        crosses two chromosomes
        """
        chromosome1, chromosome2 = self.selection()
        new_cromossome1, new_cromossome2 = chromosome1.crossover(chromosome2)

        self.chromosomes.append(new_cromossome1)
        self.chromosomes.append(new_cromossome2)

    def mutation(self) -> None:
        pass

    def fitness(self) -> None:
        pass

    def eliminate_less_fit(self) -> None:
        pass
