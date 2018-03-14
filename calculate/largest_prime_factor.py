# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:59:17 2018

@author: ODsLaptop
"""

import math

def isPrime(number):
    if number == 2:
        return True
    elif (number % 2 == 0) or number <= 1:
        return False

    sqroot = int(math.sqrt(number)) + 1

    for divisor in range(3, sqroot, 2):
        if number % divisor == 0:
            return False
    return True
    
def largestPrimeFactor(n):
    for divisor in range((n/2), 1, -1):
        if n%divisor == 0 and isPrime(divisor) == True:
            return "largest prime factor:", divisor
            break
    return "No prime factors"
            
print largestPrimeFactor(56234)