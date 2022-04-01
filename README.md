# calcu
A simple calculator for your CLI.

(It uses Python's `eval()` and spits out the result, with some prettifying.)

![example-gif](usage.gif)

## Installation
```bash
pip install calcu
```

## Usage
Type `c` followed by your expression.

Example:
```bash
c 2+2
             = 4
```

Refer to the result of the previous calculation with an underscore `_`:
```bash
c _+10
             = 14
```

Do multiplication and exponentiation:
```bash
c 2 x 3^2
             = 18
# you can also use * and ** but then you must
# wrap your expression in quotes ' ' or bash will mess it up
# eg: c '2*3**2'
```

And dividing and brackets:
```bash
c [2+10]/10
             = 1.2
# as above, the square brackets are to stop bash cleverness
# if you want to use regular brackets, use quotes
# eg: c '(2+10)/10
```

Use any function from Python's `math` library:
```bash
c log[e] x pi
             = 3.141592654
```

It returns the appropriate number of decimal values, up to 9.
