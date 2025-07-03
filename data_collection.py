# data_collection.py

import arxiv
import json

def fetch_arxiv_papers(query="natural language processing", max_results=100):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "published": result.published.strftime("%Y-%m-%d"),
            "authors": [a.name for a in result.authors]
        })
    return papers

if __name__ == "__main__":
    data = fetch_arxiv_papers()
    with open("arxiv_papers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved arXiv papers to arxiv_papers.json")