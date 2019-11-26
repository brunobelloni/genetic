from __future__ import annotations

from genetic.genetic import Genetic
import random


def main():
    random.seed(4252695618)
    phrase = 'infinite monkey theorem'
    generation = 0

    genetic = Genetic(
        src_phrase=phrase,
        num_populations=100,
        num_chromosomes=25,
        mutation_rate=10
    )

    while genetic.best_chromosome.get_phrase != phrase:
        for population in genetic.populations:
            population.crossover()
            population.mutation()
            population.eliminate_less_fit()

        generation += 1
        genetic.log(generation=generation)


if __name__ == '__main__':
    main()
