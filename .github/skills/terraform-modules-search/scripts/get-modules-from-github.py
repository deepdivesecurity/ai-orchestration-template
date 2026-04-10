# /// script
# dependencies = [
#   "httpx",
# ]
# ///

from tenacity import retry, stop_after_attempt, wait_random_exponential
import httpx
import base64
import os
from dotenv import load_dotenv

load_dotenv()

GH_TOKEN = os.getenv("GH_TOKEN")
GH_ORG = os.getenv("GH_ORG")
BASE_URL = os.getenv("BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

@retry(stop=stop_after_attempt(3), wait=wait_random_exponential(multiplier=1, min=4, max=10), reraise=True)
def _fetch_repository_page(query: str, org: str, page: int, client: httpx.Client) -> list: 
    """Fetch a single page of repository results with retry logic.
    
    Args:
        query (str): GitHub search query.
        org (str): GitHub organization name.
        page (int): Page number to fetch.
        client (httpx.Client): HTTP client instance.
    
    Returns:
        list: A list of repository URLs for this page.
    """
    url = f"{BASE_URL}/search/repositories?q={query}+org:{org}&per_page=100&page={page}"
    response = client.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    repos = data.get("items", [])
    return [repo["html_url"] for repo in repos]

def search_repository_url(query: str, org: str) -> list:
    """Search for repositories in a GitHub organization matching a query.

    Args:
        query (str): GitHub search query (e.g., "AWS ALB").
        org (str): GitHub organization name.

    Returns:
        list: A list of repository URLs matching the query.
    """
    all_repositories = []
    page = 1
    with httpx.Client(headers=HEADERS, timeout=30.0) as client:
        while True:
            repos = _fetch_repository_page(query, org, page, client)
            if not repos:
                break
            all_repositories.extend(repos)
            page += 1
    return all_repositories

@retry(stop=stop_after_attempt(3), wait=wait_random_exponential(multiplier=1, min=4, max=10), reraise=True)
def get_repository_readme(repo_name: str, org: str) -> str | None:
    """Fetch the README content of a GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        org (str): The GitHub organization name.

    Returns:
        str: The decoded content of the README file, or an empty string if not found.
    """
    url = f"{BASE_URL}/repos/{org}/{repo_name}/readme"
    with httpx.Client(headers=HEADERS, timeout=30.0) as client:
        response = client.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            return base64.b64decode(data["content"]).decode("utf-8")
        elif response.status_code == 404:
            print(f"README not found for {repo_name} (404)")
            return ""
        else:
            response.raise_for_status()