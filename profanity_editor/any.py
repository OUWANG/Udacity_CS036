#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 18:46:35 2018

@author: Austin
"""

def any(iterable):
    for element in iterable:
        if element==5:
            return True
    return False

testlist = [1,2,3,4,5,6,7]
print (any(testlist))