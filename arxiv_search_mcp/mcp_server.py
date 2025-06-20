import arxiv
import itertools
import logging

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

logging.basicConfig(level=logging.DEBUG)

mcp = FastMCP("arxiv-search-mcp")

client = arxiv.Client(page_size=5, delay_seconds=3, num_retries=3)

@mcp.tool()
def search_papers(query: str, page: int = 1, page_size: int = 5):
    """
    Search for papers on arXiv with pagination.

    This tool searches for papers on arXiv based on a query string. It supports pagination to browse through the search results.

    The search results are sorted by the submission date, with the most recent papers appearing first.

    If timeouts occur, consider requesting fewer results and paging through them.

    Each paper in the returned list is a dictionary containing the following fields:
    - id: The paper's unique arXiv ID.
    - title: The title of the paper.
    - summary: A brief summary of the paper.
    - authors: A list of the paper's authors.
    - published: The publication date of the paper in ISO format.
    - updated: The date the paper was last updated in ISO format.
    - pdf_url: The URL to the PDF version of the paper.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    search = arxiv.Search(
        query=query,
        max_results=end_index,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results_generator = client.results(search)

    paginated_results = itertools.islice(results_generator, start_index, end_index)

    results = []
    for r in paginated_results:
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

    This tool retrieves detailed information for a single paper from arXiv, identified by its unique ID.

    The returned dictionary contains the following fields:
    - id: The paper's unique arXiv ID.
    - title: The title of the paper.
    - summary: A brief summary of the paper.
    - authors: A list of the paper's authors.
    - published: The publication date of the paper in ISO format.
    - updated: The date the paper was last updated in ISO format.
    - pdf_url: The URL to the PDF version of the paper.
    - categories: A list of categories the paper belongs to.
    - comment: Any comments associated with the paper.
    - journal_ref: The journal reference for the paper, if available.
    - doi: The Digital Object Identifier (DOI) for the paper, if available.
    - primary_category: The primary category of the paper.
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
