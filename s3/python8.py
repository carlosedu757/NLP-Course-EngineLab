# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:26:36 2024

@author: cerpc
"""

inp = input("Enter a number: ")
number1 = int(inp)

inp = input("Enter a number: ")
number2 = int(inp)

print(number1 + number2)

inp = input("Enter some text: ")

with open("textFile.txt", "w") as f:
    f.write(inp)
    
with open("textFile.txt", "a") as f:
    f.write(inp)
    
with open("textFile.txt", "r") as f:
    print(f.read())
