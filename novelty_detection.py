# novelty_detection.py

def detect_novel_topics(trend_df, threshold_recent=3):
    # threshold_recent: how many most recent periods to consider
    recent_periods = trend_df.tail(threshold_recent)
    recent_totals = recent_periods.sum()
    overall_totals = trend_df.sum()
    
    novelty_scores = (recent_totals / (overall_totals + 1))
    ranked = novelty_scores.sort_values(ascending=False)
    return ranked
