# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:12:23 2024

@author: cerpc
"""
import re

sentence = "I was born in the year 1996"
sentence = "b"

re.match(r".*", sentence)
re.match(r".+", sentence)

re.match(r"[a-zA-Z]+", sentence)

re.match(r"ab?", sentence)