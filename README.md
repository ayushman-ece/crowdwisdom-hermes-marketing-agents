# CrowdWisdom Hermes Marketing Agents

## Overview

This project is an AI-powered multi-agent marketing backend built using the Hermes Agent Framework.

It automates the complete workflow of researching successful advertisements, extracting marketing insights, generating ad scripts, preparing video generation prompts, and producing structured reports.

---

## Architecture

```
User Input
      │
      ▼
Ads Manager
      │
      ▼
Marketing Analyzer
      │
      ▼
Script Agent
      │
      ▼
Video Agent
      │
      ▼
Telegram + Reports
```

---

## Agents

### Ads Manager Agent

- Searches Meta Ads
- Selects top-performing ads
- Saves results to JSON

### Marketing Analyzer

- Extracts:
  - Pain Points
  - Marketing Angles
  - Customer Problems
  - Winning Concepts

### Script Agent

Generates AI marketing scripts including:

- Hook
- Problem
- Solution
- CTA

### Video Agent

Generates:

- Video Prompt
- Storyboard
- Video Metadata

Compatible with OpenMontage.

---

## Features

- Hermes Agent Framework
- OpenRouter LLM
- Apify Integration
- Telegram Integration
- Kanban Workflow
- JSON Reports
- Markdown Reports
- Logging
- Modular Agent Architecture

---

## Output

```
outputs/

ads/
analysis/
scripts/
videos/
reports/
logs/
```

---

## Tech Stack

- Python
- Hermes
- OpenRouter
- Apify
- Telegram
- OpenMontage

---

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=YOUR_KEY
APIFY_API_TOKEN=YOUR_TOKEN
TELEGRAM_BOT_TOKEN=YOUR_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

Run:

```bash
python main.py
```

---

## Output Files

- ads.json
- analysis.json
- scripts.json
- video_prompt.txt
- storyboard.json
- execution_report.json
- execution_report.md
- kanban.md

---

## Author

Ayushman Tiwari