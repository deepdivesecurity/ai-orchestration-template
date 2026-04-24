---
name: coding-standard
description: Baseline cross-project coding standards for naming, readability, immutability, and code-quality. Use detailed IaC, frontend, backend, or other skills for specific framework patterns or standards.
license: Complete terms in LICENSE.txt
metadata:
  author: Deep Dive Security
  version: 1.0.0
---

# Coding Standards & Best Practices

## When to Use
- Starting a new project or module
- Reviewing code for quality and maintainability
- Refactoring existing code to improve readability, reduce technical debt, follow coding standards, improve performance, ensure immutability, or enhance security
- Setting up linting, formatting, or type-checking rules

## Scope Boundaries
Envoke this skill for: 
- Descriptive naming
- Immutability defaults
- Readability, KISS, DRY, and YAGNI principle enforcement
- Error-handling expectations and code review

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
- Clear varaible and function names that follow consistent naming conventions
- Self-documenting code with minimal comments
- Consisting formatting and style

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
- Organize files and directories by feature, module, or layer (e.g., frontend, backend, infrastructure)
- Follow consistent naming conventions for files and directories
- Separate concerns (e.g., separate business logic from presentation logic)
