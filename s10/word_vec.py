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
from nltk.corpus import stopwords
nltk.download('stopwords')

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup = bs.BeautifulSoup(source,'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    
    
# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)

words = model.wv.vocab

# Finding Word Vectors
vector = model.wv['global']

# Most similar words
similar = model.wv.most_similar('global')