# n8n Workflow Stats — Analysis Package

Reusable analyzer behind the "I Analyzed 2,046 n8n Workflows" article.

## Files
- `analyze.py` — scans any folder of n8n workflow JSONs, prints + saves stats
- `results.json` — results from the 2,046-workflow sample (the article's numbers)

## Run it
```bash
python3 analyze.py /path/to/workflows --out results.json
```

## Headline findings (from `results.json`)
- 2,046 valid workflows · median **11 nodes** · 76% under 20 nodes
- #1 node: **HTTP Request** (2,123 instances) — the universal adapter
- **Google Sheets (597)** used 2.3x more than Airtable (255) — the spreadsheet is the database of automation
- **Telegram (390)** beats Slack (198) nearly 2:1
- **181 chat triggers** — the AI agent wave, quantified
