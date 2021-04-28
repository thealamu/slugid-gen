import string
import sys
from random import choice


def create_slug_id(length, sample_space=string.ascii_letters + string.digits):
    return "".join([choice(sample_space) for _ in range(length)])


if __name__ == "__main__":
    length = 4
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    print(create_slug_id(length))
