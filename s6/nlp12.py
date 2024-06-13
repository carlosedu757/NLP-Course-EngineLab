# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:49:39 2024

@author: cerpc
"""

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
  for s in syn.lemmas():
    synonyms.append(s.name())
    for a in s.antonyms():
      antonyms.append(a.name())

print(set(synonyms))
print(set(antonyms))

