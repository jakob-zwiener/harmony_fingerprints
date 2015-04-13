__author__ = 'Jakob Zwiener'


class IntervalStatisticsGenerator(object):
    def __init__(self, n):
        self.n = n

    def get_statistics(self, grid_lines, score):
        chordified_score = score.chordify().flat

        analysis_list = []
        for grid_line in grid_lines:
            chords = chordified_score.getElementsByOffset(grid_line).getElementsByClass('Chord')
            if not chords:
                continue
            chord = chords[0]

            root_pitch_scale = chord.root().ps
            analysis_list.append(root_pitch_scale)

        return analysis_list