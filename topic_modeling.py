# topic_modeling.py

from gensim import corpora, models

def build_lda_model(tokenized_texts, num_topics=5, passes=10):
    dictionary = corpora.Dictionary(tokenized_texts)
    corpus = [dictionary.doc2bow(text) for text in tokenized_texts]
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
    return lda_model, corpus, dictionary

def print_topics(lda_model):
    topics = lda_model.print_topics()
    for idx, topic in topics:
        print(f"Topic {idx}: {topic}")
