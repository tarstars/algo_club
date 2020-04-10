import unittest


def lengthEachScene(inputList):
    # WRITE YOUR CODE HERE

    # for each letter find the rightmost position of this letter
    rightmost = {}
    for ind, letter in enumerate(inputList):
        rightmost[letter] = ind

    lengths_of_scenes = []
    n = len(inputList)
    ind = 0
    while ind < n:
        begin_of_scene = ind
        next_ind = rightmost[inputList[ind]] + 1
        while ind < n and ind < next_ind:
            next_ind = max(next_ind, rightmost[inputList[ind]] + 1)
            ind += 1
        lengths_of_scenes.append(next_ind - begin_of_scene)
        ind = next_ind

    return lengths_of_scenes


class TestLengthScene(unittest.TestCase):
    def test_length_scene_00(self):
        self.assertEqual([1, 1, 1], lengthEachScene(['a', 'b', 'c']))

    def test_length_scene_01(self):
        self.assertEqual([4], lengthEachScene(['a', 'b', 'c', 'a']))

    def test_length_scene_02(self):               #   0    1    2    3    4    5    6    7    8    9
        self.assertEqual([9, 7, 8], lengthEachScene(['a', 'b', 'a', 'b', 'c', 'b', 'a', 'c', 'a', 'd',
                                                     'e', 'f', 'e', 'g', 'd', 'e', 'h', 'i', 'j', 'h',
                                                     'k', 'l', 'i', 'j']))


if __name__ == '__main__':
    unittest.main()
