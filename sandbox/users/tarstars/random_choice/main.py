import random
from typing import List


class Generator:
    """
    Stores weights and allows to pick index of random object
    """
    def __init__(self, tree: List[int], last_level_length: int):
        """
        Intrinsic structure: the tree and the length of the last level of the tree
        """
        self.tree = tree
        self.last_level_length = last_level_length

    @classmethod
    def from_weights(cls, weights: List[int]):
        """
        Constructs Generator from array of weights
        """
        n = len(weights)

        last_level_length = 1
        while last_level_length < n:
            last_level_length *= 2

        tree = [0] * (2 * last_level_length - 1)
        for ind in range(n):
            tree[last_level_length - 1 + ind] = weights[ind]

        for ind in range(last_level_length - 2, -1, -1):
            tree[ind] = tree[2 * ind + 1] + tree[2 * ind + 2]

        self = cls(tree, last_level_length)

        return self

    def __iter__(self):
        """
        Makes this object iterable
        """
        return self

    def __next__(self):
        """
        Iterates over objects. Each iteration is selection of the index of some random object
        according to weights of objects.
        """
        if not self.tree[0]:
            raise StopIteration

        x = random.random() * self.tree[0]
        current = 0
        while current < self.last_level_length - 1:
            if self.tree[current * 2 + 1] and x < self.tree[current * 2 + 1]:
                current = current * 2 + 1
            else:
                current = current * 2 + 2
                x -= self.tree[current - 1]

        result = current - (self.last_level_length - 1)

        leaf = self.tree[current]
        while current >= 0:
            self.tree[current] -= leaf
            current = (current - 1) // 2

        return result


def main():
    determined = [100, 1, 1000, 1000000]
    obvious = [1, 4, 3, 2]

    random.seed(100500)

    for _ in range(10):
        g = Generator.from_weights(determined)
        print(list(g))


if __name__ == '__main__':
    main()
