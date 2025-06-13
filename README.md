# arxiv-mcp

An MCP server for searching arXiv.

## Installation

TODO: this uses uv, so it can be directly run.

## Usage

To run the server, execute the following command:

```bash
# Dev mode, brings up the MCP inspector
uv run mcp dev mcp_server.py
```

The server will start and be available for MCP clients.

## Tools

The following tools are available:

### `search_papers`

Search for papers on arXiv.

**Parameters:**

*   `query` (str): The search query.
*   `max_results` (int, optional): The maximum number of results to return. Defaults to 10.

### `get_paper`

Get detailed information about a specific paper.

**Parameters:**

*   `paper_id` (str): The ID of the paper to retrieve.
