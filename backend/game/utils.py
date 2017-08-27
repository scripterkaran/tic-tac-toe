import numpy


def generate_winning_positions():
    """Returns a list of Winning combination sets across rows, columns and diagonal
    """
    winning_combos = []
    for row in range(3):
        win_set = set()
        for col in range(3):
            win_set.add((row, col))
        winning_combos.append(win_set)
    for col in range(3):
        win_set = set()
        for row in range(3):
            win_set.add((row, col))
        winning_combos.append(win_set)
    winning_combos.append(set([(0, 0), (1, 1), (2, 2)]))
    winning_combos.append(set([(0, 2), (1, 1), (2, 0)]))

    return winning_combos

position_array = numpy.array([[0,1,2],
                             [3,4,5],
                             [6,7,8]])

def get_coordinates_by_position(position=0):
    """Returns the row col co-ordinate in a 3x3 matrices for position between 0 to 8
    """
    pos = numpy.where(position_array == position)
    return tuple(zip(*pos))