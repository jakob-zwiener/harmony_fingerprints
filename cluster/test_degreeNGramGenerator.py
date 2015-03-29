from unittest import TestCase

from cluster.degree_n_gram_generator import DegreeNGramGenerator


__author__ = 'Jakob Zwiener'


class TestDegreeNGramGenerator(TestCase):
    def test_make_n_grams(self):
        generator = DegreeNGramGenerator(None, None, 3)
        expected_3_grams = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (6, 7, 8), (7, 8, 9)]

        actual_3_grams = generator.make_n_grams([1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(expected_3_grams, actual_3_grams)




