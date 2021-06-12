 #!/usr/bin/env python
# -*-coding:utf-8 -*
"""reducer.py"""

from operator import itemgetter
import sys

current_decade = 0
current_rating = 0
current_count = 0
decade = 0
year = 0

for line in sys.stdin:

    line = line.strip()
    year, rating = line.split('\t', 1)
    
    try:
        rating = float(rating)
    except ValueError:
        continue
    try:
        year = int(year)
    except ValueError:
        continue
    
    decade = year - (year%10)
     
    if current_decade == decade:
        current_rating += rating
        current_count += 1
    else:
        if current_decade:
            current_count += 1
            avg = current_rating/current_count
            print('%s,%s' % (current_decade, avg))

        current_rating = rating
        current_decade = decade
        current_count = 0

# if current_decade == decade:
#    print('%s,%s' % (current_decade, current_count))

