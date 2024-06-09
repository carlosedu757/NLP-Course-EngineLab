# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:49:43 2024

@author: cerpc
"""

list1 = [12, 12, "This is a string"]


print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

list1.append(50)
list1.insert(0, "String number 1")


list1[1] = 20

list1.pop()
del list1[2]

print(len(list1))

for index in range(0, len(list1) - 1):
    print(list1[index])
    
for index in range(0, len(list1) - 1):
    list1[index] = 12
    
for item in list1:
    print(item)