#!/usr/bin/env python3

"""Perform simple command-line based calculations."""

import sys
from math import *  # noqa
from pathlib import Path

last_path = Path("~/.config/calculon.last").expanduser()
precision = 1e-10


def estimate_decimals(res):
    if isinstance(res, int) or abs(int(res) - res) < 1e-9:
        return 0
    for i in range(9):
        if (res * 10**i) % 1 < precision:
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
        print(f"\t\t= {res:.{estimate_decimals(res)}f}")
    except SyntaxError:
        print("\t\tError", query)


if __name__ == "__main__":
    main("".join(sys.argv[1:]))
