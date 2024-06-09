# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:51:02 2024

@author: cerpc
"""
import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~% +++--- arrived at @Jack's place. #fun"
sentence3 = "I                love                you"

sentence1_modified = re.sub(r"\d", "", sentence1)
sentence2_modified = re.sub(r"[@%#~+\-\.\']", "", sentence2) # correction \-

sentence2_modified = re.sub(r"\W", " ", sentence2) #a-zA-Z0-9 == \w (\W == complemento)
sentence2_modified = re.sub(r"\s+", " ", sentence2_modified) # sequencia de espaços
sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+", " ", sentence2_modified)

sentence3_modified = re.sub(r"\s+love\s+"," hate ", sentence3)
