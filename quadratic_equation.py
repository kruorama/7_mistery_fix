from math import sqrt
import sys
import argparse


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None

    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)

    if discriminant == 0:
        return root1, None
    else:
        return root1, root2

def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input numerical coefficients')

    parser.add_argument(
        '-a',
        help='First coefficient',
        type=float,
        required=True)

    parser.add_argument(
        '-b',
        help='Second coefficient',
        type=float,
        required=True)

    parser.add_argument(
        '-c',
        help='Third coefficient',
        type=float,
        required=True)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_parser_args()
    a = args.a
    b = args.b
    c = args.c

    print(get_roots(a, b, c))
