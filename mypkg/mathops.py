# -*- coding: utf-8 -*-
from __future__ import division, print_function

def add(a, b):
    return a + b

def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
