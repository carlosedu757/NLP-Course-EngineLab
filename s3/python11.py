# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:45:09 2024

@author: cerpc
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newNumbers = []
for number in numbers:
    newNumbers.append(number)
    
newNumbers = [number for number in numbers]

numbers2 = [1, 3, 5, 2, 9]

newNumbers = [number for number in numbers if number <= 5]

newNumbers = [number*2 for number in numbers]
newNumbers = [number for number in numbers if number % 2 == 1]

squareGen = (number**2 for number in numbers)
list(squareGen)

myDict = {"apple": 1, "orange": 4, "banana": 10}
newDict = {key: myDict[key] for key in myDict.keys()}

newDict = {key: myDict[key] for key in myDict.keys() if myDict[key] > 1}

words = ["I", "Love", "Avengers"]
sentence = ' '.join(words)
sentence = '.'.join(words)