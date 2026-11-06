# TechBit 💡 — One Technical Concept Every Day

A tiny daily-learning web app, built to teach Python and AI engineering incrementally.

## What V1 does

- Displays the same technical concept to everyone on the same calendar date (based on the running server's local date).
- Explains the concept, shares an analogy and example, and links to hand-curated references.
- Lets users explore a catalog of concepts without signing in or using an API key.

This is **not yet an AI app**. That is intentional: V1 gives us a simple working baseline. V2 will add an LLM-generated explanation and follow-up Q&A while keeping references sourced from a trusted catalog.

## Start locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` (or run `.venv\Scripts\python -m streamlit run app.py` directly).

Open the local URL Streamlit prints in the terminal.

## Tests

```bash
python -m pytest -q
```

## Project structure

- `app.py`: the Streamlit user interface
- `catalog.py`: data and deterministic daily rotation
- `tests/test_catalog.py`: basic correctness checks

## Learning milestones

1. **V1 (this repository):** UI, Python dicts/lists, modular code, dates, deterministic logic, and tests.
2. **V2:** add an LLM API for adaptive explanations and user's follow-up questions; handle API errors and secrets using `.env`.
3. **V3:** require structured model outputs, evaluate accuracy, cache repeated queries, and measure token costs.
4. **V4:** SQLite bookmarks, explore history, and user preferences.
5. **V5:** optional scheduled notifications and mobile-friendly deployment.

## Portfolio questions

- Why not ask an LLM to choose the word every day? Deterministic selection is free, consistent, and testable.
- Why curate source links? LLMs can invent URLs; curated links are easier to verify.
- What happens after five days? The demo cycles through five concepts. Expand the catalog before production.
- What is the current limitation? No personalization, no persistence, limited topics, server-local date, and no live AI.

## Publish yourself to GitHub

Create an empty repository named `techbit`, then run:

```bash
git init
git add .
git commit -m "Build TechBit V1 daily concept app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/techbit.git
git push -u origin main
```

Do not commit API keys, `.env`, or personal data.
