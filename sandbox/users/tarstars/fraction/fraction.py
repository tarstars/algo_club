import io
import unittest


def frying_pan(initial_value, step, accumulator):
    """Solves problem of determination of period and non-period parts of the sequence
    initial_value, step(initial_value), step(step(initial_value)), ...

    :param initial_value: first element in the sequence
    :param step: function that moves us toward in sequence
    :param accumulator: callable object that gathers information
    :return:
    """
    a = step(initial_value)
    b = step(a)

    while a != b:
        a = step(a)
        b = step(step(b))

    c = initial_value
    accumulator.start()
    while b != c:
        accumulator.process_value(c)
        c = step(c)
        b = step(b)

    accumulator.begin_period()
    accumulator.process_value(c)

    c = step(c)
    while b != c:
        accumulator.process_value(c)
        c = step(c)
    accumulator.finish()


class StringAccumulator:
    """Allows to accumulate results of division in form "0.<non periodic part> (<periodic part>)"

    """
    def __init__(self, digit_extractor):
        self.buf = io.StringIO()
        self.digit_extractor = digit_extractor

    def process_value(self, val):
        self.buf.write(str(self.digit_extractor(val)))

    def start(self):
        self.buf.write('0.')

    def begin_period(self):
        self.buf.write('(')

    def finish(self):
        self.buf.write(')')

    def getvalue(self):
        return self.buf.getvalue()


def fraction_string(n: int) -> str:
    """For values n greater than 1 this function calculates decimal
    representation of 1/n fraction and puts it in string

    :param n: denominator of fraction
    :return: string with decimal fraction representation 0.<non periodic part> (<periodic part>)
    """

    def next_reminder(r):
        return (r * 10) % n

    def current_digit(r):
        return str((r * 10) // n)

    string_accumulator = StringAccumulator(digit_extractor=current_digit)
    frying_pan(initial_value=1, step=next_reminder, accumulator=string_accumulator)

    return string_accumulator.getvalue()


class TestFractionString(unittest.TestCase):
    def test_00(self):
        self.assertEqual(fraction_string(7), '0.(142857)')

    def test_01(self):
        self.assertEqual(fraction_string(14), '0.0(714285)')

    def test_02(self):
        self.assertEqual(fraction_string(137), '0.(00729927)')


if __name__ == '__main__':
    unittest.main()
