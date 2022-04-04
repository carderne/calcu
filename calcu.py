#!/usr/bin/env python3

"""Perform simple command-line based calculations."""

import sys
from math import *  # noqa
from pathlib import Path

__version__ = "0.9.7"

last_path = Path("~/.config/calcu.last").expanduser()
precision = 1e-10


def estimate_decimals(res):
    if isinstance(res, int) or abs(int(res) - res) < 1e-9:
        return 0
    for i in range(9):
        if (res * 10**i) % 1 < precision:
            return i
    return 9


def load_last():
    try:
        with last_path.open() as f:
            return str(float(f.read().strip()))
    except FileNotFoundError:
        return ""


def dump_last(res):
    with last_path.open("w") as f:
        print(res, file=f)


def main(query=""):
    last = load_last()
    query = (
        query.replace("[", "(")
        .replace("]", ")")
        .replace("^", "**")
        .replace("x", "*")
        .replace("_", last)
    )
    try:
        res = eval(query)
        dump_last(res)
        print(f"\t\t= {res:,.{estimate_decimals(res)}f}")
    except (SyntaxError, NameError) as e:
        print("\t\tError", e)


def cli():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print(__version__)
        else:
            main("".join(sys.argv[1:]))


if __name__ == "__main__":
    cli()
