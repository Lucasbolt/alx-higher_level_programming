#!/usr/bin/python3
import sys

status = [200, 301, 400, 401, 404, 405, 500]
stats_count = {200:0, 301:0, 400:0, 401:0, 404:0, 405:0, 500:0}
file_size = 0
count = 0

while(True):
    line = sys.stdin.readline()
    if not bool(line):
        break
    if count == 10 or line == KeyboardInterrupt:
        print('File size: {}'.format(file_size))
        for key in stats_count:
            print(key, ': ', stats_count[key])
            stats_count[key] = 0
        count = 0
        file_size = 0 
    line = line.split()
    stcode = int(line[-2])
    if stcode in status:
        stats_count[stcode] += 1
        file_size += int(line[-1])
        count += 1
    else:
        continue
