#!/usr/bin/python

import sys
import itertools

plays = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    working_output = itertools.product(plays, repeat=n)
    output = []
    return [list(i) for i in working_output]
    # for i in working_output:
    #     output.append(list(i))
    # return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
