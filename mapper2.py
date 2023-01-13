#!/usr/bin/env python
"""mapper2.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    exec_id, activity, exec_time = line.split("\t")
    print(f"{activity}\t{exec_time}")