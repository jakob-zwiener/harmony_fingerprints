import numpy

__author__ = 'Jakob Zwiener'


class GridFinder(object):
    def __init__(self, score):
        self.score = score.flat

    def findGrid(self):
        max = 0
        chosen_grid_offset = None
        for grid_offset in [0.125, 0.25, 0.5, 1, 2, 4]:
            sum = 0
            hits = 0
            grid_lines = numpy.arange(0, self.score.highestTime, grid_offset)
            for offset in grid_lines:
                number_of_notes = len(self.score.getElementsByOffset(offset))
                sum += number_of_notes

                if number_of_notes:
                    hits += 1
            # TODO(zwiener: Use f-measure here.
            precision = hits / float(len(grid_lines))
            recall = sum / float(len(self.score.elements))
            beta = 0.5
            beta_square = beta * beta
            f_measure = (1 + beta_square) * precision * recall / (beta_square * precision + recall)
            print grid_offset, f_measure, precision, recall
            # Bigger offsets are preferred.
            if f_measure >= max:
                max = f_measure
                chosen_grid_offset = grid_offset

        return chosen_grid_offset
