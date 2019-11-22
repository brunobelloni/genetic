from __future__ import annotations

from utils.genetic import Genetic
import random


def run():
    random.seed(4252695618)
    phrase = 'infinite monkey theorem'
    generation = 0

    genetic = Genetic(
        src_phrase=phrase,
        num_populations=200,
        num_chromosomes=5,
        mutation_rate=5
    )

    while genetic.best_chromosome.get_phrase != phrase:
        for population in genetic.populations:
            population.crossover()
            population.mutation()
            population.eliminate_less_fit()

        generation += 1
        genetic.log(generation=generation)


if __name__ == '__main__':
    run()
