# visualize.py
import matplotlib.pyplot as plt

def save_trend_plot(df, filename):
    counts = df.groupby([df["published"].dt.to_period("M"), "topic"]).size().reset_index(name="count")
    counts["published"] = counts["published"].dt.to_timestamp()
    pivot = counts.pivot(index="published", columns="topic", values="count").fillna(0)
    plt.figure(figsize=(12,6))
    pivot.plot(ax=plt.gca())
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.title("Topic Frequency Over Time")
    plt.legend(title="Topic")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
