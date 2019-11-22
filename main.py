from utils.genetic import Genetic
import random


def run():
    random.seed(2019)
    phrase = 'Infinite Monkey Theorem'
    generation = 0

    genetic = Genetic(
        src_phrase=phrase,
        num_populations=200,
        num_chromosomes=5,
        mutation_rate=0.1
    )

    while genetic.best_phrase != phrase:
        generation += 1

        for population in genetic.populations:
            population.crossover()
            population.mutation()
            population.eliminate_less_fit()

        genetic.update_best_match()
        genetic.log(generation=generation)


if __name__ == '__main__':
    run()
