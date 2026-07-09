---
name: github-actions-standard
description: Baseline cross-project GitHub Actions standards for directory structure, naming conventions, composite actions, matrix strategies, caching, secrets and authn handling, concurrency, environment protection, hardening, and overall workflow design. Use detailed IaC, frontend, backend, or other skills for specific framework patterns or standards.
license: Complete terms in LICENSE.txt
metadata:
  author: Deep Dive Security
  version: 1.0.0
---

# GitHub Actions Standards & Best Practices

## When to Use
- Setting up GitHub Actions for CI/CD, testing, or deployment
- Starting a new project or GitHub workflow
- Reviewing workflows for quality and maintainability
- Setting up linting, formatting, or type-checking rules
- Refactoring existing workflows to improve readability, reduce technical debt, follow GitHub Actions standards, improve performance, ensure immutability, or enhance security

## Scope Boundaries
Envoke this skill for: 
- GitHub Workflow directory structure and naming conventions
- Composite action design and implementation
- Matrix strategy design and implementation
- Caching strategies and implementation
- Secrets and authentication handling in the CD pipeline
- Concurrency and environment protection in the CI/CD pipeline
- Readability, KISS, DRY, and YAGNI principle enforcement

Do not use this skill for: 
- Framework-specific patterns or standards (use detailed IaC, frontend, backend, or other skills for that)
- Specific language syntax or features (use detailed language-specific skills for that)
- API design
- Frontend architecture
- Backend architecture
- Database design

## Code Quality Principles
### 1. Readability First
- Code is read more than written
- Clear variable and function names that follow consistent naming conventions
- Self-documenting code with minimal comments
- Consistent formatting and style

### 2. KISS (Keep It Simple, Stupid)
- Avoid unnecessary complexity
- Break down complex problems into simpler, smaller functions or modules
- Avoid over-engineering or premature optimization
- Easy to understand code preferred over clever or complex solution

### 3. DRY (Don't Repeat Yourself)
- Avoid code duplication by abstracting common functionality into reusable functions, classes, or modules
- Use libraries or frameworks to avoid reinventing the wheel
- Refactor duplicated code when identified

### 4. YAGNI (You Aren't Gonna Need It)
- Focus on current requirements and avoid speculative features
- Refactor and add features as needed based on actual use cases
- Start simple, only refactor when necessary
- Avoid speculative generality

## File Structure
### Project Structure
- Follow consistent directory naming conventions for files and directories; workflows should be organized as follows: 
  - `.github/workflows/` - For workflow YAML files
  - `.github/actions/` - For composite actions
  - `.github/scripts/` - For scripts used in workflows
  - `.github/config/` - For configuration files used in workflows
  - `ci.yml` - Primary CI to test and lint on every push/PR
  - `deploy-staging.yml` - Deploy to staging on dev branch
  - `deploy-production.yml` - Deploy to prod on main branch (with approval)
  - `release.yml` - Create releases on version tags
  - `security-scan.yml` - Scheduled security scans
  - `dependency-update.yml` - Weekly dependency updates
  - `stale-issues.yml` - Housekeeping: Close stale issues
- Use kebab-case for filenames
- Use the `name:` field to give workflows human-readable names

## Workflow Design
- Each workflow should have a single responsibility (e.g. A CI workflow tests code; a deploy workflow deploys it) - Do not combine unrelated jobs into a single workflow

## Matrix Strategies
- Set `fail-fast: false` for test matrices
- Use `include` to add one-off jobs without expanding the entire matrix
- Keep matrices under 20 combinations

## Secrets & Authentication
- Use environment-scoped secrets for deployment credentials
- Never store secrets in workflow files
- Never echo or write secrets to files
- Use GitHub's built-in secrets management for sensitive data (e.g. `API_KEY: ${{ secrets.API_KEY }}`)
