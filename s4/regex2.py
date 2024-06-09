# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:17:51 2024

@author: cerpc
"""

import re

sentence = "1996 was the year when I died"

re.match(r"[a-zA-Z]+", sentence)

re.search(r"[a-zA-Z]+", sentence)

# Starts With
if re.match(r"^1996", sentence):
    print("Match")
else:
    print("No match")
    
#End With

if re.search(r"born$", sentence):
    print("Match")
else:
    print("No match")
    