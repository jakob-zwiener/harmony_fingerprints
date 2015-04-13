from unittest import TestCase

from mock import Mock

from cluster.degree_statistics_generator import DegreeStatisticsGenerator
from cluster.histogram_generator import HistogramGenerator
from cluster.n_gram_generator import NGramGenerator


__author__ = 'Jakob Zwiener'


class TestHistogramGenerator(TestCase):
    def test_as_histogram(self):
        statistics_generator = DegreeStatisticsGenerator()
        histogram_generator = HistogramGenerator(NGramGenerator(statistics_generator, 3))
        statistics_generator.get_statistics = Mock()
        statistics_generator.get_statistics.return_value = [1, 2, 3, 1, 2, 3, 7, 8, 9]
        expected_histogram = {(1, 2, 3): 2 / 7.0, (2, 3, 1): 1 / 7.0, (3, 1, 2): 1 / 7.0, (2, 3, 7): 1 / 7.0,
                              (3, 7, 8): 1 / 7.0, (7, 8, 9): 1 / 7.0}

        actual_histogram = histogram_generator.as_histogram(None, None)

        self.assertEqual(expected_histogram, actual_histogram)