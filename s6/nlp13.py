# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:49:50 2024

@author: cerpc
"""

import nltk
from nltk.corpus import wordnet

sentence = "I was not happy with the team's performance"

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""
for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""

    if word != "not":
        new_words.append(word)

sentence = ' '.join(new_words)