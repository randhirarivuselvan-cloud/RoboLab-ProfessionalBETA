# RoboLab Universal Professional v4.0.0

RoboLab is a modular multi-AI robotics engineering workspace under SynapseX Robotics & Technologies.

## AI architecture

USER IDEA → ROBO LAB CORE → BUILDER AI + CIRCUIT AI + CODE AI → UNIFIED PROJECT → VERIFICATION AI 1 + VERIFICATION AI 2 → CONSENSUS AI → PASS / REVISE.

The Builder, Circuit and Code engines operate against one canonical project specification. Cross-stage dependency checks detect mismatched components, pins, interfaces and controller assumptions instead of silently accepting conflicts.

The two verification agents independently review the unified project. Consensus produces PASS or REVISE. Revision returns to the affected engineering engines and repeats the cycle.

## Provider configuration

AI is provider-abstracted. Set `AI_PROVIDER` and `AI_API_KEY` on the server; never place keys in frontend code. `AI_PROVIDER=none` is the safe default and reports that an AI provider is not configured rather than pretending an agent is active.

The included adapters cover OpenAI-compatible HTTP APIs, Anthropic, Google Gemini, and a local HTTP-compatible provider. Different stage models can be configured with the `*_MODEL` environment variables.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## Tests

```bash
pytest -q
```

## Production

The project includes `render.yaml` with the required Render start command. SQLite is suitable for development; the database layer is isolated so PostgreSQL can be introduced later.

Physical hardware still requires appropriate engineering validation and human review. RoboLab does not claim physical safety or zero errors.
