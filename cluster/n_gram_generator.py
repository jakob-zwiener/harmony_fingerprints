from collections import deque, defaultdict

__author__ = 'Jakob Zwiener'


class NGramGenerator(object):
    def __init__(self, statistics_generator, n):
        self.statistics_generator = statistics_generator
        self.n = n

    def as_histogram(self, grid_lines, score):
        n_grams = self.as_n_grams(grid_lines, score)
        histogram = defaultdict(int)

        for n_gram in n_grams:
            histogram[n_gram] += 1

        return histogram

    def as_n_grams(self, grid_lines, score):
        current_n_gram = deque(maxlen=self.n)
        n_grams = []

        for entry in self.statistics_generator.get_statistics(grid_lines, score):
            current_n_gram.append(entry)

            # Wait for the n-gram to be filled.
            if len(current_n_gram) < self.n:
                continue

            n_grams.append(tuple(current_n_gram))

        return n_grams
