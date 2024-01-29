import copy
import unittest


def all_elements(board_size):
    for p in range(board_size):
        def gen_row():
            for q in range(board_size):
                yield p, q
        yield gen_row()

    for q in range(board_size):
        def gen_col():
            for p in range(board_size):
                yield p, q
        yield gen_col()

    def main_diag():
        for p in range(board_size):
            yield p, p
    yield main_diag()

    def second_diag():
        for p in range(board_size):
            yield p, board_size - 1 - p
    yield second_diag()


def find_common_element(it):
    first = True
    value = None

    for v in it:
        if first:
            value = v
            first = False
        else:
            if v != value:
                return None, False
    return value, True


def check_winner(b):
    board_size = len(b)
    
    def get_values(element):
        for p, q in element:
            yield b[p][q]
    for current_element in all_elements(board_size):
        common_element, ok = find_common_element(get_values(current_element))
        if ok and common_element != 0:
            return common_element
    return 0


def all_moves(b, t):
    board_size = len(b)
    for p in range(board_size):
        for q in range(board_size):
            if b[p][q] == 0:
                b_copy = copy.deepcopy(b)
                b_copy[p][q] = t
                yield b_copy


class TestA(unittest.TestCase):
    def test_check_winner_00(self):
        self.assertEqual(check_winner(
            [
                [1, 1, 1],
                [-1, 0, 0],
                [-1, -1, 0]
            ]
        ), 1)

    def test_check_winner_01(self):
        self.assertEqual(check_winner(
            [
                [1, -1, 1],
                [-1, -1, 0],
                [1, -1, 0]
            ]
        ), -1)
