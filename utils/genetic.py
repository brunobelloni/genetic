class Genetic:
    def __init__(self, num_generations: int, num_chromosomes: int, mutation_rate: float):
        """
        :param mutation_rate: Probablity of chromosome mutation
        :param num_generations: Number of generations
        :param num_chromosomes: Number of chromosomes in population (generation)
        """
        self._mutation_rate = mutation_rate
        self._num_generations = num_generations
        self._num_chromosomes = num_chromosomes

        self._generations = list()

    def selection(self, population):
        pass

    def initilize(self):
        pass

    def crossover(self, population):
        pass

    def mutate(self, population):
        pass

    def generate(self, population):
        pass
