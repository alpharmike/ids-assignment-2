#!/usr/bin/env python
"""mapper1.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    activity, timestamp, lifecycle_trans, exec_id = line.split("\t")
    print("%s\t%s\t%s" % (exec_id, activity, timestamp))