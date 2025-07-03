# cli.py

import argparse
import json
from preprocessing import preprocess
from topic_modeling import build_lda_model, print_topics
from recommendation_engine import generate_recommendations
from trend_analysis import build_trend_dataframe
from novelty_detection import detect_novel_topics
from visualize import plot_topic_trends

def main():
    parser = argparse.ArgumentParser(description="Research Topic Recommender CLI")
    parser.add_argument("--data", type=str, default="arxiv_papers.json", help="Path to data JSON")
    parser.add_argument("--topics", type=int, default=5, help="Number of LDA topics")
    args = parser.parse_args()

    with open(args.data, "r", encoding="utf-8") as f:
        papers = json.load(f)

    print("Preprocessing...")
    texts = [preprocess(p["summary"]) for p in papers]

    print("Building LDA model...")
    lda_model, corpus, dictionary = build_lda_model(texts, num_topics=args.topics)
    print_topics(lda_model)

    print("Assigning dominant topic to each document...")
    topic_assignments = [max(lda_model[doc], key=lambda x: x[1])[0] for doc in corpus]

    trend_df = build_trend_dataframe(papers, topic_assignments)
    plot_topic_trends(trend_df)

    novelty = detect_novel_topics(trend_df)
    recommendations = generate_recommendations(novelty, lda_model)

    print("\nTop Recommendations:")
    for rec in recommendations:
        print(f"\nTopic {rec['topic_id']} ({rec['score']}): {rec['keywords']}\nJustification: {rec['justification']}")

if __name__ == "__main__":
    main()
