# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:44:20 2022

@author: CrIva
"""
from collections import deque

numbers = deque()
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

last_item = numbers.pop()
print(last_item) 
print(numbers) 

first_item = numbers.popleft()
print(first_item) 
print(numbers) 