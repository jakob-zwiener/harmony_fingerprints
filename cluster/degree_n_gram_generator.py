from collections import defaultdict
from collections import deque

from music21 import harmony


__author__ = 'Jakob Zwiener'


class DegreeNGramGenerator(object):
    def __init__(self, n):
        self.n = n

    def get_statistics(self, grid_lines, score):
        chordified_score = score.chordify().flat
        key = score.analyze('key')

        analysis_list = []
        for grid_line in grid_lines:
            chords = chordified_score.getElementsByOffset(grid_line).getElementsByClass('Chord')
            if not chords:
                continue
            chord = chords[0]

            chord_symbol = harmony.chordSymbolFigureFromChord(chord, True)[1]
            scale_degree = key.getScaleDegreeAndAccidentalFromPitch(chord.findRoot())[0]
            analysis_list.append((chord_symbol, scale_degree))

        return analysis_list

    # TODO(zwiener): In the future this method might be pulled up.
    def as_histogram(self, grid_lines, score):
        n_grams = self.as_n_grams(grid_lines, score)
        histogram = defaultdict(int)

        for n_gram in n_grams:
            histogram[n_gram] += 1

        return histogram

    # TODO(zwiener): In the future this method might be pulled up.
    def as_n_grams(self, grid_lines, score):
        current_n_gram = deque(maxlen=self.n)
        n_grams = []

        for entry in self.get_statistics(grid_lines, score):
            current_n_gram.append(entry)

            # Wait for the n-gram to be filled.
            if len(current_n_gram) < self.n:
                continue

            n_grams.append(tuple(current_n_gram))

        return n_grams








