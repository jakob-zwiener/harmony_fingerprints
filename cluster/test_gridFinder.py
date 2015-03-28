from unittest import TestCase

from music21 import corpus

from cluster.grid_finder import GridFinder


__author__ = 'Jakob Zwiener'


class TestGridFinder(TestCase):
    def test_findGrid(self):
        score = corpus.parse(corpus.getComposer('bach')[0])
        actual_grid_size = GridFinder(score).findGrid()
        self.assertEqual(1, actual_grid_size)