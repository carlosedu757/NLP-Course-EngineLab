# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:01:12 2024

@author: cerpc
"""

dict1 = {}

dict1['apple'] = "Apple is a fruit"
dict1['orange'] = "Orange is a fruit"
dict1['car'] = "Cars are fast"
dict1['python'] = "I Love Python"

print(dict1)
print(dict1['apple'])
print(dict1['orange'])
print(dict1['car'])

print(dict1.get("apple", "Key doesn't exist"))

del dict1['apple']

print(len(dict1))

listOfKeys =list(dict1.keys())
listOfValues = list(dict1.values())

for key in dict1.keys():
    print(dict1[key])
    
for value in dict1.values():
    print(value)