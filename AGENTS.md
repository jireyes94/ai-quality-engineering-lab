# AGENTS.md

## Project purpose
AI Quality Engineering Lab studies and measures the reliability of AI agents that use tools. AutomationExercise is the initial experimental web environment, not the product.

## Current development stage
The project is an early browser-automation prototype. Build and test a minimal, controlled execution loop before integrating an LLM. Use scripted decisions to validate behavior first.

## Technology stack
- Python >=3.14, Pydantic, Playwright, and Pytest.
- uv manages dependencies, environments, and execution.
- Application code lives in `src/ai_quality_engineering_lab/`.
- `pyproject.toml` defines project dependencies and entry points.

## Architectural principles
- Follow `observe -> decide -> act -> observe`, with explicit termination and bounded execution.
- Keep observation building, decision-making, action contracts, execution, and orchestration separate.
- Validate structured actions before execution.
- Expose serializable observations and element references to decision-makers; keep Playwright objects internal.
- Treat element references as belonging to the observation that produced them. Design stale-reference protection explicitly before introducing a repeated agent loop.
- Distinguish successful tool execution from verified task success.
- Make outcomes and errors explicit so future instrumentation can measure success/failure, latency, tool calls, retries, and error categories.
- Prefer small functions and concrete models over speculative abstractions.

## Development rules
- Make small, focused changes that serve the current development stage.
- Keep module imports free of browser launches, network calls, and other execution side effects.
- Keep experimental URLs and action choices in orchestration or configuration, outside reusable execution logic.
- Make browser resource ownership and cleanup explicit.
- Use type annotations at module boundaries and Pydantic for external data contracts.
- Preserve failure details; do not silently swallow errors or add unbounded retries.
- Add dependencies only when justified by the task; manage them through uv.

## Testing expectations
- Add focused tests for new behavior and regression tests for bug fixes.
- Cover action validation, reference resolution, observation construction, execution outcomes, and termination as these capabilities are implemented.
- Prefer deterministic tests using controlled HTML and test doubles.
- Keep live-site experiments separate from deterministic tests.
- Do not treat a completed click as proof of task success.

## Agent workflow
Before modifying code:
1. Read relevant modules, tests, `pyproject.toml`, and `README.md`.
2. Identify the requested scope, affected contracts, and appropriate validation.
3. Explain the intended change briefly in Spanish. Respect analysis-only requests.

After modifying code:
1. Run relevant validation, then the available test suite when appropriate.
2. Review the diff for unintended changes and unnecessary dependencies.
3. Report changes, validation results, and remaining limitations in Spanish.
4. State clearly which checks were not run. Never claim unperformed validation.

## Validation commands
- `uv run pytest`: run the test suite.

No lint, formatting, or type-check commands are currently configured. Do not assume they exist. uv may synchronize dependencies; respect any restriction on installation or file changes.

## Language conventions
- Communicate with the developer in Spanish.
- Write source code, identifiers, comments, documentation, configuration, commit messages, and other repository artifacts in English.
- Keep established technical terms in English when translating them would reduce clarity.

## Avoid
- Integrating an LLM before the controlled loop is validated.
- Adding LangChain, LangGraph, CrewAI, or similar agent frameworks without an explicit architectural decision.
- Premature abstractions, unnecessary dependencies, and unrelated refactors.
- Coupling reusable logic to AutomationExercise or hardcoded element positions.
- Exposing Playwright objects to the agent.
- Building a metrics platform before execution contracts are stable.
- Modifying the repository when the task is explicitly analysis-only or proposal-only.
