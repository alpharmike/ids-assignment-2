#!/usr/bin/env python
"""reducer1.py"""

import sys

current_exec_id = None
current_timestamp = 0.0
current_activity = 0
exec_id = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    exec_id, activity, timestamp = line.split('\t')

    # convert count (currently a string) to int
    try:
        timestamp = float(timestamp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_exec_id == exec_id:
        # This will actually be the execution time (absolute difference between the start and complete timestamps)
        current_timestamp = abs(current_timestamp - timestamp)
        current_activity = activity
    else:
        if current_exec_id:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_exec_id, current_activity, current_timestamp))
        current_timestamp = timestamp
        current_exec_id = exec_id
        current_activity = activity

# do not forget to output the last word if needed!
if current_exec_id == exec_id:
    print('%s\t%s\t%s' % (current_exec_id, current_activity, current_timestamp))
