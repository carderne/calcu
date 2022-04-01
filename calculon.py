#!/usr/bin/env python3

"""Perform simple command-line based calculations."""

from __future__ import division
import sys
from math import *
from pathlib import Path

last_path = Path("~/.config/calculon.last").expanduser()


def estimate_decimals(res):
    if isinstance(res, int) or abs(int(res) - res) < 1e-9:
        return 0
    for i in range(9):
        if (res * 10 ** i) % 1 == 0.0:
            return i
    return 9


def main(query=None):
    try:
        with last_path.open() as f:
            last = str(float(f.read().strip()))
    except FileNotFoundError:
        last = ""
    query = (
        query.replace("[", "(")
        .replace("]", ")")
        .replace("^", "**")
        .replace("x", "*")
        .replace("_", last)
    )
    try:
        res = eval(query)
        with last_path.open("w") as f:
            print(res, file=f)
        print("\t\t= {:.{}f}".format(res, estimate_decimals(res)))
    except SyntaxError:
        print("\t\tError", query)


if __name__ == "__main__":
    main("".join(sys.argv[1:]))
