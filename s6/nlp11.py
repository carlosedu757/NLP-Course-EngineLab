# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:16:42 2024

@author: cerpc
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

dataset = [line.lower() for line in dataset]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

print(X[0])

lsa = TruncatedSVD(n_components = 4, n_iter = 100)

lsa.fit(X)

row1 = lsa.components_[0]

concept_words = {}
terms = vectorizer.get_feature_names_out()

for i, comp in enumerate(lsa.components_):
  componentTerms = zip(terms, comp)
  sortedTerms = sorted(componentTerms, key = lambda x:x[1], reverse = True)
  sortedTerms = sortedTerms[:10]
  concept_words["Concept" + str(i)] = sortedTerms

print(concept_words)

for key in concept_words.keys():
  sentence_scores = []
  for sentence in dataset:
    words = nltk.word_tokenize(sentence)
    score = 0
    for word in words:
      for word_with_score in concept_words[key]:
        if word == word_with_score[0]:
          score += word_with_score[1]
    sentence_scores.append(score)
  print("\n" + key + ":")
  for sentence_score in sentence_scores:
    print(sentence_score)