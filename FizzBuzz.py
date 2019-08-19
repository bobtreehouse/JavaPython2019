# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:30:33 2019

@author: bobtr
"""

for num in range (1,100):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
        
        
        