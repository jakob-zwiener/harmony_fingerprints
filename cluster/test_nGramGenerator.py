from unittest import TestCase

from mock import Mock

from cluster.degree_statistics_generator import DegreeStatisticsGenerator
from cluster.n_gram_generator import NGramGenerator


__author__ = 'Jakob Zwiener'


class TestNGramGenerator(TestCase):

    def test_as_n_grams(self):
        statistics_generator = DegreeStatisticsGenerator()
        n_gram_generator = NGramGenerator(statistics_generator, 3)
        statistics_generator.get_statistics = Mock()
        statistics_generator.get_statistics.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_3_grams = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (6, 7, 8), (7, 8, 9)]

        actual_3_grams = n_gram_generator.as_n_grams(None, None)

        self.assertEqual(expected_3_grams, actual_3_grams)



