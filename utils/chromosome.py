from __future__ import annotations

from .gene import Gene


class Chromosome:
    def __init__(self, population):
        """
        The chromosome contains information which feature is included and which is excluded.
        """
        self.genes = list()  # list of Gene
        self.population = population  # reference to Population

        self.initilize()

    def initilize(self):
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
        pass

    def crossover(self, chromosome: Chromosome) -> [Chromosome, Chromosome]:
        new_cromossome1 = Chromosome()
        new_cromossome2 = Chromosome()

        return new_cromossome1, new_cromossome2

    def start_half(self) -> str:
        """
        first half of chromosome
        """
        return self._phrase[:len(self._phrase) / 2]

    def end_half(self):
        """
        second half of chromosome
        """
        return self._phrase[len(self._phrase) / 2:]

    @property
    def _phrase(self):
        return ''.join(map(lambda gene: gene.letter, self.genes))

    def __str__(self):
        return '{0:.1f}% = {1}'.format(self.fitness(), self._phrase)

    def __repr__(self):
        return self.__str__()
