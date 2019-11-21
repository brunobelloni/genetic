from utils.genetic import Genetic


def run():
    phrase = 'abcd'
    generation = 0

    genetic = Genetic(
        src_phrase=phrase,
        num_populations=100,
        num_chromosomes=50,
        mutation_rate=0.8
    )

    while genetic.best_match != f'{100:.2f}% = {phrase}':
        generation += 1
        genetic.logs(generation=generation)

        for population in genetic.populations:
            population.crossover()
            population.mutation()
            population.eliminate_less_fit()

        genetic.update_best_match()


if __name__ == '__main__':
    run()
