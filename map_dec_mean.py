#!/usr/bin/env python
# -*-coding:utf-8 -*
"""mapper.py"""
import sys
import re 

for line in sys.stdin:

# mapper rok ocena filmu
# "title,duration,rating,year,director,votes_number"
        
    s = line.strip()
    words = re.split(',', s)
    
    years = None
    rating = None
    
    if words[-3] != 'year':
        years = words[-3]
    if words[-4] != 'rating':
        rating = words[-4]
        
    if (years != None and rating != None):
        print('%s\t%s' % (years, rating))
