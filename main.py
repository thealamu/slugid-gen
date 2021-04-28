import string
import sys
from random import choice

sample_space = [c for c in string.ascii_letters] + [str(n) for n in range(10)]


def create_slug_id(length: int):
    slug_id = ""
    for _ in range(length):
        slug_id += choice(sample_space)
    return slug_id


if __name__ == "__main__":
    length = 4
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    print(create_slug_id(length))
