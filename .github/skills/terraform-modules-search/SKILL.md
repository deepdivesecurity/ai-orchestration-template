---
name: terraform-modules-search
description: Searches for Terraform modules in a GitHub organization and retrieves their README content to provide information on how to use the modules.
license: Complete terms in LICENSE.txt
metadata: 
  version: 1.0.0
---

# Terraform Module Search

## When to Use
- User is writing Terraform IaC and wants to see if an existing module exists in a GitHub organization that can be reused.
- User wants to find Terraform modules in a GitHub organization.
- User needs the README content of a specific module repo to determine how to write the Terraform IaC for using it.
- User wants to list or search repositories in a GitHub organization that contain Terraform modules.

## Prerequisites
- Python environment with dependencies installed (`httpx`, `python-dotenv`)
- `.env` file with `GH_TOKEN`, `GH_ORG`, `BASE_URL`

## Available functions
See [get-modules-from-github.py](./scripts/get-modules-from-github.py) for the implementation.

## Procedure
1. Ensure the `.env` file is configured with the required variables
2. Run the script using: `python .github/skills/terraform-modules-search/scripts/get-modules-from-github.py`
3. Or import and call individual functions from the script: 
    - `search_repository_url(query, org)` - search repos matching a query, use this whenever possible instead of listing all repos and filtering client-side. For example, to find modules related to "AWS ALB", call `search_repository_url("AWS ALB", "your-org")`, then find the instructions by calling `get_repository_readme(repo_name, org)` with the URL of the repo returned from the search for how to use the module.
    - `get_repository_readme(repo_name, org)` - fetch the README content of a specific GitHub repository to understand how to use the module, this is the most important function for users looking to use Terraform modules.
