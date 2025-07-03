# trend_analysis.py

import pandas as pd

def build_trend_dataframe(papers, topic_assignments):
    # papers: list of dicts with 'published'
    # topic_assignments: list of topic indices
    data = []
    for paper, topic in zip(papers, topic_assignments):
        data.append({"date": paper["published"], "topic": topic})
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["year_month"] = df["date"].dt.to_period("M")
    trend = df.groupby(["year_month", "topic"]).size().unstack(fill_value=0)
    return trend
