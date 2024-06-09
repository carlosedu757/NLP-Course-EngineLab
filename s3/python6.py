# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:59:12 2024

@author: cerpc
"""

tuple1 = (12, "This is a string", 13, 8, "Another string")
tuple2 = (50, 90, 2)

print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

tuple3 = tuple1 + tuple2

print(len(tuple3))

for i in range(0, len(tuple3)):
    print(tuple3[i])
    
for item in tuple3:
    print(item)