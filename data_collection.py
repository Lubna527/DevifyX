# data_collection.py
import arxiv
import json

def fetch_arxiv_papers(query="natural language processing", max_results=200):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending  # older first
    )
    papers = []
    for result in client.results(search):
        published_date = result.published.strftime("%Y-%m-%d") if result.published else None
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "published": published_date,
            "authors": [a.name for a in result.authors]
        })
    return papers

if __name__ == "__main__":
    data = fetch_arxiv_papers()
    with open("arxiv_papers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved arXiv papers to arxiv_papers.json")
