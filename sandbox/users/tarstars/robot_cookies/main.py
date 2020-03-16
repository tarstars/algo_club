import functools
import unittest
import random
import sys
import time

sys.setrecursionlimit(10000)


def non_uniform(r):
    if r < 0.6:
        return 0
    if r < 0.61:
        return 1
    return 2


def generate_map(h, w, seed=100500):
    random.seed(seed)
    s = [['.', '#', '*'][ind] for ind in (non_uniform(random.random()) for _ in range(h * w))]
    return tuple([''.join(s[ind * w: (ind + 1) * w]) for ind in range(h)])


@functools.lru_cache(10 ** 9)
def gather_cookies_helper(maze, p, q):
    if maze[p][q] == '#':
        return None

    if p - 1 < 0 or maze[p - 1][q] == '#':
        u = None
    else:
        u = gather_cookies_helper(maze, p - 1, q)

    if q - 1 < 0 or maze[p][1 - 1] == '#':
        l = None
    else:
        l = gather_cookies_helper(maze, p, q - 1)

    result = 1

    if maze[p][q] == '.':
        result = 0

    if not p and not q:
        return result

    if u is None and l is None:
        return None

    if l is None:
        return result + u

    if u is None:
        return result + l

    return result + max(u, l)


def gather_cookies_recursion(maze):
    h, w = len(maze), len(maze[0])
    return gather_cookies_helper(maze, h - 1, w - 1)


def from_prev_val(curr_cell, prev_val):
    if curr_cell == '#' or prev_val is None:
        return None

    return prev_val + (1 if curr_cell == '*' else 0)


def gather_cookies(maze):
    if maze[0][0] == '#':
        return None

    h, w = len(maze), len(maze[0])
    a = [0] * w
    a[0] = from_prev_val(maze[0][0], 0)

    for q in range(1, w):
        a[q] = from_prev_val(maze[0][q], a[q - 1])

    for p in range(1, h):
        a[0] = from_prev_val(maze[p][0], a[0])
        for q in range(1, w):
            v1 = from_prev_val(maze[p][q], a[q])
            v2 = from_prev_val(maze[p][q], a[q - 1])
            if v1 is None:
                a[q] = v2
            elif v2 is None:
                a[q] = v1
            else:
                a[q] = max(v1, v2)

    return a[-1]


class TestMaze(unittest.TestCase):
    def setUp(self) -> None:
        self.maze_00 = (
            ('...',
             '...',
             '...')
            , 0)  # no walls, no cookies

        self.maze_01 = (
            ('...',
             '*.*',
             '...')
            , 2)  # twe reachable cookies

        self.maze_02 = (
            ('...',
             '.**',
             '.*.')  # there are three of them, but you can reach only one
            , 2)

        self.maze_03 = (
            ('...',
             '...',
             '..*')  # at the last point
            , 1)

        self.maze_04 = (
            ('*..',
             '...',
             '...')  # at the first point
            , 1)

        self.maze_05 = (
            ('...',
             '.##',
             '.#.')  # exit unreachable
            , None)

        self.maze_06 = (
            ('...',
             '#..',
             '*..')  # unreachable cookie behind the wall
            , 0)

    def test_all_mazes(self):
        maze_list = [
            self.maze_00,
            self.maze_01,
            self.maze_02,
            self.maze_03,
            self.maze_04,
            self.maze_05,
            self.maze_06,
        ]

        for maze, answer in maze_list:
            self.assertEqual(answer, gather_cookies(maze), '\n'.join(maze))


if __name__ == '__main__':
    # unittest.main()
    m = generate_map(200, 200, 17)
    start = time.time()
    c1 = gather_cookies_recursion(m)
    c2 = gather_cookies_recursion(m)
    end = time.time()
    print('\n'.join(m), '\n', c1, c2, end - start)
