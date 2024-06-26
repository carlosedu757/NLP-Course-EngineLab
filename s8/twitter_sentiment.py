# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:42:22 2024

@author: cerpc
"""

import tweepy
import re
import pickle

from tweepy import OAuthHandler

#Initializing the keys

consumer_key = 'vIrA4Y8go5YXIGMXuNRLdhgzy'
consumer_secret = '44MdlTfiGKEMPwjkcHe2R1yVcD27FVJPciI5rK4juTv29SWOeU'
access_token = '2804777890-Me0MeIjm3UnsnVYK4sIOwHgVovKSo7fQhwRI1iE'
access_secret = 't33GHh9koyTtkaeOR8JMfe9LxqgEtTBRZ6Q7WDb6PzvxW'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
args = ['facebook']
api = tweepy.API(auth, timeout = 10)

list_tweets = []

query = args[0]
if len(args) == 1:
    for status in tweepy.Cursor(api.search_tweets, q = query + " -filter:retweets", lang = 'en', result_type = 'recent').items(100):
        list_tweets.append(status.text)
# DEU RUIM POR CONTA DA COMPRA DO ELON MUSK, MUDOU PARA X E AGORA A API SÓ PERMITE AUTENTICAÇÃO E CRIAÇÃO DE TWEETS

with open('tfidf.pickle', 'rb') as f:
    vectorizer = pickle.load(f)        

with open('classifier.pickle', 'rb') as f:
    clf = pickle.load(f)
    
clf.predict(vectorizer.transform(['You are a nice person man, have a good life']))

total_pos = 0
total_neg = 0

for tweet in list_tweets:
    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", tweet)
    tweet = tweet.lower()
    tweet = re.sub(r"that's","that is",tweet)
    tweet = re.sub(r"there's","there is",tweet)
    tweet = re.sub(r"what's","what is",tweet)
    tweet = re.sub(r"where's","where is",tweet)
    tweet = re.sub(r"it's","it is",tweet)
    tweet = re.sub(r"who's","who is",tweet)
    tweet = re.sub(r"i'm","i am",tweet)
    tweet = re.sub(r"she's","she is",tweet)
    tweet = re.sub(r"he's","he is",tweet)
    tweet = re.sub(r"they're","they are",tweet)
    tweet = re.sub(r"who're","who are",tweet)
    tweet = re.sub(r"ain't","am not",tweet)
    tweet = re.sub(r"wouldn't","would not",tweet)
    tweet = re.sub(r"shouldn't","should not",tweet)
    tweet = re.sub(r"can't","can not",tweet)
    tweet = re.sub(r"couldn't","could not",tweet)
    tweet = re.sub(r"won't","will not",tweet)
    tweet = re.sub(r"\W"," ",tweet)
    tweet = re.sub(r"\d"," ",tweet)
    tweet = re.sub(r"\s+[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+[a-z]$"," ",tweet)
    tweet = re.sub(r"^[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+"," ",tweet)
    sent = classifier.predict(tfidf.transform([tweet]).toarray())
    if sent[0] == 1:
        total_pos += 1
    else:
        total_neg += 1


# Visualizing the results
import matplotlib.pyplot as plt
import numpy as np
objects = ['Positive','Negative']
y_pos = np.arange(len(objects))

plt.bar(y_pos,[total_pos,total_neg],alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Number')
plt.title('Number of Postive and NEgative Tweets')

plt.show()

