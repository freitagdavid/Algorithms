#!/usr/bin/python

import sys
import itertools

plays = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    return [list(i) for i in itertools.product(plays, repeat=n)]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
