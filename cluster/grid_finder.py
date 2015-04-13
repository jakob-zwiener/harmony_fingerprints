import numpy

__author__ = 'Jakob Zwiener'


class GridFinder(object):
    def __init__(self, beta=0.5):
        self.beta_square = beta * beta

    def find_grid(self, score):
        score = score.flat
        score_max = 0
        chosen_grid_offset = None
        for grid_offset in [0.125, 0.25, 0.5, 1, 2, 4]:
            score_sum = 0
            hits = 0
            grid_lines = numpy.arange(0, score.highestTime, grid_offset)
            for offset in grid_lines:
                number_of_notes = len(score.getElementsByOffset(offset))
                score_sum += number_of_notes

                if number_of_notes:
                    hits += 1
            # Ratio of grid lines that contain a chord.
            precision = hits / float(len(grid_lines))
            # Ratio of notes hit by grid line.
            recall = score_sum / float(len(score.elements))
            f_measure = (1 + self.beta_square) * precision * recall / (self.beta_square * precision + recall)
            print grid_offset, f_measure, precision, recall
            # Bigger offsets are preferred.
            if f_measure >= score_max:
                score_max = f_measure
                chosen_grid_offset = grid_offset

        return chosen_grid_offset
