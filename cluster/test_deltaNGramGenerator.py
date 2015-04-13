from unittest import TestCase

from mock import Mock

from cluster.degree_statistics_generator import DegreeStatisticsGenerator
from cluster.delta_n_gram_generator import DeltaNGramGenerator


__author__ = 'Jakob Zwiener'


class TestDeltaNGramGenerator(TestCase):
    def test_as_n_grams(self):
        # TODO(zwiener): Use a more likely generator here.
        statistics_generator = DegreeStatisticsGenerator()
        n_gram_generator = DeltaNGramGenerator(statistics_generator, 3)
        statistics_generator.get_statistics = Mock()
        statistics_generator.get_statistics.return_value = [1, 2, 3, 4, 5, 1, 2, 5, 2]
        expected_3_grams = [(0, 1, 2), (0, 1, 2), (0, 1, 2), (0, 1, -3), (0, -4, -3), (0, 1, 4), (0, 3, 0)]

        actual_3_grams = n_gram_generator.as_n_grams(None, None)

        self.assertEqual(expected_3_grams, actual_3_grams)