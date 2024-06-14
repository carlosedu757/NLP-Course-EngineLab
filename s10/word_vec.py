# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:10:28 2024

@author: cerpc
"""

import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup = bs.BeautifulSoup(source, 'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text