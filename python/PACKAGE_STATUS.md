# Python Package Status

This file tracks the current lifecycle state of the Python packages in this workspace. Some packages at later stages might have features within them that are not ready yet, these have feature stage decorators on the relevant APIs, and for `experimental` features warnings are raised. See the [Feature-level staged APIs](#feature-level-staged-apis) section below for details on which features are in which stage and where to find them.

Status is grouped into these buckets:

- `alpha` - initial release and early development packages that are not yet ready for general use
- `beta` - prerelease packages that are not currently release candidates
- `rc` - release candidate packages, these are close to ready for release but may still have some breaking changes before the final release
- `released` - stable packages without a prerelease suffix, these are stable packages that should not have breaking changes between versions
- `deprecated` - removed or deprecated packages that should not be used for new work

## Current packages

| Package | Path | State |
| --- | --- | --- |
| `spark-core` | `python/` | `released` |
| `spark-core-a2a` | `python/packages/a2a` | `beta` |
| `spark-core-ag-ui` | `python/packages/ag-ui` | `released` |
| `spark-core-anthropic` | `python/packages/anthropic` | `beta` |
| `spark-core-azure-contentunderstanding` | `python/packages/azure-contentunderstanding` | `beta` |
| `spark-core-azure-ai-search` | `python/packages/azure-ai-search` | `beta` |
| `spark-core-azure-cosmos` | `python/packages/azure-cosmos` | `beta` |
| `spark-core-azure-cosmos-memory` | `python/packages/azure-cosmos-memory` | `alpha` |
| `spark-core-azurefunctions` | `python/packages/azurefunctions` | `beta` |
| `spark-core-bedrock` | `python/packages/bedrock` | `beta` |
| `spark-core-chatkit` | `python/packages/chatkit` | `beta` |
| `spark-core-claude` | `python/packages/claude` | `beta` |
| `spark-core-copilotstudio` | `python/packages/copilotstudio` | `beta` |
| `spark-core-core` | `python/packages/core` | `released` |
| `spark-core-declarative` | `python/packages/declarative` | `released` |
| `spark-core-devui` | `python/packages/devui` | `beta` |
| `spark-core-durabletask` | `python/packages/durabletask` | `beta` |
| `spark-core-foundry` | `python/packages/foundry` | `released` |
| `spark-core-foundry-hosting` | `python/packages/foundry_hosting` | `beta` |
| `spark-core-foundry-local` | `python/packages/foundry_local` | `beta` |
| `spark-core-gemini` | `python/packages/gemini` | `beta` |
| `spark-core-github-copilot` | `python/packages/github_copilot` | `released` |
| `spark-core-hosting` | `python/packages/hosting` | `alpha` |
| `spark-core-hosting-a2a` | `python/packages/hosting-a2a` | `alpha` |
| `spark-core-hosting-mcp` | `python/packages/hosting-mcp` | `alpha` |
| `spark-core-hosting-responses` | `python/packages/hosting-responses` | `alpha` |
| `spark-core-hosting-telegram` | `python/packages/hosting-telegram` | `alpha` |
| `spark-core-hyperlight` | `python/packages/hyperlight` | `beta` |
| `spark-core-lab` | `python/packages/lab` | `beta` |
| `spark-core-mem0` | `python/packages/mem0` | `beta` |
| `spark-core-mistral` | `python/packages/mistral` | `beta` |
| `spark-core-monty` | `python/packages/monty` | `beta` |
| `spark-core-ollama` | `python/packages/ollama` | `beta` |
| `spark-core-openai` | `python/packages/openai` | `released` |
| `spark-core-orchestrations` | `python/packages/orchestrations` | `released` |
| `spark-core-purview` | `python/packages/purview` | `beta` |
| `spark-core-redis` | `python/packages/redis` | `beta` |
| `spark-core-tools` | `python/packages/tools` | `beta` |

## Deprecated / removed packages

| Package | Previous path | State | Notes |
| --- | --- | --- | --- |
| `spark-core-azure-ai` | `python/packages/azure-ai` | `deprecated` | The client classes within the `azure-ai` package were renamed, sometimes changed, and moved to `spark-core-foundry`. |

## Feature-level staged APIs

The following feature IDs have explicit feature-stage decorators on public APIs in the packages
listed below.

### Experimental features

#### `DECLARATIVE_AGENTS`

- `spark-core-declarative`: declarative agent loading APIs from
  `spark_core_declarative`, including `AgentFactory`,
  `DeclarativeLoaderError`, `ProviderLookupError`, and `ProviderTypeMapping`
  from `spark_core_declarative/_loader.py`

#### `EVALS`

- `spark-core-core`: exported evaluation APIs from `spark_core`, including
  `LocalEvaluator`, `evaluate_agent`, `evaluate_workflow`, and the related evaluation types and
  helper checks defined in `spark_core/_evaluation.py`
- `spark-core-foundry`: `FoundryEvals`, `evaluate_traces`, and `evaluate_foundry_target`

#### `SKILLS`

- `spark-core-core`: exported skills APIs from `spark_core`, including `Skill`,
  `SkillResource`, `SkillScript`, `SkillScriptRunner`, and `SkillsProvider` from
  `spark_core/_skills.py`

### Release-candidate features

There are currently no feature-level `rc` APIs.
