import sys

from fraction import fraction_string


def main():
    for n in range(2, int(sys.argv[1])):
        print('1/{} = {}'.format(n, fraction_string(n)))


if __name__ == '__main__':
    main()
