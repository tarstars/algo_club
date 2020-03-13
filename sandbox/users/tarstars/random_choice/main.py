import random


class Generator:
    def __init__(self, tree, l):
        self.tree = tree
        self.l = l

    @classmethod
    def from_objects(cls, objects):
        n = len(objects)

        l = 1
        while l < n:
            l *= 2

        tree = [0] * (2 * l - 1)
        for ind in range(n):
            tree[l - 1 + ind] = objects[ind]

        for ind in range(l - 2, -1, -1):
            tree[ind] = tree[2 * ind + 1] + tree[2 * ind + 2]

        self = cls(tree, l)

        return self

    def __iter__(self):
        return self

    def __next__(self):
        if not self.tree[0]:
            raise StopIteration

        x = random.random() * self.tree[0]
        current = 0
        while current < self.l - 1:  # current * 2 + 1 >= 2 * l - 1
            if self.tree[current * 2 + 1] and x < self.tree[current * 2 + 1]:
                current = current * 2 + 1
            else:
                current = current * 2 + 2
                x -= self.tree[current - 1]

        result = current - (self.l - 1)

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
        g = Generator.from_objects(determined)
        print(list(g))


if __name__ == '__main__':
    main()
