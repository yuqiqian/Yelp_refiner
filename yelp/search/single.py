'''
Created on 2015-4-3

@author: Lyle
'''
import nltk
import json
import random
from nltk import *
from nltk.util import ngrams
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from math import log
from os import listdir
import re
import string
import operator
from nltk.corpus.europarl_raw import english

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def _generate_candidate_keywords(sentences):
    phrase_list = []
    for sentence in sentences:
        words = map(lambda x: "|" if x in nltk.corpus.stopwords.words() else x, nltk.word_tokenize(sentence.lower()))
        phrase = []
        for word in words:
            if word == "|" or isPunct(word):
                if len(phrase) > 0:
                    temp = ' '.join(phrase)
                    phrase_list.append(temp)
                    phrase = []
            else:
                phrase.append(word)
    return phrase_list

def listkeywords(target):
    corpus_dir = 'reviews.json'
    corpus = {}
    f = open(corpus_dir,encoding='utf-8')
    object = json.load(f)
    reviews = {}
    review = object[0]['name']
    for i in range(0, len(object)):
        if (i+1) < len(object) and object[i+1]['id'] == object[i]['id']:
            review += ' ' + object[i+1]['name']
        else:
            review = review.replace('.', '. ')
            reviews[object[i]['id']] = review
            if (i+1) < len(object):
                review = object[i+1]['name']

    sentences = nltk.sent_tokenize(reviews[target])
    words = _generate_candidate_keywords(sentences)
    corpus[target] = words
    for i in range(0, 10):
        a = random.randint(0, len(reviews))
        id = list(reviews.keys())[a]
        temp = reviews[id]
        sentences = nltk.sent_tokenize(temp)
        words = _generate_candidate_keywords(sentences)
        corpus[id] = words

    cfd = ConditionalFreqDist(
                              (topic, word)
                              for topic in corpus.keys()
                              for word in corpus[topic])

    df = {}
    topics = cfd.conditions()
    sum_topics = len(topics)
    for topic in topics:
        for k in cfd[topic].keys():
            if k not in df:
                df[k] = 0
            df[k] += 1
        
    topic_tf_idf = {}
    for topic in topics:
        if topic not in topic_tf_idf:
            topic_tf_idf[topic] = {}
        sum_tf = len(corpus[topic])
        for k, v in cfd[topic].items():
            topic_tf_idf[topic][k] = float(v) / sum_tf * log(float(sum_topics)/df[k])

    keywordslist = []
    i = 0
    for k,v in sorted(topic_tf_idf[target].items(), key = lambda x:x[1], reverse = True):
        i += 1
        keywordslist.append(k)
        if i >= 10:
            break
    
    return keywordslist