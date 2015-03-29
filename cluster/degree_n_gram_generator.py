from collections import deque

from music21 import harmony


__author__ = 'Jakob Zwiener'


class DegreeNGramGenerator(object):
    def __init__(self, grid_lines, score, n):
        self.grid_lines = grid_lines
        self.score = score
        self.n = n

    def get_statistics(self):
        chordified_score = self.score.chordify().flat
        key = self.score.analyze('key')

        analyis_list = []
        for grid_line in self.grid_lines:
            chords = chordified_score.getElementsByOffset(grid_line).getElementsByClass('Chord')
            if not chords:
                continue
            chord = chords[0]

            chord_symbol = harmony.chordSymbolFigureFromChord(chord, True)[1]
            scale_degree = key.getScaleDegreeAndAccidentalFromPitch(chord.findRoot())[0]
            analyis_list.append((chord_symbol, scale_degree))

        return self.make_n_grams(analyis_list)

    # TODO(zwiener): In the future this method might be pulled up.
    def make_n_grams(self, analysis_list):
        current_n_gram = deque(maxlen=self.n)
        n_grams = []

        for entry in analysis_list:
            current_n_gram.append(entry)

            # Wait for the n-gram to be filled.
            if len(current_n_gram) < self.n:
                continue

            n_grams.append(tuple(current_n_gram))

        return n_grams








