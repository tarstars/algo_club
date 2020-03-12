import io
import unittest


def fraction_string(n: int) -> str:
    """For values n greater than 1 this function calculates decimal
    representation of 1/n fraction and puts it in string

    :param n: denominator of fraction
    :return: string with decimal fraction representation 0.<non periodic part> (<periodic part>)
    """
    buf = io.StringIO()

    def f(r):
        return (r * 10) % n

    a = 1

    a = f(a)
    b = f(a)

    while a != b:
        a = f(a)
        b = f(f(b))

    c = 1
    buf.write('0.')
    while b != c:
        buf.write(str((c * 10) // n))
        c = f(c)
        b = f(f(b))

    buf.write('(')
    buf.write(str((c * 10) // n))

    c = f(c)
    while b != c:
        buf.write(str((c * 10) // n))
        c = f(c)
    buf.write(')')

    return buf.getvalue()


class TestFractionString(unittest.TestCase):
    def test_00(self):
        self.assertEqual(fraction_string(7), '0.(142857)')

    def test_01(self):
        self.assertEqual(fraction_string(137), '0.(00729927)')


if __name__ == '__main__':
    unittest.main()
