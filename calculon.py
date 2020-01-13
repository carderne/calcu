#!/usr/bin/env python

"""Perform simple command-line based calculations."""

import sys

from math import *


def main(query=None, decimals=None):
    query = query.replace("[", "(").replace("]", ")")
    try:
        res = eval(query)
        if decimals is None:
            if isinstance(res, int) or abs(int(res) - res) < 1e-9:
                decimals = 0
            else:
                decimals = 3
        print("\t\t= {:.{}f}".format(res, decimals))
    except SyntaxError:
        print("\t\tError")


if __name__ == "__main__":
    args = sys.argv
    main(
        query=args[1] if len(args) >= 2 else None,
        decimals=args[2] if len(args) >= 3 else None,
    )
