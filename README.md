# arxiv-search-mcp

An MCP server for searching arXiv.

## Installation

Install the package directly with PyPI.

```bash
pip install arxiv-search-mcp
```

Once installed in your agent's environment, you can load it with the settings in
[`sample_settings.json`](./sample_settings.json).

## Usage

Once installed, you can run the server module directly.

```bash
python -m arxiv_search_mcp
```

To run the server using the MCP inspector, execute the following command.

```bash
uv run mcp dev arxiv_search_mcp/mcp_server.py
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

