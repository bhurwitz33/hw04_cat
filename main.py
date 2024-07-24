#!/usr/bin/env python3

""" Tests for cat.py"""

import os
import string
import random
import re
from subprocess import getstatusoutput

PRG = './cat.py'

# --------------------------------------------------
def run(filenames, opts, expected):
    """ Run with a note """

    rv, out = getstatusoutput(f'{PRG} {" ".join(opts)} {" ".join(filenames)}')
    assert rv == 0
    assert out == expected