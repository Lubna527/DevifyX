# app.py
from flask import Flask, render_template
import json
from data_collection import fetch_arxiv_papers
from topic_modeling import build_lda_model, assign_topics
from trend_analysis import build_topic_dataframe
from recommendation import generate_recommendations
from visualize import save_trend_plot

app = Flask(__name__)

@app.route("/")
def index():
    # Load data
    with open("arxiv_papers.json", encoding="utf-8") as f:
        papers = json.load(f)

    texts = [p["summary"] for p in papers]

    # Topic modeling
    lda, corpus, dictionary = build_lda_model(texts, num_topics=5)
    dominant_topics = assign_topics(lda, corpus)

    # DataFrame
    df = build_topic_dataframe(papers, dominant_topics)

    # Recommendations
    recs = generate_recommendations(df)

    # Save plot
    save_trend_plot(df, "static/topic_trends.png")

    # Top keywords for each topic
    topic_keywords = []
    for i in range(5):
        terms = lda.show_topic(i, topn=5)
        topic_keywords.append({"topic": i, "keywords": [word for word, prob in terms]})

    return render_template(
        "index.html",
        recommendations=recs,
        topic_keywords=topic_keywords,
        plot_path="static/topic_trends.png"
    )

if __name__ == "__main__":
    app.run(debug=True)
