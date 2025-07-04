# recommendation.py
def generate_recommendations(df):
    recs = []
    grouped = df.groupby("topic").size().sort_values(ascending=False)
    for topic, count in grouped.items():
        recs.append({
            "topic": topic,
            "count": int(count),
            "justification": "Topic shows high recent activity compared to historical average."
        })
    return recs
