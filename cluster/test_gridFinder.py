from unittest import TestCase

from music21 import corpus

from cluster.grid_finder import GridFinder


__author__ = 'Jakob Zwiener'


class TestGridFinder(TestCase):

    def test_findGrid(self):
        actual_grid_size = self.findGridFor('bach', 0)
        self.assertEqual(1, actual_grid_size)

        actual_grid_size = self.findGridFor('bach', 110)
        self.assertEqual(1, actual_grid_size)

        actual_grid_size = self.findGridFor('bach', 325)
        self.assertEqual(1, actual_grid_size)

    def findGridFor(self, composer, score_number):
        score = corpus.parse(corpus.getComposer(composer)[score_number])
        return GridFinder(score).findGrid()