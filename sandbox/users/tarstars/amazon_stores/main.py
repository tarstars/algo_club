import unittest


def lays_in(position, rows, columns):
    p, q = position
    return (0 <= p < rows) and (0 <= q < columns)


def get_neighbours(rows, columns, position):
    dpdq = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dp, dq in dpdq:
        current_p, current_q = position
        next_p, next_q = current_p + dp, current_q + dq
        next_position = next_p, next_q
        if lays_in(next_position, rows, columns):
            yield next_position


def numberAmazonGoStores(rows, columns, grid):
    # WRITE YOUR CODE HERE
    disconnected_components = 0

    if not rows or not columns:
        return disconnected_components

    visited = set()
    for p in range(rows):
        for q in range(columns):
            if grid[p][q] and (p, q) not in visited:
                visited.add((p, q))
                todo = [(p, q)]
                disconnected_components += 1

                while todo:
                    current_position = todo.pop()
                    for next_position in get_neighbours(rows, columns, current_position):
                        next_p, next_q = next_position
                        if grid[next_p][next_q] and next_position not in visited:
                            visited.add(next_position)
                            todo.append(next_position)

    return disconnected_components


class TestNumberAmazonGoStores(unittest.TestCase):
    def test_number_of_stores_00(self):
        rows = 5
        columns = 4
        grid = [
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(3, numberAmazonGoStores(rows, columns, grid))

    def test_number_of_stores_01(self):
        rows = 5
        columns = 4
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(0, numberAmazonGoStores(rows, columns, grid))

    def test_number_of_stores_02(self):
        rows = 5
        columns = 6
        grid = [
            [1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]
        ]
        self.assertEqual(1, numberAmazonGoStores(rows, columns, grid))


if __name__ == '__main__':
    unittest.main()
