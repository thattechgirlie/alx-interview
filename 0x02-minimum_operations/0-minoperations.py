#!/usr/bin/python3
"""Minimum operations task"""


def minOperations(n):
    """
    text editor can execute only two operations
    in this file Copy All and Paste
    """
   
    if (n < 2):
        return 0
    Operation, polynomial = 0, 2
    while polynomial <= n:
        # if n evenly divides by root
        if n % polynomial == 0:
           
            Operation += polynomial
            
            n = n / polynomial
            
            polynomial -= 1
  
        polynomial += 1
    return Operation
