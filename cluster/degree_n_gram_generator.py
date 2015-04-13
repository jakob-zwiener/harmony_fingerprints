from music21 import harmony


__author__ = 'Jakob Zwiener'


# TODO(zwiener): rename
class DegreeNGramGenerator(object):

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
            analysis_list.append(scale_degree)

        return analysis_list









