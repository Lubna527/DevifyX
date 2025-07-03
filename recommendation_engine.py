# recommendation_engine.py

def generate_recommendations(novelty_series, lda_model):
    recs = []
    for topic_id, score in novelty_series.items():
        terms = lda_model.show_topic(topic_id, topn=5)
        keywords = ", ".join([term for term, _ in terms])
        recs.append({
            "topic_id": topic_id,
            "score": round(score, 3),
            "keywords": keywords,
            "justification": f"Topic shows high recent activity compared to historical average."
        })
    return recs
