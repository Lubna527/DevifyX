# trend_analysis.py
import pandas as pd

def build_topic_dataframe(papers, dominant_topics):
    df = pd.DataFrame(papers)
    df["published"] = pd.to_datetime(df["published"], errors="coerce")
    df["topic"] = dominant_topics
    df = df.dropna(subset=["published"])
    return df
