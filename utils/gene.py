from __future__ import annotations
import random
import string

ascii = [char for char in string.ascii_letters] + [' ']


class Gene:
    def __init__(self, chromosome: Chromosome, letter: str = None):
        """
        Gene can have either a value 1 (feature is included) or 0 (feature is excluded).
        """
        self.letter = letter
        self.chromosome = chromosome

        if self.letter is None:
            self.initilize()

    def initilize(self):
        """
        Initialize the gene
        """
        self.letter = random.choice(ascii)

    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.__str__()
