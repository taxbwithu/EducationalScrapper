#!/usr/bin/env python
# -*-coding:utf-8 -*
"""mapper.py"""
import sys
import re 


for line in sys.stdin:

# mapper rok licznik 
# "title,duration,rating,year,director,votes_number":
        
    s = line.strip()
    words = re.split(',', s)
    
    res = []
    if words[-3] != "year":
        res.append(words[-3])

    for word in res:
        print('%s\t%s' % (word, 1))
