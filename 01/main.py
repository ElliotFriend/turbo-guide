#!/usr/bin/env python

import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

SAMPLE_DATA = True

contents = None
with open(os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'), 'r') as f:
    contents = f.read().splitlines()
