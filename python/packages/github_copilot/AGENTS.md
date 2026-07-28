# GitHub Copilot Package (spark-core-github-copilot)

Integration with GitHub Copilot extensions.

## Main Classes

- **`GitHubCopilotAgent`** - Agent for GitHub Copilot extensions
- **`GitHubCopilotOptions`** - Options for Copilot agent configuration
- **`GitHubCopilotSettings`** - Pydantic settings for configuration

## Usage

```python
from spark_core.github import GitHubCopilotAgent

agent = GitHubCopilotAgent(...)
response = await agent.run("Hello")
```

## Import Path

```python
from spark_core.github import GitHubCopilotAgent
# or directly:
from spark_core_github_copilot import GitHubCopilotAgent
```
