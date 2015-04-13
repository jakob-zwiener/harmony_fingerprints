from cluster.n_gram_generator import NGramGenerator

__author__ = 'Jakob Zwiener'


class DeltaNGramGenerator(object):
    def __init__(self, statistics_generator, n):
        self.n_gram_generator = NGramGenerator(statistics_generator, n)
        self.statistics_generator = statistics_generator
        self.n = n

    def as_n_grams(self, grid_lines, score):
        n_grams = self.n_gram_generator.as_n_grams(grid_lines, score)
        delta_n_grams = []

        for n_gram in n_grams:
            reference = n_gram[0]
            delta_n_gram = []
            for value in n_gram:
                delta_n_gram.append(value - reference)

            delta_n_grams.append(tuple(delta_n_gram))

        return delta_n_grams
