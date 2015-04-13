from collections import defaultdict

__author__ = 'Jakob Zwiener'


class HistogramGenerator(object):
    def __init__(self, n_gram_generator):
        self.n_gram_generator = n_gram_generator

    def as_histogram(self, grid_lines, score):
        n_grams = self.n_gram_generator.as_n_grams(grid_lines, score)
        histogram = defaultdict(int)

        for n_gram in n_grams:
            histogram[n_gram] += 1

        normal_histogram = {}
        for n_gram, freq in histogram.iteritems():
            normal_histogram[n_gram] = freq / float(len(n_grams))

        return normal_histogram

