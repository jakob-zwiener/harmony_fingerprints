from unittest import TestCase

from mock import Mock

from cluster.degree_n_gram_generator import DegreeNGramGenerator
from cluster.n_gram_generator import NGramGenerator


__author__ = 'Jakob Zwiener'


class TestDegreeNGramGenerator(TestCase):

    def test_as_n_grams(self):
        statistics_generator = DegreeNGramGenerator()
        n_gram_generator = NGramGenerator(statistics_generator, 3)
        statistics_generator.get_statistics = Mock()
        statistics_generator.get_statistics.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_3_grams = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (6, 7, 8), (7, 8, 9)]

        actual_3_grams = n_gram_generator.as_n_grams(None, None)

        self.assertEqual(expected_3_grams, actual_3_grams)

    def test_as_histogram(self):
        statistics_generator = DegreeNGramGenerator()
        histogram_generator = NGramGenerator(statistics_generator, 3)
        statistics_generator.get_statistics = Mock()
        statistics_generator.get_statistics.return_value = [1, 2, 3, 1, 2, 3, 7, 8, 9]
        expected_histogram = {(1, 2, 3): 2, (2, 3, 1): 1, (3, 1, 2): 1, (2, 3, 7): 1, (3, 7, 8): 1, (7, 8, 9): 1}

        actual_histogram = histogram_generator.as_histogram(None, None)

        self.assertEqual(expected_histogram, actual_histogram)



