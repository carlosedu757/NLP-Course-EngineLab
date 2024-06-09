# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:21:16 2024

@author: cerpc
"""

import re

sentence = "I love Avengers Avengers"

print(re.sub(r"Avengers", "Justice League", sentence))

print(re.sub(r"[a-z]", "0", sentence, 5, flags = re.I))