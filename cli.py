# cli.py
import json
import argparse
from data_collection import fetch_arxiv_papers
from topic_modeling import build_lda_model, assign_topics
from trend_analysis import build_topic_dataframe
from recommendation import generate_recommendations
from visualize import plot_trends

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true", help="Fetch new data")
    parser.add_argument("--topics", type=int, default=5, help="Number of topics")
    args = parser.parse_args()

    if args.collect:
        papers = fetch_arxiv_papers()
        with open("arxiv_papers.json", "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2)
        print("Fetched and saved papers.")
    else:
        with open("arxiv_papers.json", encoding="utf-8") as f:
            papers = json.load(f)

    texts = [p["summary"] for p in papers]
    lda, corpus, dictionary = build_lda_model(texts, num_topics=args.topics)
    dominant_topics = assign_topics(lda, corpus)
    df = build_topic_dataframe(papers, dominant_topics)

    print("\nRecommendations:\n")
    recs = generate_recommendations(df)
    for r in recs:
        print(f"Topic {r['topic']}: {r['justification']} (Count: {r['count']})")

    plot_trends(df)

if __name__ == "__main__":
    main()
