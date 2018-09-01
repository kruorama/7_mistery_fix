from math import sqrt
import sys


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


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    print(get_roots(a, b, c))
