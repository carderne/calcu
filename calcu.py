#!/usr/bin/env python3

"""Perform simple command-line based calculations."""

import sys
from math import *  # noqa
from pathlib import Path
from typing import Any

__version__ = "0.9.9"

last_path = Path("~/.config/calcu.last").expanduser()
PRECISION = 1e-10


def estimate_decimals(res: float) -> int:
    """Estimate number of decimals to show."""
    if isinstance(res, int) or abs(int(res) - res) < 1e-9:
        return 0
    for i in range(9):
        if (res * 10**i) % 1 < PRECISION:
            return i
    return 9


def load_last() -> str:
    """Load saved value from previous run."""
    try:
        with last_path.open("r") as file:
            return str(float(file.read().strip()))
    except FileNotFoundError:
        return ""


def dump_last(res: Any) -> None:
    """Save value to file."""
    with last_path.open("w") as file:
        print(res, file=file)


def main(query: str = "") -> None:
    """Evaluate query and print result."""
    last = load_last()
    query = (
        query.replace("[", "(")
        .replace("]", ")")
        .replace("^", "**")
        .replace("x", "*")
        .replace("_", last)
    )
    try:
        res = eval(query)  # pylint: disable=eval-used
        dump_last(res)
        print(f"\t\t= {res:,.{estimate_decimals(res)}f}")
    except (SyntaxError, NameError) as ex:
        print("\t\tError", ex)


def cli() -> None:
    """CLI entrypoint."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print(__version__)
        else:
            main("".join(sys.argv[1:]))


if __name__ == "__main__":
    cli()
