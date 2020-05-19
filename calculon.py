#!/usr/bin/env python3

"""Perform simple command-line based calculations."""

from __future__ import division
import sys
from math import *


def estimate_decimals(res):
    if isinstance(res, int) or abs(int(res) - res) < 1e-9:
        return 0
    for i in range(9):
        if (res * 10 ** i) % 1 == 0.0:
            return i
    return 9


def main(query=None):
    query = (
        query.replace("[", "(").replace("]", ")").replace("^", "**").replace("x", "*")
    )
    try:
        res = eval(query)
        print("\t\t= {:.{}f}".format(res, estimate_decimals(res)))
    except SyntaxError:
        print("\t\tError", query)


if __name__ == "__main__":
    main("".join(sys.argv[1:]))
