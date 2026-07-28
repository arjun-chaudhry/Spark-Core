# Changelog

All notable changes to the Spark Core Python packages will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [github-copilot-1.0.0] - 2026-07-23

### Added
- **spark-core-github-copilot**: Forward input attachments (images, documents, and other inline binary content) to GitHub Copilot as inline blobs ([#7300](https://github.com/microsoft/spark-core/pull/7300))

### Changed
- **spark-core-github-copilot**: Promote the package from release candidate to stable

## [hosting-a2a-1.0.0a260723] - 2026-07-23

### Added
- **spark-core-hosting-a2a**: Add progressive agent and workflow A2A adapters with native card generation, skill discovery, typed conversion, and mode-aware validation ([#7258](https://github.com/microsoft/spark-core/pull/7258))

### Changed
- **samples**: Update the app-owned A2A hosting sample to use the progressive adapter surface ([#7258](https://github.com/microsoft/spark-core/pull/7258))

## [1.12.1] - 2026-07-22

### Added
- **spark-core-openai**: Add explicit prompt cache breakpoints for GPT-5.6 models and a usage sample ([#7163](https://github.com/microsoft/spark-core/pull/7163))

### Changed
- **spark-core-ag-ui**: Promote the package from release candidate to stable
- **spark-core-core**: Add security guidance for custom MCP Streamable HTTP clients ([#7245](https://github.com/microsoft/spark-core/pull/7245))

### Fixed
- **spark-core-gemini**: Preserve Gemini 3 thought signatures across function-call replays ([#7095](https://github.com/microsoft/spark-core/pull/7095))
- **spark-core-core**, **spark-core-foundry**, **spark-core-foundry-hosting**, **spark-core-openai**: Fix stateless replay of reasoning-paired tool calls ([#7233](https://github.com/microsoft/spark-core/pull/7233))

## [1.12.0] - 2026-07-21

### Added
- **spark-core-azure-cosmos-memory**: Add an alpha Azure Cosmos DB semantic-memory context provider with fact extraction, user profiles, samples, and integration coverage ([#6719](https://github.com/microsoft/spark-core/pull/6719))
- **spark-core-azurefunctions**, **spark-core-core**, **spark-core-durabletask**: Add HITL response-URL addressing for requests raised from inside workflows ([#7001](https://github.com/microsoft/spark-core/pull/7001))
- **spark-core-core**: Add cross-session origin attribution to context-injected messages ([#7041](https://github.com/microsoft/spark-core/pull/7041))
- **spark-core-core**, **spark-core-tools**: Warn when auto-approved tools have name collisions ([#7090](https://github.com/microsoft/spark-core/pull/7090))
- **spark-core-core**: Add a `session_provider` option to `MCPSkillsSource` and `MCPSkill` (mutually exclusive with `client`) that resolves the MCP session on every fetch, keeping cached skills reconnect-safe when the underlying session is replaced ([#7135](https://github.com/microsoft/spark-core/pull/7135))
- **spark-core-hosting-a2a**: Add app-owned A2A hosting helpers ([#7050](https://github.com/microsoft/spark-core/pull/7050))
- **spark-core-hosting-mcp**: Add app-owned MCP hosting helpers for exposing agents and workflows as native MCP tools ([#7209](https://github.com/microsoft/spark-core/pull/7209))
- **spark-core-hosting-responses**: [BREAKING] Add Responses conversation ID creation and parsing helpers, and distinguish conversation IDs from previous response IDs ([#7234](https://github.com/microsoft/spark-core/pull/7234))
- **spark-core-hosting-telegram**: Add Telegram hosting helpers and samples ([#7047](https://github.com/microsoft/spark-core/pull/7047))
- **samples**: Add a Microsoft OpenTelemetry Distro observability sample ([#5632](https://github.com/microsoft/spark-core/pull/5632))

### Changed
- **spark-core-ag-ui**: [BREAKING] Emit `TOOL_CALL` events for workflow participant tool calls ([#7039](https://github.com/microsoft/spark-core/pull/7039))
- **spark-core-a2a**: Reduce `A2AExecutor` log noise for content types without protocol mappings ([#7034](https://github.com/microsoft/spark-core/pull/7034))
- **spark-core-ag-ui**, **spark-core-core**: Optimize shared serialization paths ([#7165](https://github.com/microsoft/spark-core/pull/7165))
- **spark-core-ag-ui**, **spark-core-bedrock**, **spark-core-claude**, **spark-core-core**, **spark-core-github-copilot**, **spark-core-ollama**, **spark-core-openai**: Normalize chat finish reasons across providers ([#7105](https://github.com/microsoft/spark-core/pull/7105))
- **spark-core-anthropic**, **spark-core-azure-contentunderstanding**, **spark-core-azure-cosmos**, **spark-core-core**, **spark-core-declarative**, **spark-core-devui**, **spark-core-foundry**, **spark-core**: Update Microsoft Foundry branding in shipped APIs and package documentation ([#6999](https://github.com/microsoft/spark-core/pull/6999))
- **spark-core-azure-contentunderstanding**, **spark-core-azure-cosmos-memory**, **spark-core-chatkit**, **spark-core-core**, **spark-core-durabletask**, **spark-core-foundry**, **spark-core-foundry-hosting**, **spark-core-gemini**, **spark-core-hyperlight**, **spark-core-lab**, **spark-core-monty**, **spark-core-openai**, **spark-core-tools**, **spark-core**: Consolidate dependency updates and compatibility adjustments ([#7204](https://github.com/microsoft/spark-core/pull/7204))
- **spark-core-azurefunctions**, **spark-core-devui**, **spark-core-foundry**, **spark-core-hosting-responses**, **spark-core-lab**, **spark-core-mistral**, **spark-core**: Clean up dependency groups and compatibility handling ([#7046](https://github.com/microsoft/spark-core/pull/7046))
- **spark-core-azurefunctions**, **spark-core-durabletask**: Normalize initial durable workflow inputs across hosting paths ([#7205](https://github.com/microsoft/spark-core/pull/7205))
- **spark-core-core**: [BREAKING — experimental] Correct harness before-strategy compaction when state persists per service call ([#7055](https://github.com/microsoft/spark-core/pull/7055))
- **spark-core-core**: [BREAKING] Graduate `create_harness_agent` from experimental to stable ([#7120](https://github.com/microsoft/spark-core/pull/7120))
- **spark-core-core**: Graduate the mode and todo providers from experimental to stable ([#7053](https://github.com/microsoft/spark-core/pull/7053))
- **spark-core-core**: Graduate `ToolApprovalMiddleware` from experimental to stable ([#7106](https://github.com/microsoft/spark-core/pull/7106))
- **spark-core-core**: Graduate `FileMemoryProvider` from experimental to stable ([#7113](https://github.com/microsoft/spark-core/pull/7113))
- **spark-core-core**: Make `FileAccessProvider` opt-in for harness agents ([#7094](https://github.com/microsoft/spark-core/pull/7094))
- **spark-core-core**: Serialize tool definitions best-effort for observability ([#7029](https://github.com/microsoft/spark-core/pull/7029))
- **spark-core-declarative**: Promote declarative workflows from release candidate to stable ([#7065](https://github.com/microsoft/spark-core/pull/7065))
- **spark-core-devui**: Refine request logging ([#7083](https://github.com/microsoft/spark-core/pull/7083))
- **spark-core-foundry-hosting**: Promote the package to beta and add it to the main installation surface; make the Foundry Toolbox MCP skills sample self-contained ([#7099](https://github.com/microsoft/spark-core/pull/7099))
- **spark-core-azure-contentunderstanding**, **spark-core-gemini**, **spark-core-mistral**, **spark-core-monty**, **spark-core-tools**: Promote the packages to beta, add them to the main installation surface, expose lazy-loading namespaces, and move package-local samples into the root sample tree
- **spark-core-github-copilot**: Forward `GitHubCopilotOptions` verbatim when creating sessions ([#7155](https://github.com/microsoft/spark-core/pull/7155))
- **docs**: Add self-hosting sample snippets ([#7104](https://github.com/microsoft/spark-core/pull/7104))
- **docs**: Add environment-file templates for Durable Task hosting samples ([#5948](https://github.com/microsoft/spark-core/pull/5948))
- **samples**: Keep ChatKit attachments close to the sample application that owns them ([#7038](https://github.com/microsoft/spark-core/pull/7038))

### Fixed
- **spark-core-ag-ui**: Bind streamed tool arguments to their call ids ([#6342](https://github.com/microsoft/spark-core/pull/6342))
- **spark-core-ag-ui**: Accept state data URIs whose media type includes parameters ([#6905](https://github.com/microsoft/spark-core/pull/6905))
- **spark-core-ag-ui**: Coalesce reasoning deltas without content ids into a single reasoning block ([#6804](https://github.com/microsoft/spark-core/pull/6804))
- **spark-core-ag-ui**: Bridge request state and session continuity ([#7084](https://github.com/microsoft/spark-core/pull/7084))
- **spark-core-ag-ui**: Replay workflow handoff results correctly ([#7102](https://github.com/microsoft/spark-core/pull/7102))
- **spark-core-ag-ui**: Clarify `require_confirmation` documentation for `confirm_changes` HITL gating ([#6884](https://github.com/microsoft/spark-core/pull/6884))
- **spark-core-anthropic**: Prevent per-run `additional_beta_flags` from leaking into request keyword arguments ([#7060](https://github.com/microsoft/spark-core/pull/7060))
- **spark-core-core**: Clear `service_session_id` in the agent wrapper when session propagation is enabled ([#5875](https://github.com/microsoft/spark-core/pull/5875))
- **spark-core-core**: Preserve tool span context for parallel calls ([#6512](https://github.com/microsoft/spark-core/pull/6512))
- **spark-core-core**: Parse structured values assembled from split text chunks ([#6990](https://github.com/microsoft/spark-core/pull/6990))
- **spark-core-core**: Raise `ValueError` for malformed data URIs ([#6916](https://github.com/microsoft/spark-core/pull/6916))
- **spark-core-core**: Preserve function-call names when merging streaming deltas ([#6809](https://github.com/microsoft/spark-core/pull/6809))
- **spark-core-core**, **spark-core-durabletask**: Handle checkpoint encodings consistently ([#6579](https://github.com/microsoft/spark-core/pull/6579))
- **spark-core-core**: Preserve explicit null arguments during automatic function calling ([#7108](https://github.com/microsoft/spark-core/pull/7108))
- **spark-core-core**: Count non-ASCII text correctly during compaction ([#7124](https://github.com/microsoft/spark-core/pull/7124))
- **spark-core-core**: Forward `header_provider` headers to streamable HTTP MCP transports ([#7218](https://github.com/microsoft/spark-core/pull/7218))
- **spark-core-core**: Prevent compaction from emitting empty projections ([#7219](https://github.com/microsoft/spark-core/pull/7219))
- **spark-core-core**: Return MCP tool-use sampling results to the requesting server ([#7189](https://github.com/microsoft/spark-core/pull/7189))
- **spark-core-foundry-hosting**: Make `FoundryToolbox.as_skills_provider()` cache toolbox skill discovery by default so `skill://index.json` is read once instead of on every agent run, give `disable_caching` an observable effect, and add a `cache_refresh_interval` option ([#7135](https://github.com/microsoft/spark-core/pull/7135))
- **spark-core-hosting**, **spark-core-hosting-responses**: Isolate stored session snapshots from later mutations ([#7141](https://github.com/microsoft/spark-core/pull/7141))
- **spark-core-ollama**: Generate distinct call ids for parallel tool calls ([#6822](https://github.com/microsoft/spark-core/pull/6822))
- **spark-core-orchestrations**: Prevent the Magentic manager from duplicating conversation history ([#6297](https://github.com/microsoft/spark-core/pull/6297))
- **samples**: Correct the concurrent agents sample's handling of workflow output ([#6548](https://github.com/microsoft/spark-core/pull/6548))

## [1.11.0] - 2026-07-09

### Added
- **spark-core-core**: Add message injection middleware so tools or host code can enqueue messages into an active run and drain them into the next model call within the same `AgentSession` ([#6998](https://github.com/microsoft/spark-core/pull/6998))
- **spark-core-core**: Integrate message injection into `create_harness_agent` and the harness console sample so a running harness agent can be nudged mid-turn ([#7027](https://github.com/microsoft/spark-core/pull/7027))
- **spark-core-core**: Add progressive MCP disclosure so agents can discover, load, and unload MCP tool schemas on demand while keeping the `allowed_tools` boundary intact ([#6850](https://github.com/microsoft/spark-core/pull/6850))
- **spark-core-core**: Add `refresh_interval` (TTL) to `CachingSkillsSource` so cached skill lists expire and re-fetch on a configured interval ([#6977](https://github.com/microsoft/spark-core/pull/6977))
- **spark-core-core**, **spark-core-foundry-hosting**: Add `SkillsSourceContext` (invoking agent plus optional session) threaded through the skills source pipeline, enabling context-aware filtering and per-key cache isolation ([#6895](https://github.com/microsoft/spark-core/pull/6895))
- **spark-core-core**: Allow disabling approval for `SkillsProvider` tools ([#6867](https://github.com/microsoft/spark-core/pull/6867))
- **spark-core-core**: Allow opting out of `FileAccessProvider` tool approval ([#6879](https://github.com/microsoft/spark-core/pull/6879))
- **spark-core-core**: Allow custom argument parsing for inline skill scripts so non-conforming tool-call argument shapes (for example, vLLM) can be handled ([#6817](https://github.com/microsoft/spark-core/pull/6817))
- **spark-core-hosting**, **spark-core-hosting-responses**: Add a hosting protocol helper surface (`AgentState`, `WorkflowState`, `SessionStore`, `AgentRunArgs`, `WorkflowRunArgs`) and Responses helpers (`create_response_id`, `responses_session_id`, `responses_to_run`, `responses_from_run`, `responses_from_streaming_run`) ([#6891](https://github.com/microsoft/spark-core/pull/6891))
- **spark-core-ag-ui**: Add FastAPI SSE keepalive support for long, output-silent streams ([#6980](https://github.com/microsoft/spark-core/pull/6980))
- **spark-core-github-copilot**: Forward `skill_directories` and `disabled_skills` to the Copilot session ([#6937](https://github.com/microsoft/spark-core/pull/6937))
- **spark-core-openai**: Allow `tool_choice: required` when `allowed_tools` is set ([#7024](https://github.com/microsoft/spark-core/pull/7024))
- **spark-core-anthropic**, **spark-core-core**, **spark-core-foundry-hosting**, **spark-core-gemini**, **spark-core-openai**: Mark hosted/provider-executed tool calls as informational-only via `Content.informational_only` so they remain visible in transcripts without local re-invocation ([#6997](https://github.com/microsoft/spark-core/pull/6997))
- **samples**: Add a deterministic action-boundary validation middleware sample ([#6528](https://github.com/microsoft/spark-core/pull/6528))
- **samples**: Add Agent Harness blog post accompanying samples, part 3 ([#6741](https://github.com/microsoft/spark-core/pull/6741))
- **samples**: Add a declarative Foundry Hosted Agent workflow sample ([#6897](https://github.com/microsoft/spark-core/pull/6897))

### Changed
- **spark-core-core**: [BREAKING — experimental] Extract caching from `SkillsProvider` into a `CachingSkillsSource` decorator ([#6847](https://github.com/microsoft/spark-core/pull/6847))
- **spark-core-core**: [BREAKING — experimental] Treat nested `SKILL.md` content as part of the parent skill instead of discovering it as a separate skill root ([#6849](https://github.com/microsoft/spark-core/pull/6849))
- **spark-core-core**: [BREAKING — experimental] `FileAccess`/`FileMemory` `replace_lines` now performs literal replacement (including line deletion) instead of always re-adding a line terminator ([#6859](https://github.com/microsoft/spark-core/pull/6859))
- **spark-core-core**: Remove the experimental marker from the Skills API now that its surface is stable ([#6974](https://github.com/microsoft/spark-core/pull/6974))
- **spark-core-core**: Lazy-load root `spark_core` exports to reduce import cost for narrow-surface scenarios ([#6962](https://github.com/microsoft/spark-core/pull/6962))
- **spark-core-a2a**, **spark-core-claude**, **spark-core-copilotstudio**, **spark-core-core**, **spark-core-durabletask**, **spark-core-github-copilot**, **spark-core-purview**: Implement ADR-0029 `service_session_id` lifecycle mapping, separating durable continuation state, per-run identity forwarding, and telemetry conversation-id extraction ([#6724](https://github.com/microsoft/spark-core/pull/6724))
- **spark-core-azurefunctions**, **spark-core-core**, **spark-core-durabletask**: [BREAKING] Support multi-workflow hosting and sub-workflows on the Durable Task host, including per-workflow durable naming and nested human-in-the-loop request routing ([#6696](https://github.com/microsoft/spark-core/pull/6696))
- **spark-core-ag-ui**: [BREAKING] Canonicalize AG-UI interrupt and resume handling around `RUN_FINISHED.outcome.interrupts` and canonical `ResumeEntry` payloads ([#6925](https://github.com/microsoft/spark-core/pull/6925))
- **spark-core-mem0**: Support the mem0ai 2.x OSS search call shape ([#7004](https://github.com/microsoft/spark-core/pull/7004))
- **spark-core-mistral**: Widen the `uv_build` backend requirement to allow newer `uv` releases ([#7033](https://github.com/microsoft/spark-core/pull/7033))
- **spark-core-lab**: Raise the `agentlightning` dependency ceiling for the `lightning` extra ([#6984](https://github.com/microsoft/spark-core/pull/6984))
- **spark-core-claude**, **spark-core-durabletask**, **spark-core-gemini**, **spark-core-monty**, **spark-core-openai**: Raise dependency floors to the first versions that provide the SDK APIs and typing consumed by these packages
- **docs**: Clarify `AgentSession.service_session_id` scoping to document backing API key/project boundaries and hosted multi-tenant guidance ([#6993](https://github.com/microsoft/spark-core/pull/6993))
- **docs**: Add security guidance for external skill sources and script execution to harness feature docstrings ([#6936](https://github.com/microsoft/spark-core/pull/6936))
- **samples**: Bump `vite` and `@vitejs/plugin-react-swc` in the ChatKit integration sample frontend ([#6613](https://github.com/microsoft/spark-core/pull/6613))
- **samples**: Add a multi-tenant hosting security consideration note to the A2A sample ([#6983](https://github.com/microsoft/spark-core/pull/6983))
- **samples**: Update Foundry Hosted Agent samples for the v2 protocol changes ([#6841](https://github.com/microsoft/spark-core/pull/6841))
- **samples**: Use a writable runtime directory for the Foundry Skills sample ([#6606](https://github.com/microsoft/spark-core/pull/6606))
- **tests**: Add Agent typing smoke tests across chat clients ([#6950](https://github.com/microsoft/spark-core/pull/6950))
- **tests**: Skip NumPy stubs during mypy typing to unblock scheduled dependency-maintenance typing runs ([#6969](https://github.com/microsoft/spark-core/pull/6969))
- **tests**: Consolidate Dependabot dependency updates for dev tooling (`uv`, `ruff`, `pytest`, `mypy`, `pyright`, `mcp`, `opentelemetry-sdk`, `poethepoet`) across the workspace and package dev-dependency groups ([#6984](https://github.com/microsoft/spark-core/pull/6984), [#7033](https://github.com/microsoft/spark-core/pull/7033))
- **tests**: Bump the transitive `js-yaml` dependency in the DevUI frontend lockfile ([#6813](https://github.com/microsoft/spark-core/pull/6813))

### Fixed
- **spark-core-core**: Parse the structured response value from the final message instead of concatenated text, avoiding spurious `ValidationError`/`JSONDecodeError` ([#6383](https://github.com/microsoft/spark-core/pull/6383))
- **spark-core-core**: Fix `read_skill_resource` instruction dropping the `.md` extension ([#7031](https://github.com/microsoft/spark-core/pull/7031))
- **spark-core-core**: Bind policy-enforcement approvals to a single tool invocation (call id, function, arguments, security label, and session) and consume them on first use ([#6966](https://github.com/microsoft/spark-core/pull/6966))
- **spark-core-core**: Process messages to an executor serially within a superstep to prevent concurrent handler invocations for the same target executor ([#6776](https://github.com/microsoft/spark-core/pull/6776))
- **spark-core-core**: Auto-inject local conversation history on stateless clients even when non-history context providers (for example, `SkillsProvider` and `FileAccessProvider`) are registered ([#6810](https://github.com/microsoft/spark-core/pull/6810))
- **spark-core-core**: Improve the error message when a `TypeVar` is used in handler/executor registration ([#4553](https://github.com/microsoft/spark-core/pull/4553))
- **spark-core-anthropic**, **spark-core-core**: Fix Anthropic requests that mix tool calls and tool results in one assistant message, and return a deterministic result when the function-loop limit is reached with a blank final response ([#6794](https://github.com/microsoft/spark-core/pull/6794))
- **spark-core-anthropic**, **spark-core-core**, **spark-core-foundry-hosting**, **spark-core-openai**: Fix Foundry reasoning/MCP compaction so reasoning output keeps its provider id and reasoning plus MCP call pairs stay atomic ([#6907](https://github.com/microsoft/spark-core/pull/6907))
- **spark-core-anthropic**: Normalize a single Anthropic tool value the same as a one-item sequence during request preparation ([#6903](https://github.com/microsoft/spark-core/pull/6903))
- **spark-core-anthropic**: Migrate structured outputs to the stable `output_config.format` shape to avoid malformed/concatenated JSON when tools are also present ([#5884](https://github.com/microsoft/spark-core/pull/5884))
- **spark-core-azure-ai-search**: Pass `include_reference_source_data` in agentic search requests so `source_data` is populated on returned references ([#5100](https://github.com/microsoft/spark-core/pull/5100))
- **spark-core-bedrock**: Fix non-ASCII escaping in JSON content blocks returned by the Converse API ([#6628](https://github.com/microsoft/spark-core/pull/6628))
- **spark-core-foundry**: Strip tools from the Foundry agent request on the preview path (`allow_preview=True`) to avoid `invalid_payload` errors ([#6644](https://github.com/microsoft/spark-core/pull/6644))
- **spark-core-gemini**: Fix `GeminiChatClient` dropping image/file content on multimodal messages ([#6751](https://github.com/microsoft/spark-core/pull/6751))
- **spark-core-claude**, **spark-core-core**, **spark-core-github-copilot**, **spark-core-ollama**: Fix response metadata construction so usage, finish reason, raw response, continuation token, and structured value are propagated consistently across providers ([#6955](https://github.com/microsoft/spark-core/pull/6955))
- **spark-core-a2a**: Accept A2A data URIs whose media type includes parameters before the `;base64` marker ([#6818](https://github.com/microsoft/spark-core/pull/6818))
- **spark-core-ag-ui**: Prefer explicit AG-UI resume payloads over message-derived responses ([#6360](https://github.com/microsoft/spark-core/pull/6360))
- **spark-core-ag-ui**: Clear queued approvals on cancel so cancelled flows do not leave stale prompts for later turns ([#6947](https://github.com/microsoft/spark-core/pull/6947))
- **spark-core-ag-ui**: Preserve the streamed text message id in mixed snapshots with pending tool calls and streamed trailing text ([#6269](https://github.com/microsoft/spark-core/pull/6269))
- **spark-core-devui**: Fix `list[Message]` input handling for declarative `ToolAgent` entries ([#6534](https://github.com/microsoft/spark-core/pull/6534))
- **spark-core-devui**: Fix DevUI deployment Dockerfile auth args ([#6150](https://github.com/microsoft/spark-core/pull/6150))
- **spark-core-hyperlight**: Harden workspace staging against symlinks and reparse points that could escape the sandbox workspace/mount root ([#6856](https://github.com/microsoft/spark-core/pull/6856))
- **spark-core-openai**: Fix `web_search_options` sent to the Azure OpenAI Chat Completions API ([#6225](https://github.com/microsoft/spark-core/pull/6225))
- **docs**: Fix stale `ChatAgent` references in `_clients.py` docstrings and make tool-support examples copy/paste-safe ([#6924](https://github.com/microsoft/spark-core/pull/6924))
- **samples**: Fix an invalid `options` kwarg in the workflow shared-session sample ([#6294](https://github.com/microsoft/spark-core/pull/6294))
- **docs**: Add prerequisite command documentation for Python hosting samples ([#5935](https://github.com/microsoft/spark-core/pull/5935))

### Removed
- **spark-core-hosting-telegram**: [BREAKING] Remove the unreleased hosting-telegram package and the earlier host/channel surface from the workspace, superseded by the new hosting protocol helper surface ([#6891](https://github.com/microsoft/spark-core/pull/6891))

## [1.10.0] - 2026-06-30

### Added
- **spark-core-core**: Explicitly emit `available_resources` and `available_scripts` in skill content ([#6694](https://github.com/microsoft/spark-core/pull/6694))
- **spark-core-core**: Autolabelling MCP servers based on hints and GitHub MCP server interface labels ([#6171](https://github.com/microsoft/spark-core/pull/6171))
- **spark-core-core**: `create_harness_agent` `skills_paths` accepts `str | Path | Sequence[str | Path] | None` ([#6717](https://github.com/microsoft/spark-core/pull/6717))
- **spark-core-core**: Background agent loop resolves provider automatically and adds feedback message builder ([#6735](https://github.com/microsoft/spark-core/pull/6735))
- **spark-core-core**: Stop swallowing skill script and resource errors so the model can self-correct ([#6755](https://github.com/microsoft/spark-core/pull/6755))
- **spark-core-foundry**: Add `FoundryAgent` conversation session helper ([#6623](https://github.com/microsoft/spark-core/pull/6623))
- **spark-core-foundry**: Add support for Foundry Adaptive evals ([#6267](https://github.com/microsoft/spark-core/pull/6267))
- **spark-core-bedrock**, **spark-core-gemini**: Surface cache and reasoning token counts ([#6640](https://github.com/microsoft/spark-core/pull/6640))
- **spark-core-durabletask**: Host Spark Core workflows on a standalone Durable Task worker ([#6418](https://github.com/microsoft/spark-core/pull/6418))
- **spark-core-azure-ai-search**: Support stable and preview Azure AI Search (Foundry IQ) API versions ([#6603](https://github.com/microsoft/spark-core/pull/6603))
- **spark-core-github-copilot**: Align function approval to use SDK `on_pre_tool_use` hook ([#6750](https://github.com/microsoft/spark-core/pull/6750))

### Changed
- **spark-core-core**: [BREAKING — experimental] Refactor `FileSkillsSource` for depth-based discovery and predicate filters ([#6488](https://github.com/microsoft/spark-core/pull/6488))
- **spark-core-core**: [BREAKING — experimental] Require approval for file-access tools with read-only auto-approval ([#6599](https://github.com/microsoft/spark-core/pull/6599))
- **spark-core-core**: [BREAKING — experimental] Integrate looping into `HarnessAgent` ([#6607](https://github.com/microsoft/spark-core/pull/6607))
- **spark-core-core**: [BREAKING — experimental] Port `FileMemoryProvider` and integrate into harness agent ([#6547](https://github.com/microsoft/spark-core/pull/6547))
- **spark-core-core**: [BREAKING — experimental] Make all `SkillsProvider` tools require approval by default ([#6754](https://github.com/microsoft/spark-core/pull/6754))
- **spark-core-core**: [BREAKING — experimental] Improve FileAccess/FileMemory harness providers (surgical edits, read-only tier, consistent naming) ([#6801](https://github.com/microsoft/spark-core/pull/6801))
- **spark-core-core**: Align serialized tool format to OTel GenAI tool definition format ([#6556](https://github.com/microsoft/spark-core/pull/6556))
- **spark-core-foundry-hosting**: [BREAKING] Foundry Hosted Agent V2 protocol upgrade ([#6811](https://github.com/microsoft/spark-core/pull/6811))
- **spark-core-foundry-hosting**: Add MCP as a hard dependency ([#6634](https://github.com/microsoft/spark-core/pull/6634))
- **spark-core-purview**: Prefer token principal for user identity ([#6693](https://github.com/microsoft/spark-core/pull/6693))
- **spark-core-ollama**: Convert Pydantic model class `response_format` to JSON schema in `OllamaChatClient` ([#6782](https://github.com/microsoft/spark-core/pull/6782))

### Fixed
- **spark-core-core**: Fix background agent telemetry context error ([#6764](https://github.com/microsoft/spark-core/pull/6764))
- **spark-core-core**: Fix MCP metadata and tool name handling ([#6656](https://github.com/microsoft/spark-core/pull/6656))
- **spark-core-core**: Ensure spans created inside sync preparations in streaming call are correctly nested ([#6552](https://github.com/microsoft/spark-core/pull/6552))
- **spark-core-openai**: Preserve OTel parent context for deferred streams ([#6709](https://github.com/microsoft/spark-core/pull/6709))
- **spark-core-openai**: Fix `FunctionShellTool` throw and empty streaming shell command ([#6763](https://github.com/microsoft/spark-core/pull/6763))
- **spark-core-ag-ui**: Fix tool history replay sanitization ([#6581](https://github.com/microsoft/spark-core/pull/6581))
- **spark-core-anthropic**: Re-role trailing assistant message to user for Anthropic compatibility ([#6207](https://github.com/microsoft/spark-core/pull/6207))
- **spark-core-hyperlight**: Fix CodeAct span parenting ([#6712](https://github.com/microsoft/spark-core/pull/6712))
- **spark-core-hyperlight**: Harden output capture against symlinks ([#6601](https://github.com/microsoft/spark-core/pull/6601))

## [1.9.0] - 2026-06-18

### Added
- **spark-core-core**: Add `AgentLoopMiddleware` for re-running agents in a loop ([#6174](https://github.com/microsoft/spark-core/pull/6174))
- **spark-core-core**: Integrate tool approval into the harness agent ([#6522](https://github.com/microsoft/spark-core/pull/6522))
- **spark-core-core**: Add tool approval middleware ([#6414](https://github.com/microsoft/spark-core/pull/6414))
- **spark-core-core**: Integrate the shell tool into the harness agent ([#6451](https://github.com/microsoft/spark-core/pull/6451))
- **spark-core-core**: Capture context provider instructions in agent telemetry ([#6515](https://github.com/microsoft/spark-core/pull/6515))
- **spark-core-core**, **spark-core-ag-ui**: Add opt-in AG-UI thread snapshot persistence and hydration ([#6471](https://github.com/microsoft/spark-core/pull/6471))
- **spark-core-foundry-hosting**: Emit failed events for hosted agent responses ([#6502](https://github.com/microsoft/spark-core/pull/6502))

### Changed
- **spark-core-core**: [BREAKING] Add sampling guardrails to MCP tools — deny server-initiated sampling by default and add `sampling_approval_callback`, `sampling_max_tokens`, and `sampling_max_requests` parameters ([#6413](https://github.com/microsoft/spark-core/pull/6413))
- **spark-core-core**: [BREAKING] Align FileAccess tools with .NET, adding directory discovery and recursive search ([#6476](https://github.com/microsoft/spark-core/pull/6476))
- **spark-core-declarative**: [BREAKING] Additional fixes for declarative workflow execution ([#6489](https://github.com/microsoft/spark-core/pull/6489))
- **spark-core-azure-contentunderstanding**: Adopt `azure-ai-contentunderstanding` `to_llm_input` in the CU context provider ([#5796](https://github.com/microsoft/spark-core/pull/5796))
- **spark-core-orchestrations**: Promote to stable (`1.0.0`)

### Fixed
- **spark-core-core**: Stop forwarding the unsupported `function_invocation_configuration` kwarg from `as_agent` ([#6520](https://github.com/microsoft/spark-core/pull/6520))
- **spark-core-core**: Fix MCP `allowed_tools` empty-list handling ([#6296](https://github.com/microsoft/spark-core/pull/6296))
- **spark-core-core**: Disable harness compaction when max tokens are not provided ([#6410](https://github.com/microsoft/spark-core/pull/6410))
- **spark-core-core**: Parse MCP `CallToolResult.structuredContent` to prevent tool results returning `None` ([#6421](https://github.com/microsoft/spark-core/pull/6421))
- **spark-core-core**: Catch bare `ImportError` during hosted-environment detection so optional Foundry hosting probing cannot crash user-agent setup
- **spark-core-anthropic**, **spark-core-core**, **spark-core-openai**: Fix OTel usage detail attributes ([#6493](https://github.com/microsoft/spark-core/pull/6493))
- **spark-core-foundry**, **spark-core-openai**: Fix Azure AI Search citation URLs ([#6453](https://github.com/microsoft/spark-core/pull/6453))
- **spark-core-foundry**: Fix `aiohttp` dependency specification ([#6567](https://github.com/microsoft/spark-core/pull/6567))
- **spark-core-declarative**: Fix declarative workflow execution ([#6468](https://github.com/microsoft/spark-core/pull/6468))
- **samples**: Fix harness console rendering a single streamed tool call multiple times ([#6549](https://github.com/microsoft/spark-core/pull/6549))
- **samples**: Fix `ollama_chat_client.py` to pass tools via the options dict ([#6480](https://github.com/microsoft/spark-core/pull/6480))

## [1.8.1] - 2026-06-09

### Added
- **spark-core-core**: Add MCP client OTel spans per GenAI semantic conventions ([#6349](https://github.com/microsoft/spark-core/pull/6349))
- **spark-core-core**: Add MCP long-running task support ([#6319](https://github.com/microsoft/spark-core/pull/6319))

### Changed
- **spark-core-claude**: Bump `claude-agent-sdk` to 0.2.87 ([#6248](https://github.com/microsoft/spark-core/pull/6248))
- **spark-core-core**: Document checkpoint storage security model and deserialization trust boundaries ([#6295](https://github.com/microsoft/spark-core/pull/6295))
- **spark-core-azurefunctions**: Document checkpoint storage security model and deserialization trust boundaries ([#6295](https://github.com/microsoft/spark-core/pull/6295))

### Fixed
- **spark-core-core**: Filter MCP tool kwargs to declared params via allowlist ([#6399](https://github.com/microsoft/spark-core/pull/6399))
- **spark-core-core**: Fix per-service-call history persistence with server-storing clients ([#6310](https://github.com/microsoft/spark-core/pull/6310))
- **spark-core-openai**: Use `getattr` for non-OpenAI provider response compatibility ([#6270](https://github.com/microsoft/spark-core/pull/6270))
- **spark-core-foundry-hosting**: Refactor workflow-as-agent pending request handling ([#6259](https://github.com/microsoft/spark-core/pull/6259))
- **spark-core-gemini**: Make Gemini honor declarative `outputSchema`, not just JSON mode ([#5893](https://github.com/microsoft/spark-core/pull/5893))
- **spark-core-mem0**: Isolate entity retrieval and correct `app_id` payload ([#6242](https://github.com/microsoft/spark-core/pull/6242))
- **spark-core-ag-ui**: Match AG-UI approval responses to requested arguments ([#6376](https://github.com/microsoft/spark-core/pull/6376))

## [1.8.0] - 2026-06-04

### Added
- **spark-core-core**: Add MCP-based skills discovery (`McpSkillsSource`) ([#6169](https://github.com/microsoft/spark-core/pull/6169))
- **spark-core-core**: Progressive tool exposure via `FunctionInvocationContext` ([#6233](https://github.com/microsoft/spark-core/pull/6233))
- **spark-core-core**: Add background agent support to harness agent ([#6155](https://github.com/microsoft/spark-core/pull/6155))
- **spark-core-core**: Add `AgentFileStore` and `FileAccessProvider` for file access operations ([#6099](https://github.com/microsoft/spark-core/pull/6099))
- **spark-core-core**: Coalesce code interpreter history chunks ([#5801](https://github.com/microsoft/spark-core/pull/5801))
- **spark-core-core**: Run sync tools off the event loop ([#5773](https://github.com/microsoft/spark-core/pull/5773))
- **spark-core-bedrock**: Implement native structured output support via Converse API ([#6052](https://github.com/microsoft/spark-core/pull/6052))
- **spark-core-foundry**: Add Foundry Adaptive Evals integration for rubric-generation ([#6101](https://github.com/microsoft/spark-core/pull/6101))
- **spark-core-foundry**: Add `timeout` parameter to `FoundryAgent` to fix `ConnectTimeout` on multi-turn conversations ([#6263](https://github.com/microsoft/spark-core/pull/6263))
- **spark-core-mistral**: Add Mistral AI embedding client package ([#5480](https://github.com/microsoft/spark-core/pull/5480))
- **spark-core-a2a**: Expose `supported_protocol_bindings` as configurable parameter ([#6098](https://github.com/microsoft/spark-core/pull/6098))
- **spark-core-a2a**: Set `message_id` on `AgentResponseUpdate` for message-bearing paths ([#6163](https://github.com/microsoft/spark-core/pull/6163))
- **spark-core-foundry-hosting**: Persist hosted MCP call/results as canonical `mcp_call` output ([#6070](https://github.com/microsoft/spark-core/pull/6070))

### Changed
- **spark-core-github-copilot**: [BREAKING] Upgrade `github-copilot-sdk` to v1.0.0 (stable) ([#6292](https://github.com/microsoft/spark-core/pull/6292))
- **spark-core-core**: [BREAKING — experimental] Refactor Skill API to async resource and script lookup ([#6135](https://github.com/microsoft/spark-core/pull/6135))
- **spark-core-github-copilot**: Promote to release candidate (`1.0.0rc1`)
- **spark-core-declarative**: Promote to release candidate (`1.0.0rc1`) ([#6256](https://github.com/microsoft/spark-core/pull/6256))

### Fixed
- **spark-core-core**: Fix compaction message-id collisions and tool-loop summary persistence ([#6299](https://github.com/microsoft/spark-core/pull/6299))
- **spark-core-core**: Fix observability unsafe serialization of function-call arguments containing dataclass/framework objects ([#6026](https://github.com/microsoft/spark-core/pull/6026))
- **spark-core-core**: Consolidate MCP reliability fixes ([#6145](https://github.com/microsoft/spark-core/pull/6145))
- **spark-core-core**: Backfill chat span request model if unknown and response model is available ([#6160](https://github.com/microsoft/spark-core/pull/6160))
- **spark-core-anthropic**: Skip orphan anthropic thinking signatures ([#5784](https://github.com/microsoft/spark-core/pull/5784))
- **spark-core-foundry**: Fix `FoundryAgent` stripping model from `PromptAgent` requests ([#5526](https://github.com/microsoft/spark-core/pull/5526))
- **spark-core-foundry-hosting**: Fix toolbox consent flow in hosted agent ([#6249](https://github.com/microsoft/spark-core/pull/6249))
- **spark-core-foundry-hosting**: Drop hosted MCP calls when reasoning is stripped ([#6210](https://github.com/microsoft/spark-core/pull/6210))
- **spark-core-openai**: Fix OTLP HTTP base-endpoint losing `/v1/{signal}` auto-append ([#5913](https://github.com/microsoft/spark-core/pull/5913))
- **spark-core-openai**: Drop hosted MCP calls when reasoning is stripped ([#6210](https://github.com/microsoft/spark-core/pull/6210))
- **spark-core-orchestrations**: Fix spurious Magentic custom manager warning ([#6261](https://github.com/microsoft/spark-core/pull/6261))
- **spark-core-azurefunctions**: Fix integration test worker crashes on Py3.13 ([#4260](https://github.com/microsoft/spark-core/pull/4260))

## [1.7.0] - 2026-05-28

### Added
- **spark-core-core**: Add `HarnessAgent` and background-agents harness provider ([#6041](https://github.com/microsoft/spark-core/pull/6041), [#6069](https://github.com/microsoft/spark-core/pull/6069))
- **spark-core-core**, **spark-core-a2a**: Add `A2AAgentSession` with referenced task IDs and input-required support ([#5980](https://github.com/microsoft/spark-core/pull/5980))
- **spark-core-foundry**: Add experimental prompt-agent conversion and deployment APIs ([#5959](https://github.com/microsoft/spark-core/pull/5959))
- **spark-core-declarative**: Add Foundry Toolbox MCP invocation support and sample ([#5933](https://github.com/microsoft/spark-core/pull/5933))
- **samples**: Add hosting samples overview README ([#5407](https://github.com/microsoft/spark-core/pull/5407))

### Changed
- **spark-core-core**: Align TodoProvider tool names with the C# implementation ([#6107](https://github.com/microsoft/spark-core/pull/6107))
- **spark-core-core**: Align ModeProvider tool names and instructions ([#6071](https://github.com/microsoft/spark-core/pull/6071))
- **spark-core-chatkit**: Raise the `openai-chatkit` dependency floor to `>=1.6.4` to match the current typed API usage.
- **spark-core-declarative**: [BREAKING] Remove Python-only declarative actions and rename alias kinds to C# canonical names ([#6126](https://github.com/microsoft/spark-core/pull/6126))
- **tests**: Replace deprecated `asyncio.iscoroutinefunction` usage in DevUI cleanup-hook tests ([#4563](https://github.com/microsoft/spark-core/pull/4563))

### Fixed
- **spark-core-core**: Point `@experimental` warnings at user code ([#5996](https://github.com/microsoft/spark-core/pull/5996))
- **spark-core-declarative**: Fix Foreach body exit wiring ([#6050](https://github.com/microsoft/spark-core/pull/6050))
- **spark-core-devui**: Fix streaming memory growth regression ([#6038](https://github.com/microsoft/spark-core/pull/6038))
- **spark-core-foundry**: Pass default headers to Foundry agents ([#6040](https://github.com/microsoft/spark-core/pull/6040))
- **spark-core-foundry-hosting**: Fix hosted handoff argument serialization ([#5861](https://github.com/microsoft/spark-core/pull/5861))
- **spark-core-foundry-hosting**: Allow hosted checkpoints to restore `MessageRole` values ([#6049](https://github.com/microsoft/spark-core/pull/6049))
- **spark-core-openai**: Preserve citation `get_url` metadata ([#6037](https://github.com/microsoft/spark-core/pull/6037))
- **spark-core-openai**: Guard Chat Completions streaming against null deltas ([#5734](https://github.com/microsoft/spark-core/pull/5734))
- **spark-core-openai**: Read response headers defensively for stream wrappers without `.headers` ([#6028](https://github.com/microsoft/spark-core/pull/6028), [#6029](https://github.com/microsoft/spark-core/pull/6029))
- **samples**: Fix sequential workflow sample output handling ([#5976](https://github.com/microsoft/spark-core/pull/5976))

## [1.6.0] - 2026-05-21

### Added
- **spark-core-core**: Shell tool with support for local and Docker execution ([#5664](https://github.com/microsoft/spark-core/pull/5664))
- **spark-core-monty**: New Monty-backed CodeAct provider package ([#5915](https://github.com/microsoft/spark-core/pull/5915))
- **spark-core-foundry**: Add experimental hosted tool factories on `FoundryChatClient` ([#5958](https://github.com/microsoft/spark-core/pull/5958))
- **spark-core-foundry**: Include tool definitions for Foundry agent evals ([#5974](https://github.com/microsoft/spark-core/pull/5974))
- **spark-core-a2a**: Use non-streaming transport and `return_immediately` for background ops ([#5963](https://github.com/microsoft/spark-core/pull/5963))

### Changed
- **spark-core-core**, **spark-core-foundry**: [BREAKING] Enable instrumentation by default ([#5865](https://github.com/microsoft/spark-core/pull/5865))
- **spark-core-foundry**: Show more authentication methods in Foundry Toolbox MCP ([#5719](https://github.com/microsoft/spark-core/pull/5719))

### Fixed
- **spark-core-core**: Skip MCP prompt loading when unsupported ([#5370](https://github.com/microsoft/spark-core/pull/5370))

## [1.5.0] - 2026-05-19

### Added
- **spark-core-core**, **spark-core-foundry**, **spark-core-openai**: Record actual served model from Azure OpenAI ([#5910](https://github.com/microsoft/spark-core/pull/5910))
- **samples**: New Foundry Hosted Agents samples for RAG, Skills, and Memory ([#5822](https://github.com/microsoft/spark-core/pull/5822))

### Changed
- **spark-core-core**, **spark-core-azurefunctions**, **spark-core-devui**, **spark-core-foundry**, **spark-core-orchestrations**: Improve handling of intermediate outputs for workflows and orchestrations ([#5623](https://github.com/microsoft/spark-core/pull/5623))
- **spark-core-durabletask**: Pin `durabletask` and `durabletask-azuremanaged` floors to `>=1.4.0` and exclude upstream `durabletask` 1.4.1, 1.4.2, and 1.4.3 from the supported version range.
- **spark-core-orchestrations**: Bumped package to release candidate stage.

### Fixed
- **spark-core-core**: Parse YAML block scalars in SKILL.md frontmatter ([#5863](https://github.com/microsoft/spark-core/pull/5863))
- **spark-core-github-copilot**: Include tools added by `ContextProvider.before_run` in session creation ([#5780](https://github.com/microsoft/spark-core/pull/5780))
- **spark-core-hyperlight**: Skip symlinks when staging sandbox input ([#5919](https://github.com/microsoft/spark-core/pull/5919))
- **spark-core-purview**: Remove duplicate pop in `InMemoryCacheProvider.remove` ([#5795](https://github.com/microsoft/spark-core/pull/5795))

## [1.4.0] - 2026-05-14

### Added
- **spark-core-core**: Forward MCP tool call metadata ([#5815](https://github.com/microsoft/spark-core/pull/5815))
- **spark-core-core**: Support `list[str]` arguments for file-based skill scripts ([#5850](https://github.com/microsoft/spark-core/pull/5850))
- **spark-core-core**: Strip server-issued response item IDs under storage ([#5690](https://github.com/microsoft/spark-core/pull/5690))
- **spark-core-ag-ui**: Add tool result display channel ([#5762](https://github.com/microsoft/spark-core/pull/5762))
- **spark-core-ag-ui**: Promote to release candidate stage ([#5844](https://github.com/microsoft/spark-core/pull/5844))
- **spark-core-devui**: Improvements for DevUI ([#5840](https://github.com/microsoft/spark-core/pull/5840))

### Changed
- **spark-core-core**: [BREAKING — experimental skills API] Align file skill folder discovery with agentskills.io spec ([#5807](https://github.com/microsoft/spark-core/pull/5807))
- **spark-core-core**: [BREAKING — experimental skills API] Extract skill spec metadata into `SkillFrontmatter` ([#5775](https://github.com/microsoft/spark-core/pull/5775))
- **spark-core-devui**: [BREAKING] Tighten default access controls and CORS posture ([#5740](https://github.com/microsoft/spark-core/pull/5740))
- **spark-core-a2a**: [BREAKING] Migrate to a2a-sdk v1.0 ([#5752](https://github.com/microsoft/spark-core/pull/5752))

### Fixed
- **spark-core-a2a**: Fix A2A v1.0 non-streaming response and sample runtime issues ([#5849](https://github.com/microsoft/spark-core/pull/5849))
- **spark-core-foundry-hosting**: Reject path-traversal context IDs in checkpoint storage ([#5851](https://github.com/microsoft/spark-core/pull/5851))
- **spark-core-core**: Prevent MCP message_handler deadlock on notification reload ([#4866](https://github.com/microsoft/spark-core/pull/4866))

## [1.3.0] - 2026-05-07

### Added
- **spark-core-core**: Add `ClassSkill` for class-based skill definitions with declarative metadata and automatic method discovery ([#5678](https://github.com/microsoft/spark-core/pull/5678))
- **spark-core-core**: Add experimental session-mode harness context provider ([#5611](https://github.com/microsoft/spark-core/pull/5611))
- **spark-core-core**: Add experimental todo-list harness context provider ([#5612](https://github.com/microsoft/spark-core/pull/5612))
- **spark-core-core**: Add experimental memory harness context provider ([#5613](https://github.com/microsoft/spark-core/pull/5613))
- **spark-core-core**: Notify agent of external `AgentModeProvider` mode changes ([#5650](https://github.com/microsoft/spark-core/pull/5650))
- **spark-core-core**: Information-flow control prompt injection defense ([#5331](https://github.com/microsoft/spark-core/pull/5331))
- **spark-core-openai**: Support OpenAI and Gemini `allowed_tools` tool choice ([#5322](https://github.com/microsoft/spark-core/pull/5322))
- **spark-core-openai**: Support GPT-5 verbosity option and restore Foundry `agent_reference` ([#5619](https://github.com/microsoft/spark-core/pull/5619))
- **spark-core-anthropic**: Add `base_url` parameter to `AnthropicClient` and `RawAnthropicClient` ([#5685](https://github.com/microsoft/spark-core/pull/5685))
- **spark-core-foundry-hosting**: Add support for function approval flow in Foundry hosted agent ([#5666](https://github.com/microsoft/spark-core/pull/5666))
- **spark-core-declarative**: Add Python parity for `InvokeMcpTool` in declarative workflow ([#5630](https://github.com/microsoft/spark-core/pull/5630))
- **spark-core-declarative**: Add Python parity for `HttpRequestAction` in declarative workflow ([#5599](https://github.com/microsoft/spark-core/pull/5599))
- **spark-core-claude**, **spark-core-github-copilot**: Enforce `approval_mode` in Claude and GitHub Copilot agents ([#5562](https://github.com/microsoft/spark-core/pull/5562))
- **spark-core-github-copilot**: Upgrade `github-copilot-sdk` to v1.0.0b2 with `instruction_directories`, `copilot_home`, and runtime options forwarding on session resume ([#5665](https://github.com/microsoft/spark-core/pull/5665))
- **samples**: Add hosted agent sample with observability ([#5608](https://github.com/microsoft/spark-core/pull/5608))
- **samples**: Add sample for hosted agent with files ([#5596](https://github.com/microsoft/spark-core/pull/5596))

### Changed
- **spark-core-core**: [BREAKING — experimental skills API] Restructure agent skills to use multi-source architecture ([#5584](https://github.com/microsoft/spark-core/pull/5584))
- **spark-core-foundry**: Remove bespoke Foundry toolbox helpers; standardize on MCP for toolbox consumption ([#5671](https://github.com/microsoft/spark-core/pull/5671))

### Fixed
- **spark-core-core**: Fix `MCPStreamableHTTPTool` leaking `asyncio.CancelledError` when MCP server is unreachable ([#5687](https://github.com/microsoft/spark-core/pull/5687))
- **spark-core-openai**: Drop completed `continuation_token` from shared options in tool loop ([#5462](https://github.com/microsoft/spark-core/pull/5462))
- **spark-core-bedrock**: Don't send `toolChoice` when no tools are configured ([#5172](https://github.com/microsoft/spark-core/pull/5172))
- **spark-core-hyperlight**: Fix `WasmSandbox` cross-thread Drop and harden hosted-agent sample ([#5603](https://github.com/microsoft/spark-core/pull/5603))
- **spark-core-devui**: Fix incorrect workflow timings by adding `created_at` to executor events ([#5615](https://github.com/microsoft/spark-core/pull/5615))
- **spark-core-foundry-hosting**: Fix hosted MCP replay producing orphan `function_call_output` ([#5581](https://github.com/microsoft/spark-core/pull/5581))

## [1.2.2] - 2026-04-29

### Added
- **spark-core-azure-contentunderstanding**: New alpha package — Azure AI Content Understanding context provider that auto-analyzes file attachments (documents, images, audio, video) and injects structured results into the LLM context, with multi-document session state, configurable timeout, output filtering via `AnalysisSection`, and auto-registered `list_documents` / `get_analyzed_document` tools ([#4829](https://github.com/microsoft/spark-core/pull/4829))
- **spark-core-foundry-hosting**: Add hosted Durable Workflow support — propagate full conversation history to workflow agents and wire `Workflow.as_agent()` end-to-end via the foundry hosting layer ([#5531](https://github.com/microsoft/spark-core/pull/5531))

### Changed
- **spark-core-orchestrations**: [BREAKING] Standardize orchestration terminal outputs as `AgentResponse` so `Workflow.as_agent()` returns the final answer only; aligns sequential-approval (`with_request_info`) and concurrent participant output designation flows on the same output contract ([#5301](https://github.com/microsoft/spark-core/pull/5301))
- **spark-core-core**, **spark-core-declarative**: Preserve `Workflow.run()` shared state across calls so multi-turn `WorkflowAgent` invocations retain context, accept `list[Message]` input in the declarative start executor, and coerce `Enum` values when serializing PowerFx symbols ([#5531](https://github.com/microsoft/spark-core/pull/5531))
- **dependencies**: Update workspace package dependencies and preserve `mcp[ws]` / `uvicorn[standard]` extras through override-dependencies in `/python` ([#5555](https://github.com/microsoft/spark-core/pull/5555))

### Fixed
- **spark-core-core**: Fix observability spans not being correctly nested when using streaming ([#5552](https://github.com/microsoft/spark-core/pull/5552))
- **spark-core-openai**: Fix `file_search` citations breaking the assistant-message history roundtrip — skip `hosted_file` content in the assistant role so the Responses API no longer rejects `input_file` ([#5557](https://github.com/microsoft/spark-core/pull/5557))

## [1.2.1] - 2026-04-28

### Added
- **spark-core-foundry-hosting**: Add file data type support to hosted-agent Responses, refresh `foundry-hosted-agents` samples, and add response test coverage ([#5485](https://github.com/microsoft/spark-core/pull/5485))
- **samples**: Add `requirements.txt` and `.env.example` to the `a2a/` hosting sample for pip-based setup ([#5510](https://github.com/microsoft/spark-core/pull/5510))

### Changed
- **dependencies**: Update `rich` requirement from `<15.0.0,>=13.7.1` to `>=13.7.1,<16.0.0` in `/python` ([#5227](https://github.com/microsoft/spark-core/pull/5227))
- **dependencies**: Bump `prek` from `0.3.8` to `0.3.9` in `/python` ([#5228](https://github.com/microsoft/spark-core/pull/5228))
- **dependencies**: Bump `python-multipart` from `0.0.22` to `0.0.26` in `/python` ([#5286](https://github.com/microsoft/spark-core/pull/5286))
- **dependencies**: Bump `pyasn1` from `0.6.2` to `0.6.3` in `/python` ([#4748](https://github.com/microsoft/spark-core/pull/4748))
- **dependencies**: Bump `pytest` from `9.0.2` to `9.0.3` in `/python/packages/ag-ui` ([#5461](https://github.com/microsoft/spark-core/pull/5461))
- **dependencies**: Bump `pytest` from `9.0.2` to `9.0.3` in `/python/packages/devui` ([#5492](https://github.com/microsoft/spark-core/pull/5492))
- **dependencies**: Bump `pytest` from `9.0.2` to `9.0.3` in `/python/packages/lab` ([#5470](https://github.com/microsoft/spark-core/pull/5470))
- **dependencies**: Bump `uv` from `0.11.3` to `0.11.6` in `/python/packages/lab` ([#5469](https://github.com/microsoft/spark-core/pull/5469))
- **dependencies**: Bump `vite` from `7.1.12` to `7.3.2` in `/python/packages/devui/frontend` ([#5127](https://github.com/microsoft/spark-core/pull/5127))
- **dependencies**: Bump `vite` from `7.1.12` to `7.3.2` in `/python/samples/05-end-to-end/chatkit-integration/frontend` ([#5126](https://github.com/microsoft/spark-core/pull/5126))
- **dependencies**: Bump `postcss` from `8.5.6` to `8.5.10` in `/python/packages/devui/frontend` ([#5484](https://github.com/microsoft/spark-core/pull/5484))
- **dependencies**: Bump `postcss` from `8.5.6` to `8.5.10` in `/python/samples/05-end-to-end/chatkit-integration/frontend` ([#5491](https://github.com/microsoft/spark-core/pull/5491))
- **dependencies**: Bump `postcss` from `8.5.6` to `8.5.12` in `/python/samples/05-end-to-end/ag_ui_workflow_handoff/frontend` ([#5527](https://github.com/microsoft/spark-core/pull/5527))
- **dependencies**: Bump `picomatch` from `4.0.3` to `4.0.4` in `/python/packages/devui/frontend` ([#4921](https://github.com/microsoft/spark-core/pull/4921))
- **dependencies**: Bump `picomatch` from `4.0.3` to `4.0.4` in `/python/samples/05-end-to-end/ag_ui_workflow_handoff/frontend` ([#4936](https://github.com/microsoft/spark-core/pull/4936))

### Fixed
- **spark-core-core**: Prevent `inner_exception` from being lost in `SparkCoreException` ([#5167](https://github.com/microsoft/spark-core/pull/5167))

## [1.2.0] - 2026-04-24

### Added
- **spark-core-core**: Add functional workflow API ([#4238](https://github.com/microsoft/spark-core/pull/4238))
- **spark-core-core**, **spark-core-github-copilot**: Add OpenTelemetry integration for `GitHubCopilotAgent` ([#5142](https://github.com/microsoft/spark-core/pull/5142))
- **spark-core-a2a**: Add Spark Core to A2A bridge support ([#2403](https://github.com/microsoft/spark-core/pull/2403))
- **spark-core-foundry**: Surface `oauth_consent_request` events from Responses API in Foundry clients ([#5070](https://github.com/microsoft/spark-core/pull/5070))

### Changed
- **spark-core-core**, **spark-core-foundry**: Update `FoundryAgent` for hosted agent sessions ([#5447](https://github.com/microsoft/spark-core/pull/5447))
- **spark-core-foundry-hosting**: Upgrade hosting server dependency and add more type support ([#5459](https://github.com/microsoft/spark-core/pull/5459))

### Fixed
- **spark-core-ag-ui**: Fix reasoning role and multimodal media parsing to follow specification ([#5389](https://github.com/microsoft/spark-core/pull/5389))
- **spark-core-foundry**: Stop emitting `[TOOLBOXES]` warning for every `FoundryChatClient` call ([#5440](https://github.com/microsoft/spark-core/pull/5440))
- **spark-core-anthropic**, **spark-core-azure-ai-search**, **spark-core-azure-cosmos**: Fix user agent prefix ([#5455](https://github.com/microsoft/spark-core/pull/5455))

## [1.1.1] - 2026-04-23

### Added
- **spark-core-core**: Add `expected_output` ground-truth support to `evaluate_workflow` for similarity evaluators ([#5234](https://github.com/microsoft/spark-core/pull/5234))
- **spark-core-ag-ui**, **spark-core-a2a**: Propagate `thread_id` and `forwarded_props` through AG-UI to A2A `context_id` ([#5383](https://github.com/microsoft/spark-core/pull/5383))
- **samples**: Add second approval-required tool (`set_stop_loss`) to `concurrent_builder_tool_approval` sample ([#4875](https://github.com/microsoft/spark-core/pull/4875))
- **spark-core-core**: Add `SKIP_PARSING` sentinel for `FunctionTool.invoke` to bypass `Content`-wrapping and return raw function results ([#5424](https://github.com/microsoft/spark-core/pull/5424))

### Changed
- **spark-core-foundry-hosting**: Correct Development Status classifier from Beta (4) to Alpha (3) to match the package's lifecycle stage ([#5387](https://github.com/microsoft/spark-core/pull/5387))
- **tests**: Add Python flaky test report workflow ([#5342](https://github.com/microsoft/spark-core/pull/5342))
- **spark-core-hyperlight**: Simplify host callback to pass raw Python results via `SKIP_PARSING`, switch `execute_code` input schema to a plain JSON-schema dict, and tighten public API surface ([#5424](https://github.com/microsoft/spark-core/pull/5424))

### Fixed
- **spark-core-openai**: Fix OpenAI Responses streaming to propagate `created_at` from the final `response.completed` event ([#5382](https://github.com/microsoft/spark-core/pull/5382))
- **spark-core-openai**: Fix `OpenAIEmbeddingClient` to use `AsyncOpenAI` for `/openai/v1` endpoints ([#5137](https://github.com/microsoft/spark-core/pull/5137))
- **spark-core-openai**: Exclude null `file_id` from `input_image` payload to prevent schema 400 errors ([#5125](https://github.com/microsoft/spark-core/pull/5125))
- **spark-core-foundry**: Reconcile Toolbox hosted-tool payloads with the Responses API ([#5414](https://github.com/microsoft/spark-core/pull/5414))
- **spark-core-ag-ui**: Pass client `thread_id` as `session_id` when constructing `AgentSession` ([#5384](https://github.com/microsoft/spark-core/pull/5384))
- **spark-core-hyperlight**: Thread-confine `WasmSandbox` interactions via per-entry `ThreadPoolExecutor` to eliminate the PyO3 `unsendable` panic when touched from asyncio worker threads ([#5424](https://github.com/microsoft/spark-core/pull/5424))

## [1.1.0] - 2026-04-21

### Added
- **spark-core-gemini**: Add `GeminiChatClient` ([#4847](https://github.com/microsoft/spark-core/pull/4847))
- **spark-core-core**: Add `context_providers` and `description` to `workflow.as_agent()` ([#4651](https://github.com/microsoft/spark-core/pull/4651))
- **spark-core-core**: Add experimental file history provider ([#5248](https://github.com/microsoft/spark-core/pull/5248))
- **spark-core-core**: Add OpenAI types to the default checkpoint encoding allow list ([#5297](https://github.com/microsoft/spark-core/pull/5297))
- **spark-core-core**: Add `AgentExecutorResponse.with_text()` to preserve conversation history through custom executors ([#5255](https://github.com/microsoft/spark-core/pull/5255))
- **spark-core-a2a**: Propagate A2A metadata from `Message`, `Artifact`, `Task`, and event types ([#5256](https://github.com/microsoft/spark-core/pull/5256))
- **spark-core-core**: Add `finish_reason` support to `AgentResponse` and `AgentResponseUpdate` ([#5211](https://github.com/microsoft/spark-core/pull/5211))
- **spark-core-hyperlight**: Add Hyperlight CodeAct package and docs ([#5185](https://github.com/microsoft/spark-core/pull/5185))
- **spark-core-openai**: Add search tool content support for OpenAI responses ([#5302](https://github.com/microsoft/spark-core/pull/5302))
- **spark-core-foundry**: Add support for Foundry Toolboxes ([#5346](https://github.com/microsoft/spark-core/pull/5346))
- **spark-core-ag-ui**: Expose `forwardedProps` to agents and tools via session metadata ([#5264](https://github.com/microsoft/spark-core/pull/5264))
- **spark-core-foundry**: Add hosted agent V2 support ([#5379](https://github.com/microsoft/spark-core/pull/5379))

### Changed
- **spark-core-azure-cosmos**: [BREAKING] `CosmosCheckpointStorage` now uses restricted pickle deserialization by default, matching `FileCheckpointStorage` behavior. If your checkpoints contain application-defined types, pass them via `allowed_checkpoint_types=["my_app.models:MyState"]`. ([#5200](https://github.com/microsoft/spark-core/issues/5200))
- **spark-core-core**: Improve skill name validation ([#4530](https://github.com/microsoft/spark-core/pull/4530))
- **spark-core-azure-cosmos**: Add `allowed_checkpoint_types` support to `CosmosCheckpointStorage` for parity with `FileCheckpointStorage` ([#5202](https://github.com/microsoft/spark-core/pull/5202))
- **spark-core-core**: Move `InMemory` history provider injection to first invocation ([#5236](https://github.com/microsoft/spark-core/pull/5236))
- **spark-core-github-copilot**: Forward provider config to `SessionConfig` in `GitHubCopilotAgent` ([#5195](https://github.com/microsoft/spark-core/pull/5195))
- **spark-core-hyperlight-codeact**: Flatten `execute_code` output ([#5333](https://github.com/microsoft/spark-core/pull/5333))
- **dependencies**: Bump `pygments` from `2.19.2` to `2.20.0` in `/python` ([#4978](https://github.com/microsoft/spark-core/pull/4978))
- **tests**: Bump misc integration retry delay to 30s ([#5293](https://github.com/microsoft/spark-core/pull/5293))
- **tests**: Improve misc integration test robustness ([#5295](https://github.com/microsoft/spark-core/pull/5295))
- **tests**: Skip hosted tools test on transient upstream MCP errors ([#5296](https://github.com/microsoft/spark-core/pull/5296))

### Fixed
- **spark-core-core**: Fix `python-feature-lifecycle` skill YAML frontmatter ([#5226](https://github.com/microsoft/spark-core/pull/5226))
- **spark-core-core**: Fix `HandoffBuilder` dropping function-level middleware when cloning agents ([#5220](https://github.com/microsoft/spark-core/pull/5220))
- **spark-core-ag-ui**: Fix deterministic state updates from tool results ([#5201](https://github.com/microsoft/spark-core/pull/5201))
- **spark-core-devui**: Fix streaming memory growth and add cross-platform regression coverage ([#5221](https://github.com/microsoft/spark-core/pull/5221))
- **spark-core-core**: Skip `get_final_response` in `_finalize_stream` when the stream has errored ([#5232](https://github.com/microsoft/spark-core/pull/5232))
- **spark-core-openai**: Fix reasoning replay when `store=False` ([#5250](https://github.com/microsoft/spark-core/pull/5250))
- **spark-core-foundry**: Handle `url_citation` annotations in `FoundryChatClient` streaming responses ([#5071](https://github.com/microsoft/spark-core/pull/5071))
- **spark-core-gemini**: Fix Gemini client support for Gemini API and Vertex AI ([#5258](https://github.com/microsoft/spark-core/pull/5258))
- **spark-core-copilotstudio**: Fix `CopilotStudioAgent` to reuse conversation ID from an existing session ([#5299](https://github.com/microsoft/spark-core/pull/5299))

## [devui-1.0.0b260414] - 2026-04-14

### Fixed
- **spark-core-devui**: Fix streaming memory growth in DevUI frontend ([#5221](https://github.com/microsoft/spark-core/pull/5221))

## [1.0.1] - 2026-04-09

### Added
- **samples**: Add sample documentation for two separate Neo4j context providers for retrieval and memory ([#4010](https://github.com/microsoft/spark-core/pull/4010))
- **spark-core-azure-cosmos**: Add Cosmos DB NoSQL checkpoint storage for Python workflows ([#4916](https://github.com/microsoft/spark-core/pull/4916))

### Changed
- **docs**: Remove pre-release flag from spark-core installation instructions ([#5082](https://github.com/microsoft/spark-core/pull/5082))
- **samples**: Revise agent examples in `README.md` ([#5067](https://github.com/microsoft/spark-core/pull/5067))
- **repo**: Update `CHANGELOG` with v1.0.0 release ([#5069](https://github.com/microsoft/spark-core/pull/5069))
- **spark-core-orchestrations**: [BREAKING] Fix handoff workflow context management and improve AG-UI demo ([#5136](https://github.com/microsoft/spark-core/pull/5136))
- **spark-core-core**: Restrict persisted checkpoint deserialization by default ([#4941](https://github.com/microsoft/spark-core/pull/4941))
- **samples**: Bump `vite` from 7.3.1 to 7.3.2 in `/python/samples/05-end-to-end/ag_ui_workflow_handoff/frontend` ([#5132](https://github.com/microsoft/spark-core/pull/5132))
- **python**: Bump `cryptography` from 46.0.6 to 46.0.7 ([#5176](https://github.com/microsoft/spark-core/pull/5176))
- **python**: Bump `mcp` from 1.26.0 to 1.27.0 ([#5117](https://github.com/microsoft/spark-core/pull/5117))
- **python**: Bump `mcp[ws]` from 1.26.0 to 1.27.0 ([#5119](https://github.com/microsoft/spark-core/pull/5119))

### Fixed
- **spark-core-core**: Raise clear handler registration error for unresolved `TypeVar` annotations ([#4944](https://github.com/microsoft/spark-core/pull/4944))
- **spark-core-openai**: Fix `response_format` crash on background polling with empty text ([#5146](https://github.com/microsoft/spark-core/pull/5146))
- **spark-core-foundry**: Strip tools from `FoundryAgent` request when `agent_reference` is present ([#5101](https://github.com/microsoft/spark-core/pull/5101))
- **spark-core-core**: Fix test compatibility for entity key validation ([#5179](https://github.com/microsoft/spark-core/pull/5179))
- **spark-core-openai**: Stop emitting duplicate reasoning content from `response.reasoning_text.done` and `response.reasoning_summary_text.done` events ([#5162](https://github.com/microsoft/spark-core/pull/5162))


## [1.0.0] - 2026-04-02

### Added

- **repo**: Add `PACKAGE_STATUS.md` to track lifecycle status of all Python packages ([#5062](https://github.com/microsoft/spark-core/pull/5062))

### Changed

- **spark-core**, **spark-core-core**, **spark-core-openai**, **spark-core-foundry**: [BREAKING] Promote from `1.0.0rc6` to `1.0.0` (Production/Stable) ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **spark-core-core**, **spark-core-openai**, **spark-core-foundry**: [BREAKING] Dependency floors now require released `>=1.0.0,<2` packages, breaking compatibility with older RC installs ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **spark-core-a2a**, **spark-core-ag-ui**, **spark-core-anthropic**, **spark-core-azure-ai-search**, **spark-core-azure-cosmos**, **spark-core-azurefunctions**, **spark-core-bedrock**, **spark-core-chatkit**, **spark-core-claude**, **spark-core-copilotstudio**, **spark-core-declarative**, **spark-core-devui**, **spark-core-durabletask**, **spark-core-foundry-local**, **spark-core-github-copilot**, **spark-core-lab**, **spark-core-mem0**, **spark-core-ollama**, **spark-core-orchestrations**, **spark-core-purview**, **spark-core-redis**: Bump beta versions from `1.0.0b260330` to `1.0.0b260402` ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **docs**: Update install instructions to drop `--pre` flag for released packages ([#5062](https://github.com/microsoft/spark-core/pull/5062))

### Removed

- **spark-core-core**: [BREAKING] Remove deprecated `BaseContextProvider` and `BaseHistoryProvider` aliases ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **spark-core-core**: [BREAKING] Remove deprecated `text` parameter from `Message` constructor ([#5062](https://github.com/microsoft/spark-core/pull/5062))

### Fixed

- **spark-core-core**, **spark-core-openai**, **spark-core-foundry**, **spark-core-azurefunctions**, **spark-core-devui**, **spark-core-orchestrations**, **spark-core-azure-ai-search**: Migrate message construction from `Message(text=...)` to `Message(contents=[...])` throughout codebase ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **spark-core-devui**: Accept legacy payload formats (`text`, `message`, `content`, `input`, `data`) and convert to framework-native `Message(contents=...)` ([#5062](https://github.com/microsoft/spark-core/pull/5062))
- **samples**: Fix Foundry samples to use env vars consistently and update install guidance ([#5062](https://github.com/microsoft/spark-core/pull/5062))

## [1.0.0rc6] - 2026-03-30

### Added

- **spark-core-openai**: New package extracted from core for OpenAI and Azure OpenAI provider support ([#4818](https://github.com/microsoft/spark-core/pull/4818))
- **spark-core-foundry**: New package for Microsoft Foundry integration ([#4818](https://github.com/microsoft/spark-core/pull/4818))
- **spark-core-core**: Support `structuredContent` in MCP tool results and fix sampling options type ([#4763](https://github.com/microsoft/spark-core/pull/4763))
- **spark-core-core**: Include reasoning messages in `MESSAGES_SNAPSHOT` events ([#4844](https://github.com/microsoft/spark-core/pull/4844))
- **spark-core-core**: [BREAKING] Add context mode to `AgentExecutor` ([#4668](https://github.com/microsoft/spark-core/pull/4668))

### Changed

- **spark-core-core**: [BREAKING] Remove deprecated kwargs compatibility paths ([#4858](https://github.com/microsoft/spark-core/pull/4858))
- **spark-core-core**: [BREAKING] Reduce core dependencies and simplify optional integrations ([#4904](https://github.com/microsoft/spark-core/pull/4904))
- **spark-core-openai**: [BREAKING] Provider-leading client design & OpenAI package extraction ([#4818](https://github.com/microsoft/spark-core/pull/4818))
- **spark-core-openai**: [BREAKING] Fix OpenAI Azure routing and provider samples ([#4925](https://github.com/microsoft/spark-core/pull/4925))
- **spark-core-azure-ai**: Deprecate Azure AI v1 (Persistent Agents API) helper methods ([#4804](https://github.com/microsoft/spark-core/pull/4804))
- **spark-core-core**: Avoid duplicate agent response telemetry ([#4685](https://github.com/microsoft/spark-core/pull/4685))
- **spark-core-devui**: Bump `flatted` from 3.3.3 to 3.4.2 in frontend ([#4805](https://github.com/microsoft/spark-core/pull/4805))
- **samples**: Move `ag_ui_workflow_handoff` demo from `demos/` to `05-end-to-end/` ([#4900](https://github.com/microsoft/spark-core/pull/4900))

### Fixed

- **spark-core-core**: Fix streaming path to emit `mcp_server_tool_result` on `output_item.done` instead of `output_item.added` ([#4821](https://github.com/microsoft/spark-core/pull/4821))
- **spark-core-a2a**: Fix `A2AAgent` to surface message content from in-progress `TaskStatusUpdateEvents` ([#4798](https://github.com/microsoft/spark-core/pull/4798))
- **spark-core-core**: Fix `PydanticSchemaGenerationError` when using `from __future__ import annotations` with `@tool` ([#4822](https://github.com/microsoft/spark-core/pull/4822))
- **samples**: Fix broken samples for GitHub Copilot, declarative, and Responses API ([#4915](https://github.com/microsoft/spark-core/pull/4915))
- **repo**: Fix: update PyRIT repository link from Azure/PyRIT to microsoft/PyRIT ([#4960](https://github.com/microsoft/spark-core/pull/4960))

## [1.0.0rc5] - 2026-03-19

### Added

- **samples**: Add foundry hosted agents samples for python ([#4648](https://github.com/microsoft/spark-core/pull/4648))
- **repo**: Add automated stale issue and PR follow-up ping workflow ([#4776](https://github.com/microsoft/spark-core/pull/4776))
- **spark-core-ag-ui**: Emit AG-UI events for MCP tool calls, results, and text reasoning ([#4760](https://github.com/microsoft/spark-core/pull/4760))
- **spark-core-ag-ui**: Emit TOOL_CALL_RESULT events when resuming after tool approval ([#4758](https://github.com/microsoft/spark-core/pull/4758))

### Changed

- **spark-core-devui**: Bump minimatch from 3.1.2 to 3.1.5 in frontend ([#4337](https://github.com/microsoft/spark-core/pull/4337))
- **spark-core-devui**: Bump rollup from 4.47.1 to 4.59.0 in frontend ([#4338](https://github.com/microsoft/spark-core/pull/4338))
- **spark-core-core**: Unify tool results as `Content` items with rich content support ([#4331](https://github.com/microsoft/spark-core/pull/4331))
- **spark-core-a2a**: Default `A2AAgent` name and description from `AgentCard` ([#4661](https://github.com/microsoft/spark-core/pull/4661))
- **spark-core-core**: [BREAKING] Clean up kwargs across agents, chat clients, tools, and sessions ([#4581](https://github.com/microsoft/spark-core/pull/4581))
- **spark-core-devui**: Bump tar from 7.5.9 to 7.5.11 ([#4688](https://github.com/microsoft/spark-core/pull/4688))
- **repo**: Improve Python dependency range automation ([#4343](https://github.com/microsoft/spark-core/pull/4343))
- **spark-core-core**: Normalize empty MCP tool output to `null` ([#4683](https://github.com/microsoft/spark-core/pull/4683))
- **spark-core-core**: Remove bad dependency ([#4696](https://github.com/microsoft/spark-core/pull/4696))
- **spark-core-core**: Keep MCP cleanup on the owner task ([#4687](https://github.com/microsoft/spark-core/pull/4687))
- **spark-core-a2a**: Preserve A2A message `context_id` ([#4686](https://github.com/microsoft/spark-core/pull/4686))
- **repo**: Bump `danielpalme/ReportGenerator-GitHub-Action` from 5.5.1 to 5.5.3 ([#4542](https://github.com/microsoft/spark-core/pull/4542))
- **repo**: Bump `MishaKav/pytest-coverage-comment` from 1.2.0 to 1.6.0 ([#4543](https://github.com/microsoft/spark-core/pull/4543))
- **spark-core-core**: Bump `pyjwt` from 2.11.0 to 2.12.0 ([#4699](https://github.com/microsoft/spark-core/pull/4699))
- **spark-core-azure-ai**: Reduce Azure chat client import overhead ([#4744](https://github.com/microsoft/spark-core/pull/4744))
- **repo**: Simplify Python Poe tasks and unify package selectors ([#4722](https://github.com/microsoft/spark-core/pull/4722))
- **spark-core-core**: Aggregate token usage across tool-call loop iterations in `invoke_agent` span ([#4739](https://github.com/microsoft/spark-core/pull/4739))
- **spark-core-core**: Support `detail` field in OpenAI Chat API `image_url` payload ([#4756](https://github.com/microsoft/spark-core/pull/4756))
- **spark-core-anthropic**: [BREAKING] Refactor middleware layering and split Anthropic raw client ([#4746](https://github.com/microsoft/spark-core/pull/4746))
- **spark-core-github-copilot**: Emit tool call events in GitHubCopilotAgent streaming ([4711](https://github.com/microsoft/spark-core/pull/4711))

### Fixed

- **spark-core-core**: Validate approval responses against the server-side pending request registry ([#4548](https://github.com/microsoft/spark-core/pull/4548))
- **spark-core-devui**: Validate function approval responses in the DevUI executor ([#4598](https://github.com/microsoft/spark-core/pull/4598))
- **spark-core-azurefunctions**: Use `deepcopy` for state snapshots so nested mutations are detected in durable workflow activities ([#4518](https://github.com/microsoft/spark-core/pull/4518))
- **spark-core-bedrock**: Fix `BedrockChatClient` sending invalid toolChoice `"none"` to the Bedrock API ([#4535](https://github.com/microsoft/spark-core/pull/4535))
- **spark-core-core**: Fix type hint for `Case` and `Default` ([#3985](https://github.com/microsoft/spark-core/pull/3985))
- **spark-core-core**: Fix duplicate tool names between supplied tools and MCP servers ([#4649](https://github.com/microsoft/spark-core/pull/4649))
- **spark-core-core**: Fix `_deduplicate_messages` catch-all branch dropping valid repeated messages ([#4716](https://github.com/microsoft/spark-core/pull/4716))
- **samples**: Fix Azure Redis sample missing session for history persistence ([#4692](https://github.com/microsoft/spark-core/pull/4692))
- **spark-core-core**: Fix thread serialization for multi-turn tool calls ([#4684](https://github.com/microsoft/spark-core/pull/4684))
- **spark-core-core**: Fix `RUN_FINISHED.interrupt` to accumulate all interrupts when multiple tools need approval ([#4717](https://github.com/microsoft/spark-core/pull/4717))
- **spark-core-azurefunctions**: Fix missing methods on the `Content` class in durable tasks ([#4738](https://github.com/microsoft/spark-core/pull/4738))
- **spark-core-core**: Fix `ENABLE_SENSITIVE_DATA` being ignored when set after module import ([#4743](https://github.com/microsoft/spark-core/pull/4743))
- **spark-core-a2a**: Fix `A2AAgent` to invoke context providers before and after run ([#4757](https://github.com/microsoft/spark-core/pull/4757))
- **spark-core-core**: Fix MCP tool schema normalization for zero-argument tools missing the `properties` key ([#4771](https://github.com/microsoft/spark-core/pull/4771))

## [1.0.0rc4] - 2026-03-11

### Added

- **spark-core-core**: Add `propagate_session` to `as_tool()` for session sharing in agent-as-tool scenarios ([#4439](https://github.com/microsoft/spark-core/pull/4439))
- **spark-core-core**: Forward runtime kwargs to skill resource functions ([#4417](https://github.com/microsoft/spark-core/pull/4417))
- **samples**: Add A2A server sample ([#4528](https://github.com/microsoft/spark-core/pull/4528))

### Changed

- **spark-core-github-copilot**: [BREAKING] Update integration to use `ToolInvocation` and `ToolResult` types ([#4551](https://github.com/microsoft/spark-core/pull/4551))
- **spark-core-azure-ai**: [BREAKING] Upgrade to `azure-ai-projects` 2.0+ ([#4536](https://github.com/microsoft/spark-core/pull/4536))

### Fixed

- **spark-core-core**: Propagate MCP `isError` flag through the function middleware pipeline ([#4511](https://github.com/microsoft/spark-core/pull/4511))
- **spark-core-core**: Fix `as_agent()` not defaulting name/description from client properties ([#4484](https://github.com/microsoft/spark-core/pull/4484))
- **spark-core-core**: Exclude `conversation_id` from chat completions API options ([#4517](https://github.com/microsoft/spark-core/pull/4517))
- **spark-core-core**: Fix conversation ID propagation when `chat_options` is a dict ([#4340](https://github.com/microsoft/spark-core/pull/4340))
- **spark-core-core**: Auto-finalize `ResponseStream` on iteration completion ([#4478](https://github.com/microsoft/spark-core/pull/4478))
- **spark-core-core**: Prevent pickle deserialization of untrusted HITL HTTP input ([#4566](https://github.com/microsoft/spark-core/pull/4566))
- **spark-core-core**: Fix `executor_completed` event handling for non-copyable `raw_representation` in mixed workflows ([#4493](https://github.com/microsoft/spark-core/pull/4493))
- **spark-core-core**: Fix `store=False` not overriding client default ([#4569](https://github.com/microsoft/spark-core/pull/4569))
- **spark-core-redis**: Fix `RedisContextProvider` compatibility with redisvl 0.14.0 by using `AggregateHybridQuery` ([#3954](https://github.com/microsoft/spark-core/pull/3954))
- **samples**: Fix `chat_response_cancellation` sample to use `Message` objects ([#4532](https://github.com/microsoft/spark-core/pull/4532))
- **spark-core-purview**: Fix broken link in Purview README (Microsoft 365 Dev Program URL) ([#4610](https://github.com/microsoft/spark-core/pull/4610))

## [1.0.0rc3] - 2026-03-04

### Added

- **spark-core-core**: Add Shell tool ([#4339](https://github.com/microsoft/spark-core/pull/4339))
- **spark-core-core**: Add `file_ids` and `data_sources` support to `get_code_interpreter_tool()` ([#4201](https://github.com/microsoft/spark-core/pull/4201))
- **spark-core-core**: Map file citation annotations from `TextDeltaBlock` in Assistants API streaming ([#4316](https://github.com/microsoft/spark-core/pull/4316), [#4320](https://github.com/microsoft/spark-core/pull/4320))
- **spark-core-claude**: Add OpenTelemetry instrumentation to `ClaudeAgent` ([#4278](https://github.com/microsoft/spark-core/pull/4278), [#4326](https://github.com/microsoft/spark-core/pull/4326))
- **spark-core-azure-cosmos**: Add Azure Cosmos history provider package ([#4271](https://github.com/microsoft/spark-core/pull/4271))
- **samples**: Add `auto_retry.py` sample for rate limit handling ([#4223](https://github.com/microsoft/spark-core/pull/4223))
- **tests**: Add regression tests for Entry JoinExecutor workflow input initialization ([#4335](https://github.com/microsoft/spark-core/pull/4335))

### Changed

- **samples**: Restructure and improve Python samples ([#4092](https://github.com/microsoft/spark-core/pull/4092))
- **spark-core-orchestrations**: [BREAKING] Tighten `HandoffBuilder` to require `Agent` instead of `SupportsAgentRun` ([#4301](https://github.com/microsoft/spark-core/pull/4301), [#4302](https://github.com/microsoft/spark-core/pull/4302))
- **samples**: Update workflow orchestration samples to use `AzureOpenAIResponsesClient` ([#4285](https://github.com/microsoft/spark-core/pull/4285))

### Fixed

- **spark-core-bedrock**: Fix embedding test stub missing `meta` attribute ([#4287](https://github.com/microsoft/spark-core/pull/4287))
- **spark-core-ag-ui**: Fix approval payloads being re-processed on subsequent conversation turns ([#4232](https://github.com/microsoft/spark-core/pull/4232))
- **spark-core-core**: Fix `response_format` resolution in streaming finalizer ([#4291](https://github.com/microsoft/spark-core/pull/4291))
- **spark-core-core**: Strip reserved kwargs in `AgentExecutor` to prevent duplicate-argument `TypeError` ([#4298](https://github.com/microsoft/spark-core/pull/4298))
- **spark-core-core**: Preserve workflow run kwargs when continuing with `run(responses=...)` ([#4296](https://github.com/microsoft/spark-core/pull/4296))
- **spark-core-core**: Fix `WorkflowAgent` not persisting response messages to session history ([#4319](https://github.com/microsoft/spark-core/pull/4319))
- **spark-core-core**: Fix single-tool input handling in `OpenAIResponsesClient._prepare_tools_for_openai` ([#4312](https://github.com/microsoft/spark-core/pull/4312))
- **spark-core-core**: Fix agent option merge to support dict-defined tools ([#4314](https://github.com/microsoft/spark-core/pull/4314))
- **spark-core-core**: Fix executor handler type resolution when using `from __future__ import annotations` ([#4317](https://github.com/microsoft/spark-core/pull/4317))
- **spark-core-core**: Fix walrus operator precedence for `model_id` kwarg in `AzureOpenAIResponsesClient` ([#4310](https://github.com/microsoft/spark-core/pull/4310))
- **spark-core-core**: Handle `thread.message.completed` event in Assistants API streaming ([#4333](https://github.com/microsoft/spark-core/pull/4333))
- **spark-core-core**: Fix MCP tools duplicated on second turn when runtime tools are present ([#4432](https://github.com/microsoft/spark-core/pull/4432))
- **spark-core-core**: Fix PowerFx eval crash on non-English system locales by setting `CurrentUICulture` to `en-US` ([#4408](https://github.com/microsoft/spark-core/pull/4408))
- **spark-core-orchestrations**: Fix `StandardMagenticManager` to propagate session to manager agent ([#4409](https://github.com/microsoft/spark-core/pull/4409))
- **spark-core-orchestrations**: Fix `IndexError` when reasoning models produce reasoning-only messages in Magentic-One workflow ([#4413](https://github.com/microsoft/spark-core/pull/4413))
- **spark-core-azure-ai**: Fix parsing `oauth_consent_request` events in Azure AI client ([#4197](https://github.com/microsoft/spark-core/pull/4197))
- **spark-core-anthropic**: Set `role="assistant"` on `message_start` streaming update ([#4329](https://github.com/microsoft/spark-core/pull/4329))
- **samples**: Fix samples discovered by auto validation pipeline ([#4355](https://github.com/microsoft/spark-core/pull/4355))
- **samples**: Use `AgentResponse.value` instead of `model_validate_json` in HITL sample ([#4405](https://github.com/microsoft/spark-core/pull/4405))
- **spark-core-devui**: Fix .NET conversation memory handling in DevUI integration ([#3484](https://github.com/microsoft/spark-core/pull/3484), [#4294](https://github.com/microsoft/spark-core/pull/4294))

## [1.0.0rc2] - 2026-02-25

### Added

- **spark-core-core**: Support Agent Skills ([#4210](https://github.com/microsoft/spark-core/pull/4210))
- **spark-core-core**: Add embedding abstractions and OpenAI implementation (Phase 1) ([#4153](https://github.com/microsoft/spark-core/pull/4153))
- **spark-core-core**: Add Foundry Memory Context Provider ([#3943](https://github.com/microsoft/spark-core/pull/3943))
- **spark-core-core**: Add `max_function_calls` to `FunctionInvocationConfiguration` ([#4175](https://github.com/microsoft/spark-core/pull/4175))
- **spark-core-core**: Add `CreateConversationExecutor`, fix input routing, remove unused handler layer ([#4159](https://github.com/microsoft/spark-core/pull/4159))
- **spark-core-azure-ai-search**: Azure AI Search provider improvements - EmbeddingGenerator, async context manager, KB message handling ([#4212](https://github.com/microsoft/spark-core/pull/4212))
- **spark-core-azure-ai-search**: Enhance Azure AI Search Citations with Document URLs in Foundry V2 ([#4028](https://github.com/microsoft/spark-core/pull/4028))
- **spark-core-ag-ui**: Add Workflow Support, Harden Streaming Semantics, and add Dynamic Handoff Demo ([#3911](https://github.com/microsoft/spark-core/pull/3911))

### Changed

- **spark-core-declarative**: [BREAKING] Add `InvokeFunctionTool` action for declarative workflows ([#3716](https://github.com/microsoft/spark-core/pull/3716))

### Fixed

- **spark-core-core**: Fix thread corruption when `max_iterations` is reached ([#4234](https://github.com/microsoft/spark-core/pull/4234))
- **spark-core-core**: Fix workflow runner concurrent processing ([#4143](https://github.com/microsoft/spark-core/pull/4143))
- **spark-core-core**: Fix doubled `tool_call` arguments in `MESSAGES_SNAPSHOT` when streaming ([#4200](https://github.com/microsoft/spark-core/pull/4200))
- **spark-core-core**: Fix OpenAI chat client compatibility with third-party endpoints and OTel 0.4.14 ([#4161](https://github.com/microsoft/spark-core/pull/4161))
- **spark-core-claude**: Fix `structured_output` propagation in `ClaudeAgent` ([#4137](https://github.com/microsoft/spark-core/pull/4137))

## [1.0.0rc1] - 2026-02-19

Release candidate for **spark-core-core** and **spark-core-azure-ai** packages.

### Added

- **spark-core-core**: Add default in-memory history provider for workflow agents ([#3918](https://github.com/microsoft/spark-core/pull/3918))
- **spark-core-core**: Durable support for workflows ([#3630](https://github.com/microsoft/spark-core/pull/3630))

### Changed

- **spark-core-core**: [BREAKING] Scope provider state by `source_id` and standardize source IDs ([#3995](https://github.com/microsoft/spark-core/pull/3995))
- **spark-core-core**: [BREAKING] Fix chat/agent message typing alignment ([#3920](https://github.com/microsoft/spark-core/pull/3920))
- **spark-core-core**: [BREAKING] Remove `FunctionTool[Any]` compatibility shim for schema passthrough ([#3907](https://github.com/microsoft/spark-core/pull/3907))
- **spark-core-core**: Inject OpenTelemetry trace context into MCP requests ([#3780](https://github.com/microsoft/spark-core/pull/3780))
- **spark-core-core**: Replace wildcard imports with explicit imports ([#3908](https://github.com/microsoft/spark-core/pull/3908))

### Fixed

- **spark-core-core**: Fix hosted MCP tool approval flow for all session/streaming combinations ([#4054](https://github.com/microsoft/spark-core/pull/4054))
- **spark-core-core**: Prevent repeating instructions in continued Responses API conversations ([#3909](https://github.com/microsoft/spark-core/pull/3909))
- **spark-core-core**: Add missing system instruction attribute to `invoke_agent` span ([#4012](https://github.com/microsoft/spark-core/pull/4012))
- **spark-core-core**: Fix tool normalization and provider sample consolidation ([#3953](https://github.com/microsoft/spark-core/pull/3953))
- **spark-core-azure-ai**: Warn on unsupported AzureAIClient runtime tool/structured_output overrides ([#3919](https://github.com/microsoft/spark-core/pull/3919))
- **spark-core-azure-ai-search**: Improve Azure AI Search package test coverage ([#4019](https://github.com/microsoft/spark-core/pull/4019))
- **spark-core-anthropic**: Fix Anthropic option conflicts and manager parse retries ([#4000](https://github.com/microsoft/spark-core/pull/4000))
- **spark-core-anthropic**: Track and enforce 85%+ unit test coverage for anthropic package ([#3926](https://github.com/microsoft/spark-core/pull/3926))
- **spark-core-azurefunctions**: Achieve 85%+ unit test coverage for azurefunctions package ([#3866](https://github.com/microsoft/spark-core/pull/3866))
- **samples**: Fix workflow, declarative, Redis, Anthropic, GitHub Copilot, Azure AI, MCP, eval, and migration samples ([#4055](https://github.com/microsoft/spark-core/pull/4055), [#4051](https://github.com/microsoft/spark-core/pull/4051), [#4049](https://github.com/microsoft/spark-core/pull/4049), [#4046](https://github.com/microsoft/spark-core/pull/4046), [#4033](https://github.com/microsoft/spark-core/pull/4033), [#4030](https://github.com/microsoft/spark-core/pull/4030), [#4027](https://github.com/microsoft/spark-core/pull/4027), [#4032](https://github.com/microsoft/spark-core/pull/4032), [#4025](https://github.com/microsoft/spark-core/pull/4025), [#4021](https://github.com/microsoft/spark-core/pull/4021), [#4022](https://github.com/microsoft/spark-core/pull/4022), [#4001](https://github.com/microsoft/spark-core/pull/4001))

## [1.0.0b260212] - 2026-02-12

### Added

- **spark-core-core**: Allow `AzureOpenAIResponsesClient` creation with Foundry project endpoint ([#3814](https://github.com/microsoft/spark-core/pull/3814))

### Changed

- **spark-core-core**: [BREAKING] Wire context provider pipeline, remove old types, update all consumers ([#3850](https://github.com/microsoft/spark-core/pull/3850))
- **spark-core-core**: [BREAKING] Checkpoint refactor: encode/decode, checkpoint format, etc ([#3744](https://github.com/microsoft/spark-core/pull/3744))
- **spark-core-core**: [BREAKING] Replace `Hosted*Tool` classes with tool methods ([#3634](https://github.com/microsoft/spark-core/pull/3634))
- **spark-core-core**: Replace Pydantic Settings with `TypedDict` + `load_settings()` ([#3843](https://github.com/microsoft/spark-core/pull/3843))
- **spark-core-core**: Centralize tool result parsing in `FunctionTool.invoke()` ([#3854](https://github.com/microsoft/spark-core/pull/3854))
- **samples**: Restructure Python samples into progressive 01-05 layout ([#3862](https://github.com/microsoft/spark-core/pull/3862))
- **samples**: Adopt `AzureOpenAIResponsesClient`, reorganize orchestration examples, and fix workflow/orchestration bugs ([#3873](https://github.com/microsoft/spark-core/pull/3873))

### Fixed

- **spark-core-core**: Fix non-ascii chars in span attributes ([#3894](https://github.com/microsoft/spark-core/pull/3894))
- **spark-core-core**: Fix streamed workflow agent continuation context by finalizing `AgentExecutor` streams ([#3882](https://github.com/microsoft/spark-core/pull/3882))
- **spark-core-ag-ui**: Fix `Workflow.as_agent()` streaming regression ([#3875](https://github.com/microsoft/spark-core/pull/3875))
- **spark-core-declarative**: Fix declarative package powerfx import crash and `response_format` kwarg error ([#3841](https://github.com/microsoft/spark-core/pull/3841))

## [1.0.0b260210] - 2026-02-10

### Added

- **spark-core-core**: Add long-running agents and background responses support with `ContinuationToken` TypedDict, `background` option in `OpenAIResponsesOptions`, and continuation token propagation through response types ([#3808](https://github.com/microsoft/spark-core/pull/3808))
- **spark-core-core**: Add streaming support for code interpreter deltas ([#3775](https://github.com/microsoft/spark-core/pull/3775))
- **spark-core-core**: Add explicit input, output, and workflow_output parameters to `@handler`, `@executor` and `request_info` ([#3472](https://github.com/microsoft/spark-core/pull/3472))
- **spark-core-core**: Add explicit schema handling to `@tool` decorator ([#3734](https://github.com/microsoft/spark-core/pull/3734))
- **spark-core-core**: New session and context provider types ([#3763](https://github.com/microsoft/spark-core/pull/3763))
- **spark-core-purview**: Add tests to Purview package ([#3513](https://github.com/microsoft/spark-core/pull/3513))

### Changed

- **spark-core-core**: [BREAKING] Renamed core types for simpler API: `ChatAgent` → `Agent`, `RawChatAgent` → `RawAgent`, `ChatMessage` → `Message`, `ChatClientProtocol` → `SupportsChatGetResponse` ([#3747](https://github.com/microsoft/spark-core/pull/3747))
- **spark-core-core**: [BREAKING] Moved to a single `get_response` and `run` API ([#3379](https://github.com/microsoft/spark-core/pull/3379))
- **spark-core-core**: [BREAKING] Merge `send_responses` into `run` method ([#3720](https://github.com/microsoft/spark-core/pull/3720))
- **spark-core-core**: [BREAKING] Renamed `AgentRunContext` to `AgentContext` ([#3714](https://github.com/microsoft/spark-core/pull/3714))
- **spark-core-core**: [BREAKING] Renamed `AgentProtocol` to `SupportsAgentRun` ([#3717](https://github.com/microsoft/spark-core/pull/3717))
- **spark-core-core**: [BREAKING] Renamed next middleware parameter to `call_next` ([#3735](https://github.com/microsoft/spark-core/pull/3735))
- **spark-core-core**: [BREAKING] Standardize TypeVar naming convention (`TName` → `NameT`) ([#3770](https://github.com/microsoft/spark-core/pull/3770))
- **spark-core-core**: [BREAKING] Refactor workflow events to unified discriminated union pattern ([#3690](https://github.com/microsoft/spark-core/pull/3690))
- **spark-core-core**: [BREAKING] Refactor `SharedState` to `State` with sync methods and superstep caching ([#3667](https://github.com/microsoft/spark-core/pull/3667))
- **spark-core-core**: [BREAKING] Move single-config fluent methods to constructor parameters ([#3693](https://github.com/microsoft/spark-core/pull/3693))
- **spark-core-core**: [BREAKING] Types API Review improvements ([#3647](https://github.com/microsoft/spark-core/pull/3647))
- **spark-core-core**: [BREAKING] Fix workflow as agent streaming output ([#3649](https://github.com/microsoft/spark-core/pull/3649))
- **spark-core-orchestrations**: [BREAKING] Move orchestrations to dedicated package ([#3685](https://github.com/microsoft/spark-core/pull/3685))
- **spark-core-core**: [BREAKING] Remove workflow register factory methods; update tests and samples ([#3781](https://github.com/microsoft/spark-core/pull/3781))
- **spark-core-core**: Include sub-workflow structure in graph signature for checkpoint validation ([#3783](https://github.com/microsoft/spark-core/pull/3783))
- **spark-core-core**: Adjust workflows TypeVars from prefix to suffix naming convention ([#3661](https://github.com/microsoft/spark-core/pull/3661))
- **spark-core-purview**: Update CorrelationId ([#3745](https://github.com/microsoft/spark-core/pull/3745))
- **spark-core-anthropic**: Added internal kwargs filtering for Anthropic client ([#3544](https://github.com/microsoft/spark-core/pull/3544))
- **spark-core-github-copilot**: Updated instructions/system_message logic in GitHub Copilot agent ([#3625](https://github.com/microsoft/spark-core/pull/3625))
- **spark-core-mem0**: Disable mem0 telemetry by default ([#3506](https://github.com/microsoft/spark-core/pull/3506))

### Fixed

- **spark-core-core**: Fix workflow not pausing when agent calls declaration-only tool ([#3757](https://github.com/microsoft/spark-core/pull/3757))
- **spark-core-core**: Fix GroupChat orchestrator message cleanup issue ([#3712](https://github.com/microsoft/spark-core/pull/3712))
- **spark-core-core**: Fix HandoffBuilder silently dropping `context_provider` during agent cloning ([#3721](https://github.com/microsoft/spark-core/pull/3721))
- **spark-core-core**: Fix subworkflow duplicate request info events ([#3689](https://github.com/microsoft/spark-core/pull/3689))
- **spark-core-core**: Fix workflow cancellation not propagating to active executors ([#3663](https://github.com/microsoft/spark-core/pull/3663))
- **spark-core-core**: Filter `response_format` from MCP tool call kwargs ([#3494](https://github.com/microsoft/spark-core/pull/3494))
- **spark-core-core**: Fix broken Content API imports in Python samples ([#3639](https://github.com/microsoft/spark-core/pull/3639))
- **spark-core-core**: Potential fix for clear-text logging of sensitive information ([#3573](https://github.com/microsoft/spark-core/pull/3573))
- **spark-core-core**: Skip `model_deployment_name` validation for application endpoints ([#3621](https://github.com/microsoft/spark-core/pull/3621))
- **spark-core-azure-ai**: Fix AzureAIClient dropping agent instructions (Responses API) ([#3636](https://github.com/microsoft/spark-core/pull/3636))
- **spark-core-azure-ai**: Fix AzureAIAgentClient dropping agent instructions in sequential workflows ([#3563](https://github.com/microsoft/spark-core/pull/3563))
- **spark-core-ag-ui**: Fix AG-UI message handling and MCP tool double-call bug ([#3635](https://github.com/microsoft/spark-core/pull/3635))
- **spark-core-claude**: Handle API errors in `run_stream()` method ([#3653](https://github.com/microsoft/spark-core/pull/3653))
- **spark-core-claude**: Preserve `$defs` in JSON schema for nested Pydantic models ([#3655](https://github.com/microsoft/spark-core/pull/3655))

## [1.0.0b260130] - 2026-01-30

### Added

- **spark-core-claude**: Add BaseAgent implementation for Claude Agent SDK ([#3509](https://github.com/microsoft/spark-core/pull/3509))
- **spark-core-core**: Add core types and agents unit tests ([#3470](https://github.com/microsoft/spark-core/pull/3470))
- **spark-core-core**: Add core utilities unit tests ([#3487](https://github.com/microsoft/spark-core/pull/3487))
- **spark-core-core**: Add observability unit tests to improve coverage ([#3469](https://github.com/microsoft/spark-core/pull/3469))
- **spark-core-azure-ai**: Improved AzureAI package test coverage ([#3452](https://github.com/microsoft/spark-core/pull/3452))

### Changed

- **spark-core-core**: Added generic types to `ChatOptions` and `ChatResponse`/`AgentResponse` for Response Format ([#3305](https://github.com/microsoft/spark-core/pull/3305))
- **spark-core-durabletask**: Update durabletask package ([#3492](https://github.com/microsoft/spark-core/pull/3492))

## [1.0.0b260128] - 2026-01-28

### Changed

- **spark-core-core**: [BREAKING] Renamed `@ai_function` decorator to `@tool` and `AIFunction` to `FunctionTool` ([#3413](https://github.com/microsoft/spark-core/pull/3413))
- **spark-core-core**: [BREAKING] Add factory pattern to `GroupChatBuilder` and `MagenticBuilder` ([#3224](https://github.com/microsoft/spark-core/pull/3224))
- **spark-core-github-copilot**: [BREAKING] Renamed `Github` to `GitHub`  ([#3486](https://github.com/microsoft/spark-core/pull/3486))

## [1.0.0b260127] - 2026-01-27

### Added

- **spark-core-github-copilot**: Add BaseAgent implementation for GitHub Copilot SDK ([#3404](https://github.com/microsoft/spark-core/pull/3404))

## [1.0.0b260123] - 2026-01-23

### Added

- **spark-core-azure-ai**: Add support for `rai_config` in agent creation ([#3265](https://github.com/microsoft/spark-core/pull/3265))
- **spark-core-azure-ai**: Support reasoning config for `AzureAIClient` ([#3403](https://github.com/microsoft/spark-core/pull/3403))
- **spark-core-anthropic**: Add `response_format` support for structured outputs ([#3301](https://github.com/microsoft/spark-core/pull/3301))

### Changed

- **spark-core-core**: [BREAKING] Simplify content types to a single class with classmethod constructors ([#3252](https://github.com/microsoft/spark-core/pull/3252))
- **spark-core-core**: [BREAKING] Make `response_format` validation errors visible to users ([#3274](https://github.com/microsoft/spark-core/pull/3274))
- **spark-core-ag-ui**: [BREAKING] Simplify run logic; fix MCP and Anthropic client issues ([#3322](https://github.com/microsoft/spark-core/pull/3322))
- **spark-core-core**: Prefer runtime `kwargs` for `conversation_id` in OpenAI Responses client ([#3312](https://github.com/microsoft/spark-core/pull/3312))

### Fixed

- **spark-core-core**: Verify types during checkpoint deserialization to prevent marker spoofing ([#3243](https://github.com/microsoft/spark-core/pull/3243))
- **spark-core-core**: Filter internal args when passing kwargs to MCP tools ([#3292](https://github.com/microsoft/spark-core/pull/3292))
- **spark-core-core**: Handle anyio cancel scope errors during MCP connection cleanup ([#3277](https://github.com/microsoft/spark-core/pull/3277))
- **spark-core-core**: Filter `conversation_id` when passing kwargs to agent as tool ([#3266](https://github.com/microsoft/spark-core/pull/3266))
- **spark-core-core**: Fix `use_agent_middleware` calling private `_normalize_messages` ([#3264](https://github.com/microsoft/spark-core/pull/3264))
- **spark-core-core**: Add `system_instructions` to ChatClient LLM span tracing ([#3164](https://github.com/microsoft/spark-core/pull/3164))
- **spark-core-core**: Fix Azure chat client asynchronous filtering ([#3260](https://github.com/microsoft/spark-core/pull/3260))
- **spark-core-core**: Fix `HostedImageGenerationTool` mapping to `ImageGenTool` for Azure AI ([#3263](https://github.com/microsoft/spark-core/pull/3263))
- **spark-core-azure-ai**: Fix local MCP tools with `AzureAIProjectAgentProvider` ([#3315](https://github.com/microsoft/spark-core/pull/3315))
- **spark-core-azurefunctions**: Fix MCP tool invocation to use the correct agent ([#3339](https://github.com/microsoft/spark-core/pull/3339))
- **spark-core-declarative**: Fix MCP tool connection not passed from YAML to Azure AI agent creation API ([#3248](https://github.com/microsoft/spark-core/pull/3248))
- **spark-core-ag-ui**: Properly handle JSON serialization with handoff workflows as agent ([#3275](https://github.com/microsoft/spark-core/pull/3275))
- **spark-core-devui**: Ensure proper form rendering for `int` ([#3201](https://github.com/microsoft/spark-core/pull/3201))

## [1.0.0b260116] - 2026-01-16

### Added

- **spark-core-azure-ai**: Create/Get Agent API for Azure V1 ([#3192](https://github.com/microsoft/spark-core/pull/3192))
- **spark-core-core**: Create/Get Agent API for OpenAI Assistants ([#3208](https://github.com/microsoft/spark-core/pull/3208))
- **spark-core-ag-ui**: Support service-managed thread on AG-UI ([#3136](https://github.com/microsoft/spark-core/pull/3136))
- **spark-core-ag-ui**: Add MCP tool support for AG-UI approval flows ([#3212](https://github.com/microsoft/spark-core/pull/3212))
- **samples**: Add AzureAI sample for downloading code interpreter generated files ([#3189](https://github.com/microsoft/spark-core/pull/3189))

### Changed

- **spark-core-core**: [BREAKING] Rename `create_agent` to `as_agent` ([#3249](https://github.com/microsoft/spark-core/pull/3249))
- **spark-core-core**: [BREAKING] Rename `WorkflowOutputEvent.source_executor_id` to `executor_id` for API consistency ([#3166](https://github.com/microsoft/spark-core/pull/3166))

### Fixed

- **spark-core-core**: Properly configure structured outputs based on new options dict ([#3213](https://github.com/microsoft/spark-core/pull/3213))
- **spark-core-core**: Correct `FunctionResultContent` ordering in `WorkflowAgent.merge_updates` ([#3168](https://github.com/microsoft/spark-core/pull/3168))
- **spark-core-azurefunctions**: Update `DurableAIAgent` and fix integration tests ([#3241](https://github.com/microsoft/spark-core/pull/3241))
- **spark-core-azure-ai**: Create/Get Agent API fixes and example improvements ([#3246](https://github.com/microsoft/spark-core/pull/3246))

## [1.0.0b260114] - 2026-01-14

### Added

- **spark-core-azure-ai**: Create/Get Agent API for Azure V2 ([#3059](https://github.com/microsoft/spark-core/pull/3059)) by @moonbox3
- **spark-core-declarative**: Add declarative workflow runtime ([#2815](https://github.com/microsoft/spark-core/pull/2815)) by @moonbox3
- **spark-core-ag-ui**: Add dependencies param to ag-ui FastAPI endpoint ([#3191](https://github.com/microsoft/spark-core/pull/3191)) by @moonbox3
- **spark-core-ag-ui**: Add Pydantic request model and OpenAPI tags support to AG-UI FastAPI endpoint ([#2522](https://github.com/microsoft/spark-core/pull/2522)) by @claude89757
- **spark-core-core**: Add tool call/result content types and update connectors and samples ([#2971](https://github.com/microsoft/spark-core/pull/2971)) by @moonbox3
- **spark-core-core**: Add more specific exceptions to Workflow ([#3188](https://github.com/microsoft/spark-core/pull/3188)) by @TaoChenOSU

### Changed

- **spark-core-core**: [BREAKING] Refactor orchestrations ([#3023](https://github.com/microsoft/spark-core/pull/3023)) by @TaoChenOSU
- **spark-core-core**: [BREAKING] Introducing Options as TypedDict and Generic ([#3140](https://github.com/microsoft/spark-core/pull/3140)) by @eavanvalkenburg
- **spark-core-core**: [BREAKING] Removed display_name, renamed context_providers, middleware and AggregateContextProvider ([#3139](https://github.com/microsoft/spark-core/pull/3139)) by @eavanvalkenburg
- **spark-core-core**: MCP Improvements: improved connection loss behavior, pagination for loading and a param to control representation ([#3154](https://github.com/microsoft/spark-core/pull/3154)) by @eavanvalkenburg
- **spark-core-azure-ai**: Azure AI direct A2A endpoint support ([#3127](https://github.com/microsoft/spark-core/pull/3127)) by @moonbox3

### Fixed

- **spark-core-anthropic**: Fix duplicate ToolCallStartEvent in streaming tool calls ([#3051](https://github.com/microsoft/spark-core/pull/3051)) by @moonbox3
- **spark-core-anthropic**: Fix Anthropic streaming response bugs ([#3141](https://github.com/microsoft/spark-core/pull/3141)) by @eavanvalkenburg
- **spark-core-ag-ui**: Execute tools with approval_mode, fix shared state, code cleanup ([#3079](https://github.com/microsoft/spark-core/pull/3079)) by @moonbox3
- **spark-core-azure-ai**: Fix AzureAIClient tool call bug for AG-UI use ([#3148](https://github.com/microsoft/spark-core/pull/3148)) by @moonbox3
- **spark-core-core**: Fix MCPStreamableHTTPTool to use new streamable_http_client API ([#3088](https://github.com/microsoft/spark-core/pull/3088)) by @Copilot
- **spark-core-core**: Multiple bug fixes ([#3150](https://github.com/microsoft/spark-core/pull/3150)) by @eavanvalkenburg

## [1.0.0b260107] - 2026-01-07

### Added

- **spark-core-devui**: Improve DevUI and add Context Inspector view as a new tab under traces ([#2742](https://github.com/microsoft/spark-core/pull/2742)) by @victordibia
- **samples**: Add streaming sample for Azure Functions ([#3057](https://github.com/microsoft/spark-core/pull/3057)) by @gavin-aguiar

### Changed

- **repo**: Update templates ([#3106](https://github.com/microsoft/spark-core/pull/3106)) by @eavanvalkenburg

### Fixed

- **spark-core-ag-ui**: Fix MCP tool result serialization for list[TextContent] ([#2523](https://github.com/microsoft/spark-core/pull/2523)) by @claude89757
- **spark-core-azure-ai**: Fix response_format handling for structured outputs ([#3114](https://github.com/microsoft/spark-core/pull/3114)) by @moonbox3

## [1.0.0b260106] - 2026-01-06

### Added

- **repo**: Add issue template and additional labeling ([#3006](https://github.com/microsoft/spark-core/pull/3006)) by @eavanvalkenburg

### Changed

- None

### Fixed

- **spark-core-core**: Fix max tokens translation and add extra integer test ([#3037](https://github.com/microsoft/spark-core/pull/3037)) by @eavanvalkenburg
- **spark-core-azure-ai**: Fix failure when conversation history contains assistant messages ([#3076](https://github.com/microsoft/spark-core/pull/3076)) by @moonbox3
- **spark-core-core**: Use HTTP exporter for http/protobuf protocol ([#3070](https://github.com/microsoft/spark-core/pull/3070)) by @takanori-terai
- **spark-core-core**: Fix ExecutorInvokedEvent and ExecutorCompletedEvent observability data ([#3090](https://github.com/microsoft/spark-core/pull/3090)) by @moonbox3
- **spark-core-core**: Honor tool_choice parameter passed to agent.run() and chat client methods ([#3095](https://github.com/microsoft/spark-core/pull/3095)) by @moonbox3
- **samples**: AzureAI SharePoint sample fix ([#3108](https://github.com/microsoft/spark-core/pull/3108)) by @giles17

## [1.0.0b251223] - 2025-12-23

### Added

- **spark-core-bedrock**: Introducing support for Bedrock-hosted models (Anthropic, Cohere, etc.) ([#2610](https://github.com/microsoft/spark-core/pull/2610))
- **spark-core-core**: Added `response.created` and `response.in_progress` event process to `OpenAIBaseResponseClient` ([#2975](https://github.com/microsoft/spark-core/pull/2975))
- **spark-core-foundry-local**: Introducing Foundry Local Chat Clients ([#2915](https://github.com/microsoft/spark-core/pull/2915))
- **samples**: Added GitHub MCP sample with PAT ([#2967](https://github.com/microsoft/spark-core/pull/2967))

### Changed

- **spark-core-core**: Preserve reasoning blocks with OpenRouter ([#2950](https://github.com/microsoft/spark-core/pull/2950))

## [1.0.0b251218] - 2025-12-18

### Added

- **spark-core-core**: Azure AI Agent with Bing Grounding Citations sample ([#2892](https://github.com/microsoft/spark-core/pull/2892))
- **spark-core-core**: Workflow option to visualize internal executors ([#2917](https://github.com/microsoft/spark-core/pull/2917))
- **spark-core-core**: Workflow cancellation sample ([#2732](https://github.com/microsoft/spark-core/pull/2732))
- **spark-core-core**: Azure Managed Redis support with credential provider ([#2887](https://github.com/microsoft/spark-core/pull/2887))
- **spark-core-core**: Additional arguments for Azure AI agent configuration ([#2922](https://github.com/microsoft/spark-core/pull/2922))

### Changed

- **spark-core-ollama**: Updated Ollama package version ([#2920](https://github.com/microsoft/spark-core/pull/2920))
- **spark-core-ollama**: Move Ollama samples to samples getting started directory ([#2921](https://github.com/microsoft/spark-core/pull/2921))
- **spark-core-core**: Cleanup and refactoring of chat clients ([#2937](https://github.com/microsoft/spark-core/pull/2937))
- **spark-core-core**: Align Run ID and Thread ID casing with AG-UI TypeScript SDK ([#2948](https://github.com/microsoft/spark-core/pull/2948))

### Fixed

- **spark-core-core**: Fix Pydantic error when using Literal types for tool parameters ([#2893](https://github.com/microsoft/spark-core/pull/2893))
- **spark-core-core**: Correct MCP image type conversion in `_mcp.py` ([#2901](https://github.com/microsoft/spark-core/pull/2901))
- **spark-core-core**: Fix BadRequestError when using Pydantic models in response formatting ([#1843](https://github.com/microsoft/spark-core/pull/1843))
- **spark-core-core**: Propagate workflow kwargs to sub-workflows via WorkflowExecutor ([#2923](https://github.com/microsoft/spark-core/pull/2923))
- **spark-core-core**: Fix WorkflowAgent event handling and kwargs forwarding ([#2946](https://github.com/microsoft/spark-core/pull/2946))

## [1.0.0b251216] - 2025-12-16

### Added

- **spark-core-ollama**: Ollama connector for Spark Core (#1104)
- **spark-core-core**: Added custom args and thread object to `ai_function` kwargs (#2769)
- **spark-core-core**: Enable checkpointing for `WorkflowAgent` (#2774)

### Changed

- **spark-core-core**: [BREAKING] Observability updates (#2782)
- **spark-core-core**: Use agent description in `HandoffBuilder` auto-generated tools (#2714)
- **spark-core-core**: Remove warnings from workflow builder when not using factories (#2808)

### Fixed

- **spark-core-core**: Fix `WorkflowAgent` to include thread conversation history (#2774)
- **spark-core-core**: Fix context duplication in handoff workflows when restoring from checkpoint (#2867)
- **spark-core-core**: Fix middleware terminate flag to exit function calling loop immediately (#2868)
- **spark-core-core**: Fix `WorkflowAgent` to emit `yield_output` as agent response (#2866)
- **spark-core-core**: Filter framework kwargs from MCP tool invocations (#2870)

## [1.0.0b251211] - 2025-12-11

### Added

- **spark-core-core**: Extend HITL support for all orchestration patterns (#2620)
- **spark-core-core**: Add factory pattern to concurrent orchestration builder (#2738)
- **spark-core-core**: Add factory pattern to sequential orchestration builder (#2710)
- **spark-core-azure-ai**: Capture file IDs from code interpreter in streaming responses (#2741)

### Changed

- **spark-core-azurefunctions**: Change DurableAIAgent log level from warning to debug when invoked without thread (#2736)

### Fixed

- **spark-core-core**: Added more complete parsing for mcp tool arguments (#2756)
- **spark-core-core**: Fix GroupChat ManagerSelectionResponse JSON Schema for OpenAI Structured Outputs (#2750)
- **samples**: Standardize OpenAI API key environment variable naming (#2629)

## [1.0.0b251209] - 2025-12-09

### Added

- **spark-core-core**: Support an autonomous handoff flow (#2497)
- **spark-core-core**: WorkflowBuilder registry (#2486)
- **spark-core-a2a**: Add configurable timeout support to A2AAgent (#2432)
- **samples**: Added Azure OpenAI Responses File Search sample + Integration test update (#2645)
- **samples**: Update fan in fan out sample to show concurrency (#2705)

### Changed

- **spark-core-azure-ai**: [BREAKING] Renamed `async_credential` to `credential` (#2648)
- **samples**: Improve sample logging (#2692)
- **samples**: azureai image gen sample update (#2709)

### Fixed

- **spark-core-core**: Fix DurableState schema serializations (#2670)
- **spark-core-core**: Fix context provider lifecycle agentic mode (#2650)
- **spark-core-devui**: Fix WorkflowFailedEvent error extraction (#2706)
- **spark-core-devui**: Fix DevUI fails when uploading Pdf file (#2675)
- **spark-core-devui**: Fix message serialization issue (#2674)
- **observability**: Display system prompt in langfuse (#2653)

## [1.0.0b251204] - 2025-12-04

### Added

- **spark-core-core**: Add support for Pydantic `BaseModel` as function call result (#2606)
- **spark-core-core**: Executor events now include I/O data (#2591)
- **samples**: Inline YAML declarative sample (#2582)
- **samples**: Handoff-as-agent with HITL sample (#2534)

### Changed

- **spark-core-core**: [BREAKING] Support Magentic agent tool call approvals and plan stalling HITL behavior (#2569)
- **spark-core-core**: [BREAKING] Standardize orchestration outputs as list of `Message`; allow agent as group chat manager (#2291)
- **spark-core-core**: [BREAKING] Respond with `AgentRunResponse` including serialized structured output (#2285)
- **observability**: Use `executor_id` and `edge_group_id` as span names for clearer traces (#2538)
- **spark-core-devui**: Add multimodal input support for workflows and refactor chat input (#2593)
- **docs**: Update Python orchestration documentation (#2087)

### Fixed

- **observability**: Resolve mypy error in observability module (#2641)
- **spark-core-core**: Fix `AgentRunResponse.created_at` returning local datetime labeled as UTC (#2590)
- **spark-core-core**: Emit `ExecutorFailedEvent` before `WorkflowFailedEvent` when executor throws (#2537)
- **spark-core-core**: Fix MagenticAgentExecutor producing `repr` string for tool call content (#2566)
- **spark-core-core**: Fixed empty text content Pydantic validation failure (#2539)
- **spark-core-azure-ai**: Added support for application endpoints in Azure AI client (#2460)
- **spark-core-azurefunctions**: Add MCP tool support (#2385)
- **spark-core-core**: Preserve MCP array items schema in Pydantic field generation (#2382)
- **spark-core-devui**: Make tool call view optional and fix links (#2243)
- **spark-core-core**: Always include output in function call result messages (#2414)
- **spark-core-redis**: Fix TypeError (#2411)

## [1.0.0b251120] - 2025-11-20

### Added

- **spark-core-core**: Introducing support for declarative YAML spec ([#2002](https://github.com/microsoft/spark-core/pull/2002))
- **spark-core-core**: Use AI Foundry evaluators for self-reflection ([#2250](https://github.com/microsoft/spark-core/pull/2250))
- **spark-core-core**: Propagate `as_tool()` kwargs and add runtime context + middleware sample ([#2311](https://github.com/microsoft/spark-core/pull/2311))
- **spark-core-anthropic**: Anthropic Foundry integration ([#2302](https://github.com/microsoft/spark-core/pull/2302))
- **samples**: M365 Agent SDK Hosting sample ([#2292](https://github.com/microsoft/spark-core/pull/2292))
- **samples**: Foundry Sample for A2A + SharePoint Samples ([#2313](https://github.com/microsoft/spark-core/pull/2313))

### Changed

- **spark-core-azurefunctions**: [BREAKING] Schema changes for Azure Functions package ([#2151](https://github.com/microsoft/spark-core/pull/2151))
- **spark-core-core**: Move evaluation folders under `evaluations` ([#2355](https://github.com/microsoft/spark-core/pull/2355))
- **spark-core-core**: Move red teaming files to their own folder ([#2333](https://github.com/microsoft/spark-core/pull/2333))
- **spark-core-core**: "fix all" task now single source of truth ([#2303](https://github.com/microsoft/spark-core/pull/2303))
- **spark-core-core**: Improve and clean up exception handling ([#2337](https://github.com/microsoft/spark-core/pull/2337), [#2319](https://github.com/microsoft/spark-core/pull/2319))
- **spark-core-core**: Clean up imports ([#2318](https://github.com/microsoft/spark-core/pull/2318))

### Fixed

- **spark-core-azure-ai**: Fix for Azure AI client ([#2358](https://github.com/microsoft/spark-core/pull/2358))
- **spark-core-core**: Fix tool execution bleed-over in aiohttp/Bot Framework scenarios ([#2314](https://github.com/microsoft/spark-core/pull/2314))
- **spark-core-core**: `@ai_function` now correctly handles `self` parameter ([#2266](https://github.com/microsoft/spark-core/pull/2266))
- **spark-core-core**: Resolve string annotations in `FunctionExecutor` ([#2308](https://github.com/microsoft/spark-core/pull/2308))
- **spark-core-core**: Langfuse observability captures Agent system instructions ([#2316](https://github.com/microsoft/spark-core/pull/2316))
- **spark-core-core**: Incomplete URL substring sanitization fix ([#2274](https://github.com/microsoft/spark-core/pull/2274))
- **observability**: Handle datetime serialization in tool results ([#2248](https://github.com/microsoft/spark-core/pull/2248))

## [1.0.0b251117] - 2025-11-17

### Fixed

- **spark-core-ag-ui**: Fix ag-ui state handling issues ([#2289](https://github.com/microsoft/spark-core/pull/2289))

## [1.0.0b251114] - 2025-11-14

### Added

- **samples**: Bing Custom Search sample using `HostedWebSearchTool` ([#2226](https://github.com/microsoft/spark-core/pull/2226))
- **samples**: Fabric and Browser Automation samples ([#2207](https://github.com/microsoft/spark-core/pull/2207))
- **samples**: Hosted agent samples ([#2205](https://github.com/microsoft/spark-core/pull/2205))
- **samples**: Azure OpenAI Responses API Hosted MCP sample ([#2108](https://github.com/microsoft/spark-core/pull/2108))
- **samples**: Bing Grounding and Custom Search samples ([#2200](https://github.com/microsoft/spark-core/pull/2200))

### Changed

- **spark-core-azure-ai**: Enhance Azure AI Search citations with complete URL information ([#2066](https://github.com/microsoft/spark-core/pull/2066))
- **spark-core-azurefunctions**: Update samples to latest stable Azure Functions Worker packages ([#2189](https://github.com/microsoft/spark-core/pull/2189))
- **spark-core-azure-ai**: Agent name now required for `AzureAIClient` ([#2198](https://github.com/microsoft/spark-core/pull/2198))
- **build**: Use `uv build` for packaging ([#2161](https://github.com/microsoft/spark-core/pull/2161))
- **tooling**: Pre-commit improvements ([#2222](https://github.com/microsoft/spark-core/pull/2222))
- **dependencies**: Updated package versions ([#2208](https://github.com/microsoft/spark-core/pull/2208))

### Fixed

- **spark-core-core**: Prevent duplicate MCP tools and prompts ([#1876](https://github.com/microsoft/spark-core/pull/1876)) ([#1890](https://github.com/microsoft/spark-core/pull/1890))
- **spark-core-devui**: Fix HIL regression ([#2167](https://github.com/microsoft/spark-core/pull/2167))
- **spark-core-chatkit**: ChatKit sample fixes ([#2174](https://github.com/microsoft/spark-core/pull/2174))

## [1.0.0b251112.post1] - 2025-11-12

### Added

- **spark-core-azurefunctions**: Merge Azure Functions feature branch (#1916)

### Fixed

- **spark-core-ag-ui**: fix tool call id mismatch in ag-ui ([#2166](https://github.com/microsoft/spark-core/pull/2166))

## [1.0.0b251112] - 2025-11-12

### Added

- **spark-core-azure-ai**: Azure AI client based on new `azure-ai-projects` package ([#1910](https://github.com/microsoft/spark-core/pull/1910))
- **spark-core-anthropic**: Add convenience method on data content ([#2083](https://github.com/microsoft/spark-core/pull/2083))

### Changed

- **spark-core-core**: Update OpenAI samples to use agents ([#2012](https://github.com/microsoft/spark-core/pull/2012))

### Fixed

- **spark-core-anthropic**: Fixed image handling in Anthropic client ([#2083](https://github.com/microsoft/spark-core/pull/2083))

## [1.0.0b251111] - 2025-11-11

### Added

- **spark-core-core**: Add OpenAI Responses Image Generation Stream Support with partial images and unit tests ([#1853](https://github.com/microsoft/spark-core/pull/1853))
- **spark-core-ag-ui**: Add concrete AGUIChatClient implementation ([#2072](https://github.com/microsoft/spark-core/pull/2072))

### Fixed

- **spark-core-a2a**: Use the last entry in the task history to avoid empty responses ([#2101](https://github.com/microsoft/spark-core/pull/2101))
- **spark-core-core**: Fix MCP Tool Parameter Descriptions not propagated to LLMs ([#1978](https://github.com/microsoft/spark-core/pull/1978))
- **spark-core-core**: Handle agent user input request in AgentExecutor ([#2022](https://github.com/microsoft/spark-core/pull/2022))
- **spark-core-core**: Fix Model ID attribute not showing up in `invoke_agent` span ([#2061](https://github.com/microsoft/spark-core/pull/2061))
- **spark-core-core**: Fix underlying tool choice bug and enable return to previous Handoff subagent ([#2037](https://github.com/microsoft/spark-core/pull/2037))

## [1.0.0b251108] - 2025-11-08

### Added

- **spark-core-devui**: Add OpenAI Responses API proxy support + HIL (Human-in-the-Loop) for Workflows ([#1737](https://github.com/microsoft/spark-core/pull/1737))
- **spark-core-purview**: Add Caching and background processing in Python Purview Middleware ([#1844](https://github.com/microsoft/spark-core/pull/1844))

### Changed

- **spark-core-devui**: Use metadata.entity_id instead of model field ([#1984](https://github.com/microsoft/spark-core/pull/1984))
- **spark-core-devui**: Serialize workflow input as string to maintain conformance with OpenAI Responses format ([#2021](https://github.com/microsoft/spark-core/pull/2021))

## [1.0.0b251106.post1] - 2025-11-06

### Fixed

- **spark-core-ag-ui**: Fix ag-ui examples packaging for PyPI publish ([#1953](https://github.com/microsoft/spark-core/pull/1953))

## [1.0.0b251106] - 2025-11-06

### Changed

- **spark-core-ag-ui**: export sample ag-ui agents ([#1927](https://github.com/microsoft/spark-core/pull/1927))

## [1.0.0b251105] - 2025-11-05

### Added

- **spark-core-ag-ui**: Initial release of AG-UI protocol integration for Spark Core ([#1826](https://github.com/microsoft/spark-core/pull/1826))
- **spark-core-chatkit**: ChatKit integration with a sample application ([#1273](https://github.com/microsoft/spark-core/pull/1273))
- Added parameter to disable agent cleanup in AzureAIAgentClient ([#1882](https://github.com/microsoft/spark-core/pull/1882))
- Add support for Python 3.14 ([#1904](https://github.com/microsoft/spark-core/pull/1904))

### Changed

- [BREAKING] Replaced AIProjectClient with AgentsClient in Foundry ([#1936](https://github.com/microsoft/spark-core/pull/1936))
- Updates to Tools ([#1835](https://github.com/microsoft/spark-core/pull/1835))

### Fixed

- Fix missing packaging dependency ([#1929](https://github.com/microsoft/spark-core/pull/1929))

## [1.0.0b251104] - 2025-11-04

### Added

- Introducing the Anthropic Client ([#1819](https://github.com/microsoft/spark-core/pull/1819))

### Changed

- [BREAKING] Consolidate workflow run APIs ([#1723](https://github.com/microsoft/spark-core/pull/1723))
- [BREAKING] Remove request_type param from ctx.request_info() ([#1824](https://github.com/microsoft/spark-core/pull/1824))
- [BREAKING] Cleanup of dependencies ([#1803](https://github.com/microsoft/spark-core/pull/1803))
- [BREAKING] Replace `RequestInfoExecutor` with `request_info` API and `@response_handler` ([#1466](https://github.com/microsoft/spark-core/pull/1466))
- Azure AI Search Support Update + Refactored Samples & Unit Tests ([#1683](https://github.com/microsoft/spark-core/pull/1683))
- Lab: Updates to GAIA module ([#1763](https://github.com/microsoft/spark-core/pull/1763))

### Fixed

- Azure AI `top_p` and `temperature` parameters fix ([#1839](https://github.com/microsoft/spark-core/pull/1839))
- Ensure agent thread is part of checkpoint ([#1756](https://github.com/microsoft/spark-core/pull/1756))
- Fix middleware and cleanup confusing function ([#1865](https://github.com/microsoft/spark-core/pull/1865))
- Fix type compatibility check ([#1753](https://github.com/microsoft/spark-core/pull/1753))
- Fix mcp tool cloning for handoff pattern ([#1883](https://github.com/microsoft/spark-core/pull/1883))

## [1.0.0b251028] - 2025-10-28

### Added

- Added thread to AgentRunContext ([#1732](https://github.com/microsoft/spark-core/pull/1732))
- AutoGen migration samples ([#1738](https://github.com/microsoft/spark-core/pull/1738))
- Add Handoff orchestration pattern support ([#1469](https://github.com/microsoft/spark-core/pull/1469))
- Added Samples for HostedCodeInterpreterTool with files ([#1583](https://github.com/microsoft/spark-core/pull/1583))

### Changed

- [BREAKING] Introduce group chat and refactor orchestrations. Fix as_agent(). Standardize orchestration start msg types. ([#1538](https://github.com/microsoft/spark-core/pull/1538))
- [BREAKING] Update Spark Core Lab Lightning to use Agent-lightning v0.2.0 API ([#1644](https://github.com/microsoft/spark-core/pull/1644))
- [BREAKING] Refactor Checkpointing for runner and runner context ([#1645](https://github.com/microsoft/spark-core/pull/1645))
- Update lab packages and installation instructions ([#1687](https://github.com/microsoft/spark-core/pull/1687))
- Remove deprecated add_agent() calls from workflow samples ([#1508](https://github.com/microsoft/spark-core/pull/1508))

### Fixed

- Reject @executor on staticmethod/classmethod with clear error message ([#1719](https://github.com/microsoft/spark-core/pull/1719))
- DevUI Fix Serialization, Timestamp and Other Issues ([#1584](https://github.com/microsoft/spark-core/pull/1584))
- MCP Error Handling Fix + Added Unit Tests ([#1621](https://github.com/microsoft/spark-core/pull/1621))
- InMemoryCheckpointManager is not JSON serializable ([#1639](https://github.com/microsoft/spark-core/pull/1639))
- Fix gen_ai.operation.name to be invoke_agent ([#1729](https://github.com/microsoft/spark-core/pull/1729))

## [1.0.0b251016] - 2025-10-16

### Added

- Add Purview Middleware ([#1142](https://github.com/microsoft/spark-core/pull/1142))
- Added URL Citation Support to Azure AI Agent ([#1397](https://github.com/microsoft/spark-core/pull/1397))
- Added MCP headers for AzureAI ([#1506](https://github.com/microsoft/spark-core/pull/1506))
- Add Function Approval UI to DevUI ([#1401](https://github.com/microsoft/spark-core/pull/1401))
- Added function approval example with streaming ([#1365](https://github.com/microsoft/spark-core/pull/1365))
- Added A2A AuthInterceptor Support ([#1317](https://github.com/microsoft/spark-core/pull/1317))
- Added example with MCP and authentication ([#1389](https://github.com/microsoft/spark-core/pull/1389))
- Added sample with Foundry Redteams ([#1306](https://github.com/microsoft/spark-core/pull/1306))
- Added AzureAI Agent AI Search Sample ([#1281](https://github.com/microsoft/spark-core/pull/1281))
- Added AzureAI Bing Connection Name Support ([#1364](https://github.com/microsoft/spark-core/pull/1364))

### Changed

- Enhanced documentation for dependency injection and serialization features ([#1324](https://github.com/microsoft/spark-core/pull/1324))
- Update README to list all available examples ([#1394](https://github.com/microsoft/spark-core/pull/1394))
- Reorganize workflows modules ([#1282](https://github.com/microsoft/spark-core/pull/1282))
- Improved thread serialization and deserialization with better tests ([#1316](https://github.com/microsoft/spark-core/pull/1316))
- Included existing agent definition in requests to Azure AI ([#1285](https://github.com/microsoft/spark-core/pull/1285))
- DevUI - Internal Refactor, Conversations API support, and performance improvements ([#1235](https://github.com/microsoft/spark-core/pull/1235))
- Refactor `RequestInfoExecutor` ([#1403](https://github.com/microsoft/spark-core/pull/1403))

### Fixed

- Fix AI Search Tool Sample and improve AI Search Exceptions ([#1206](https://github.com/microsoft/spark-core/pull/1206))
- Fix Failure with Function Approval Messages in Chat Clients ([#1322](https://github.com/microsoft/spark-core/pull/1322))
- Fix deadlock in Magentic workflow ([#1325](https://github.com/microsoft/spark-core/pull/1325))
- Fix tool call content not showing up in workflow events ([#1290](https://github.com/microsoft/spark-core/pull/1290))
- Fixed instructions duplication in model clients ([#1332](https://github.com/microsoft/spark-core/pull/1332))
- Agent Name Sanitization ([#1523](https://github.com/microsoft/spark-core/pull/1523))

## [1.0.0b251007] - 2025-10-07

### Added

- Added method to expose agent as MCP server ([#1248](https://github.com/microsoft/spark-core/pull/1248))
- Add PDF file support to OpenAI content parser with filename mapping ([#1121](https://github.com/microsoft/spark-core/pull/1121))
- Sample on integration of Azure OpenAI Responses Client with a local MCP server ([#1215](https://github.com/microsoft/spark-core/pull/1215))
- Added approval_mode and allowed_tools to local MCP ([#1203](https://github.com/microsoft/spark-core/pull/1203))
- Introducing AI Function approval ([#1131](https://github.com/microsoft/spark-core/pull/1131))
- Add name and description to workflows ([#1183](https://github.com/microsoft/spark-core/pull/1183))
- Add Ollama example using OpenAIChatClient ([#1100](https://github.com/microsoft/spark-core/pull/1100))
- Add DevUI improvements with color scheme, linking, agent details, and token usage data ([#1091](https://github.com/microsoft/spark-core/pull/1091))
- Add semantic-kernel to spark-core migration code samples ([#1045](https://github.com/microsoft/spark-core/pull/1045))

### Changed

- [BREAKING] Parameter naming and other fixes ([#1255](https://github.com/microsoft/spark-core/pull/1255))
- [BREAKING] Introduce add_agent functionality and added output_response to AgentExecutor; agent streaming behavior to follow workflow invocation ([#1184](https://github.com/microsoft/spark-core/pull/1184))
- OpenAI Clients accepting api_key callback ([#1139](https://github.com/microsoft/spark-core/pull/1139))
- Updated docstrings ([#1225](https://github.com/microsoft/spark-core/pull/1225))
- Standardize docstrings: Use Keyword Args for Settings classes and add environment variable examples ([#1202](https://github.com/microsoft/spark-core/pull/1202))
- Update References to Agent2Agent protocol to use correct terminology ([#1162](https://github.com/microsoft/spark-core/pull/1162))
- Update getting started samples to reflect AF and update unit test ([#1093](https://github.com/microsoft/spark-core/pull/1093))
- Update Lab Installation instructions to install from source ([#1051](https://github.com/microsoft/spark-core/pull/1051))
- Update python DEV_SETUP to add brew-based uv installation ([#1173](https://github.com/microsoft/spark-core/pull/1173))
- Update docstrings of all files and add example code in public interfaces ([#1107](https://github.com/microsoft/spark-core/pull/1107))
- Clarifications on installing packages in README ([#1036](https://github.com/microsoft/spark-core/pull/1036))
- DevUI Fixes ([#1035](https://github.com/microsoft/spark-core/pull/1035))
- Packaging fixes: removed lab from dependencies, setup build/publish tasks, set homepage url ([#1056](https://github.com/microsoft/spark-core/pull/1056))
- Agents + Chat Client Samples Docstring Updates ([#1028](https://github.com/microsoft/spark-core/pull/1028))
- Python: Foundry Agent Completeness ([#954](https://github.com/microsoft/spark-core/pull/954))

### Fixed

- Ollama + azureai openapi samples fix ([#1244](https://github.com/microsoft/spark-core/pull/1244))
- Fix multimodal input sample: Document required environment variables and configuration options ([#1088](https://github.com/microsoft/spark-core/pull/1088))
- Fix Azure AI Getting Started samples: Improve documentation and code readability ([#1089](https://github.com/microsoft/spark-core/pull/1089))
- Fix a2a import ([#1058](https://github.com/microsoft/spark-core/pull/1058))
- Fix DevUI serialization and agent structured outputs ([#1055](https://github.com/microsoft/spark-core/pull/1055))
- Default DevUI workflows to string input when start node is auto-wrapped agent ([#1143](https://github.com/microsoft/spark-core/pull/1143))
- Add missing pre flags on pip packages ([#1130](https://github.com/microsoft/spark-core/pull/1130))


## [1.0.0b251001] - 2025-10-01

### Added

- First release of Spark Core for Python
- spark-core-core: Main abstractions, types and implementations for OpenAI and Azure OpenAI
- spark-core-azure-ai: Integration with Microsoft Foundry Agents
- spark-core-copilotstudio: Integration with Microsoft Copilot Studio agents
- spark-core-a2a: Create A2A agents
- spark-core-devui: Browser-based UI to chat with agents and workflows, with tracing visualization
- spark-core-mem0 and spark-core-redis: Integrations for Mem0 Context Provider and Redis Context Provider/Chat Memory Store
- spark-core: Meta-package for installing all packages

For more information, see the [announcement blog post](https://devblogs.microsoft.com/foundry/introducing-microsoft-spark-core-the-open-source-engine-for-agentic-ai-apps/).

[Unreleased]: https://github.com/microsoft/spark-core/compare/python-1.12.1...HEAD
[1.12.1]: https://github.com/microsoft/spark-core/compare/python-1.12.0...python-1.12.1
[1.12.0]: https://github.com/microsoft/spark-core/compare/python-1.11.0...python-1.12.0
[1.11.0]: https://github.com/microsoft/spark-core/compare/python-1.10.0...python-1.11.0
[1.10.0]: https://github.com/microsoft/spark-core/compare/python-1.9.0...python-1.10.0
[1.9.0]: https://github.com/microsoft/spark-core/compare/python-1.8.1...python-1.9.0
[1.8.1]: https://github.com/microsoft/spark-core/compare/python-1.8.0...python-1.8.1
[1.8.0]: https://github.com/microsoft/spark-core/compare/python-1.7.0...python-1.8.0
[1.7.0]: https://github.com/microsoft/spark-core/compare/python-1.6.0...python-1.7.0
[1.6.0]: https://github.com/microsoft/spark-core/compare/python-1.5.0...python-1.6.0
[1.5.0]: https://github.com/microsoft/spark-core/compare/python-1.4.0...python-1.5.0
[1.4.0]: https://github.com/microsoft/spark-core/compare/python-1.3.0...python-1.4.0
[1.3.0]: https://github.com/microsoft/spark-core/compare/python-1.2.2...python-1.3.0
[1.2.2]: https://github.com/microsoft/spark-core/compare/python-1.2.1...python-1.2.2
[1.2.1]: https://github.com/microsoft/spark-core/compare/python-1.2.0...python-1.2.1
[1.2.0]: https://github.com/microsoft/spark-core/compare/python-1.1.1...python-1.2.0
[1.1.1]: https://github.com/microsoft/spark-core/compare/python-1.1.0...python-1.1.1
[1.1.0]: https://github.com/microsoft/spark-core/compare/python-1.0.1...python-1.1.0
[1.0.1]: https://github.com/microsoft/spark-core/compare/python-1.0.0...python-1.0.1
[1.0.0]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc6...python-1.0.0
[1.0.0rc6]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc5...python-1.0.0rc6
[1.0.0rc5]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc4...python-1.0.0rc5
[1.0.0rc4]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc3...python-1.0.0rc4
[1.0.0rc3]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc2...python-1.0.0rc3
[1.0.0rc2]: https://github.com/microsoft/spark-core/compare/python-1.0.0rc1...python-1.0.0rc2
[1.0.0rc1]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260212...python-1.0.0rc1
[1.0.0b260212]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260210...python-1.0.0b260212
[1.0.0b260210]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260130...python-1.0.0b260210
[1.0.0b260130]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260128...python-1.0.0b260130
[1.0.0b260128]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260127...python-1.0.0b260128
[1.0.0b260127]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260123...python-1.0.0b260127
[1.0.0b260123]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260116...python-1.0.0b260123
[1.0.0b260116]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260114...python-1.0.0b260116
[1.0.0b260114]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260107...python-1.0.0b260114
[1.0.0b260107]: https://github.com/microsoft/spark-core/compare/python-1.0.0b260106...python-1.0.0b260107
[1.0.0b260106]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251223...python-1.0.0b260106
[1.0.0b251223]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251218...python-1.0.0b251223
[1.0.0b251218]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251216...python-1.0.0b251218
[1.0.0b251216]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251211...python-1.0.0b251216
[1.0.0b251211]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251209...python-1.0.0b251211
[1.0.0b251209]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251204...python-1.0.0b251209
[1.0.0b251204]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251120...python-1.0.0b251204
[1.0.0b251120]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251117...python-1.0.0b251120
[1.0.0b251117]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251114...python-1.0.0b251117
[1.0.0b251114]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251112.post1...python-1.0.0b251114
[1.0.0b251112.post1]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251112...python-1.0.0b251112.post1
[1.0.0b251112]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251111...python-1.0.0b251112
[1.0.0b251111]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251108...python-1.0.0b251111
[1.0.0b251108]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251106.post1...python-1.0.0b251108
[1.0.0b251106.post1]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251106...python-1.0.0b251106.post1
[1.0.0b251106]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251105...python-1.0.0b251106
[1.0.0b251105]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251104...python-1.0.0b251105
[1.0.0b251104]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251028...python-1.0.0b251104
[1.0.0b251028]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251016...python-1.0.0b251028
[1.0.0b251016]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251007...python-1.0.0b251016
[1.0.0b251007]: https://github.com/microsoft/spark-core/compare/python-1.0.0b251001...python-1.0.0b251007
[1.0.0b251001]: https://github.com/microsoft/spark-core/releases/tag/python-1.0.0b251001
