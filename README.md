# calcu
Simple, probably dangerous Python CLI calculator.  
(It uses `eval()` and spits out the result, with some prettifying.)

## Installation
Simply do the following to get going:

    git clone https://github.com/carderne/calcu.git
    ./calcu/install

This will install calcu to `~/.local/bin/calcu` and prompt you to add an alias for `c` to your `.bashrc` (or equivalent).

## Usage
Pass any valid Python expression (including all symbols from the `math` library) to the CLI to get a result back. Spaces are allowed. You can replace regular brackets with square brackets so that bash doesn't complain. You can use `^` instead of `**` for exponents. You can use `x` instead of `*` for multiplication. Or just wrap everything in quotes `"` `"`.

Examples:

    $ c 2 + 2
          = 4
    $ c 1 / 4
          = 0.25
    $ c sqrt[10] x 10
          = 31.622776602
    $ c log[e] x pi
          = 3.141592654

It returns the appropriate number of decimal values, up to 9.
