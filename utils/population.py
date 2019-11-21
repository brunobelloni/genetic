from _ast import Tuple

from .chromosome import Chromosome


class Population:
    def __init__(self, num_chromosomes: int, genetic):
        """
        Population contains several instances of different chromosomes.
        It is just a collection of different feature subsets.
        """
        self.num_chromosomes = num_chromosomes
        self.chromosomes = list()  # list of Chromosome
        self.genetic = genetic  # reference to Genetic

        self.initilize()

    def initilize(self):
        """
        Initialize the population
        """
        for _ in range(self.num_chromosomes):
            chromosome = Chromosome(population=self)

            self.chromosomes.append(chromosome)

        self.crossover()

    def selection(self) -> [Chromosome, Chromosome]:
        """
        Select the top two chromosomes in the population
        """
        list_fit = [chromosome for chromosome in self.chromosomes]
        list_fit.sort(key=lambda chromosome: chromosome.fitness(), reverse=True)
        return list_fit[0], list_fit[1]

    def crossover(self):
        chromosome1, chromosome2 = self.selection()
        # chromosome1.crossover(chromosome2)
