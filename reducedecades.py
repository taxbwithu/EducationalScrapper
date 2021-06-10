#!/usr/bin/env python
# -*-coding:utf-8 -*
"""reducer.py"""

from operator import itemgetter
import sys

current_decade = 0
current_count = 0
decade = 0
year = 0
word = None

for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)
    if word == "year":
        continue
    else:
        try:
            count = int(count)
        except ValueError:
            continue
        try:
            year = int(word)
        except ValueError:
            continue
            
        
        decade = year - (year%10)
        
        if current_decade == decade:
            current_count += count
        else:
            if current_decade:
                print('%s,%s' % (current_decade, current_count))

            current_count = count
            current_decade = decade

if current_decade == decade:
    print('%s,%s' % (current_decade, current_count))

