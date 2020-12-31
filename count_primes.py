#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:00:47 2020

a function that returns the number of prime numbers
that exist up to and including a given number

@author: kjanjua
"""

def count_primes(num):
    if num < 2:
        return 0
    primes = [2] # initializing list for primes with first value
    x=3
    while x <= num:
        isPrime = True
        for y in range(3,x,2):
            if x%y == 0:
                # not a prime
                isPrime = False
                break
        if isPrime:
            primes.append(x)
        x += 2
        
    print(primes)
    return len(primes)

count_primes(100)

