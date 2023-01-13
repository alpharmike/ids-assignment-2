# your code (nasa_reducer2.py)
import sys

current_activity = 0
current_mean = 0
current_total = 0
activity = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    activity, exec_time = line.split('\t')

    # convert count (currently a string) to int
    try:
        exec_time = int(exec_time)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_activity == activity:
        current_mean = (current_total * current_mean + exec_time) / (current_total + 1)
        current_total += 1
        current_activity = activity
    else:
        if current_activity:
            # write result to STDOUT
            print(f'{current_activity}\t{current_mean}')
        current_mean = exec_time
        current_activity = activity
        current_total = 1

# do not forget to output the last word if needed!
if current_activity == activity:
    print(f'{current_activity}\t{current_mean}')
