# preprocessing.py

import nltk
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("stopwords")

def preprocess(text):
    stop_words = set(stopwords.words("english"))
    tokens = nltk.word_tokenize(text)
    tokens = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stop_words]
    return tokens
