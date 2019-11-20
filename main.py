from utils.genetic import Genetic


def run():
    genetic = Genetic(
        num_generations=10,
        num_chromosomes=30,
        mutation_rate=0.4
    )


if __name__ == '__main__':
    run()
