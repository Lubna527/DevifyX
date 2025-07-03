# visualize.py

import matplotlib.pyplot as plt

def plot_topic_trends(trend_df):
    trend_df.plot(figsize=(12,6))
    plt.title("Topic Frequency Over Time")
    plt.xlabel("Time")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
