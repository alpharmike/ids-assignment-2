#!/usr/bin/env python
"""mapper1.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    activity, timestamp, lifecycle_trans, exec_id = line.split("\t")
    print(f"{exec_id}\t{activity}\t{timestamp}")