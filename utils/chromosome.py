class Chromosome:
    def __init__(self, genes: list):
        """
        The chromosome contains information which feature is included and which is excluded.
        """
        self._genes = genes

    def mutation(self):
        pass

    def crossover(self, chromosome):
        pass
