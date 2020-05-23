import unittest

# 4:02 - 4:16
from typing import Tuple, List


class Event:
    def __init__(self, coordinate, delta):
        self.coordinate = coordinate
        self.delta = delta


def is_red_ribbon_visible(red: Tuple[int, int],
                          blues: List[Tuple[int, int]]):
    events = [Event(coordinate=red[0], delta=-1),
              Event(coordinate=red[1], delta=1)]

    for blue_patch in blues:
        events.append(Event(coordinate=blue_patch[0], delta=1))
        events.append(Event(coordinate=blue_patch[1], delta=-1))

    events.sort(key=lambda event: (event.coordinate, -event.delta))

    visibility_counter = 0
    for ribbon in events:
        visibility_counter += ribbon.delta
        if visibility_counter == -1:
            return True
    return False


class TestRibbonVisibility(unittest.TestCase):
    def test_visibility_00(self):
        self.assertTrue(is_red_ribbon_visible(red=(0, 1), blues=[]))

    def test_visibility_01(self):
        self.assertFalse(is_red_ribbon_visible(red=(0, 1), blues=[(-1, 2)]))

    def test_visibility_02(self):
        self.assertFalse(is_red_ribbon_visible(red=(0, 1), blues=[(-1, 0.5), (0.5, 2)]))

    def test_visibility_03(self):
        self.assertTrue(is_red_ribbon_visible(red=(-10, -9), blues=[(-1, 0.5), (0.5, 2)]))

    def test_visibility_04(self):
        self.assertTrue(is_red_ribbon_visible(red=(9, 10), blues=[(-1, 0.5), (0.5, 2)]))


if __name__ == '__main__':
    unittest.main()
