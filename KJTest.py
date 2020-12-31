#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 05:37:52 2020

@author: kjanjua
"""

import os

path = '/users/kjanjua/documents/logs/core-logs'

searchStr = 'ERROR The query has timed out'

os.chdir(path)

print(os.name, os.getcwd())
print(os.listdir())

with open('results.txt','w') as fw:
    for f in (os.listdir()):
        print('Searching file "{}" .....'.format(f))
        fw.write('Searching file {} for the string "{}".\n'.format(f, searchStr))
        with open(f,'r',encoding='utf-8') as f1:
            print(f1.read(40))
            print('-----------------------')



#with open('iOS-devices.txt','r') as f:
#    for line in f:
#       if '5c' in line.casefold():
#            print(line)
