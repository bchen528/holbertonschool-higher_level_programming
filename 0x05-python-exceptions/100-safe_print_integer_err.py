#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_print_integer_err(value):
    try:
        print("Exception: {:d}".format(value))
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type 'str'",
              file=sys.stderr)
        return False
    else:
        return True
