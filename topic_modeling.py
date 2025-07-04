# topic_modeling.py
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

STOPWORDS = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in STOPWORDS]
    return tokens

def build_lda_model(docs, num_topics=5):
    processed_docs = [preprocess(d) for d in docs]
    dictionary = corpora.Dictionary(processed_docs)
    corpus = [dictionary.doc2bow(d) for d in processed_docs]
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    return lda, corpus, dictionary

def assign_topics(lda, corpus):
    dominant_topics = []
    for doc_bow in corpus:
        topics = lda.get_document_topics(doc_bow)
        dominant = max(topics, key=lambda x: x[1])[0]
        dominant_topics.append(dominant)
    return dominant_topics
