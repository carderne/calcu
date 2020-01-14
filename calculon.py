#!/usr/bin/env python

"""Perform simple command-line based calculations."""

import sys

from math import *


def main(query=None):
    query = query.replace("[", "(").replace("]", ")").replace("^", "**")
    try:
        res = eval(query)
        if isinstance(res, int) or abs(int(res) - res) < 1e-9:
            decimals = 0
        else:
            decimals = 3
        print("\t\t= {:.{}f}".format(res, decimals))
    except SyntaxError:
        print("\t\tError")


if __name__ == "__main__":
    main("".join(sys.argv[1:]))
