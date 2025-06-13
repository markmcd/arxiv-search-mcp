import arxiv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("arxiv-mcp")

client = arxiv.Client()

@mcp.tool()
def search_papers(query: str, max_results: int = 10):
    """
    Search for papers on arXiv.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    results = []
    for r in client.results(search):
        results.append({
            "id": r.entry_id,
            "title": r.title,
            "summary": r.summary,
            "authors": [str(author) for author in r.authors],
            "published": r.published.isoformat(),
            "updated": r.updated.isoformat(),
            "pdf_url": r.pdf_url,
        })
    return results

@mcp.tool()
def get_paper(paper_id: str):
    """
    Get detailed information about a specific paper.
    """
    search = arxiv.Search(id_list=[paper_id])
    try:
        paper = next(client.results(search))
        return {
            "id": paper.entry_id,
            "title": paper.title,
            "summary": paper.summary,
            "authors": [str(author) for author in paper.authors],
            "published": paper.published.isoformat(),
            "updated": paper.updated.isoformat(),
            "pdf_url": paper.pdf_url,
            "categories": paper.categories,
            "comment": paper.comment,
            "journal_ref": paper.journal_ref,
            "doi": paper.doi,
            "primary_category": paper.primary_category,
        }
    except StopIteration:
        return None


def main():
    mcp.run()


if __name__ == "__main__":
    main()

