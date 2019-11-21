from utils.genetic import Genetic


def run():
    phrase = 'Frase de Teste'

    genetic = Genetic(
        src_phrase=phrase,
        num_populations=10,
        num_chromosomes=30,
        crossover_rate=0.4,
        mutation_rate=0.4,
    )

    print('stop')


if __name__ == '__main__':
    run()
