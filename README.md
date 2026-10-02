# Awesome n8n Workflows

> 25 battle-tested n8n workflows, hand-picked from an index of 38,000 — growing weekly.

**[🔍 Search all 38,000 workflows](https://n8n-enterprise-suite.pages.dev/)** — filter by department and integration, copy the JSON, paste it straight onto your n8n canvas (Ctrl+V). Free 30-minute full-access demo.

## Why this exists

Starting from a blank n8n canvas is slow. Starting from a proven workflow is fast — I measured it: 4h 20m from scratch vs 38 minutes from a template. This repo collects the best starting points I've found, verified to import cleanly (credentials stripped, no secrets, no instance IDs — n8n prompts for your own credentials on paste).

## The Workflows

### 🤖 AI Assistants

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 1 | AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram | OpenAI, Memory, Google Docs, Telegram | 21 | Telegram AI chatbot with long-term memory stored in Google Docs — remembers past conversations and takes notes. |
| 2 | AI Email Autoresponder with Approval Step | IMAP Email, OpenAI, Email, Qdrant | 17 | Reads incoming email with AI, drafts replies, and waits for your Yes/No approval before sending. |
| 3 | Human-in-the-Loop AI Email Responder | IMAP Email, Email, AI Summarizer, AI Agent | 16 | Simple IMAP email system where AI drafts every response and a human approves — inbox on autopilot with oversight. |
| 4 | AI Google Calendar Assistant | OpenAI, Memory, Google Calendar, AI Agent | 13 | Chat with your calendar: create, check and manage events through an AI agent connected to Google Calendar. |
| 5 | AI YouTube Video Summarizer | YouTube Transcripts, Telegram, YouTube, OpenAI | 12 | Send a YouTube link via webhook, get an AI summary and analysis back — delivered to Telegram. |
| 6 | AI Backend for Chrome Extension | OpenAI | 5 | Minimal webhook backend: Chrome extension sends text, OpenAI processes it, JSON comes back. |
| 7 | Chat with PDF Docs (AI, with sources) | OpenAI, Pinecone, Google Drive, PDF | 22 | Upload PDFs from Google Drive to a Pinecone vector store, then chat with your documents — answers quote their sources. |

### 💰 Sales & CRM

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 8 | AI Lead Handler for Pipedrive + Gmail | Pipedrive, OpenAI, Gmail | 11 | New Gmail leads get AI-qualified and pushed to Pipedrive with smart routing and follow-up logic. |
| 9 | AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack | OpenAI, LLM, RSS Feed, AI Classifier | 31 | Scheduled monitor that watches sources with AI, logs findings to Google Sheets on autopilot. |
| 10 | Typeform Lead Router | Typeform, Google NLP, Notion, Slack | 6 | Typeform submissions get AI-scored, then routed to Notion, Slack and Trello automatically. |

### 📣 Marketing

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 11 | Post New YouTube Videos to X | X (Twitter), OpenAI, YouTube | 6 | Watches your YouTube channel and auto-posts new videos to X with AI-written captions. |
| 12 | Blog Content Automation | Google Sheets, OpenAI, LLM, HTTP API | 35 | End-to-end blog pipeline: scheduled topics, AI drafting, Sheets tracking — publish consistently hands-free. |
| 13 | AI WordPress Auto-Categorizer | WordPress, OpenAI, AI Agent | 9 | New WordPress posts get automatically categorized by AI — no more manual taxonomy. |
| 14 | Hugging Face → Notion Curator | HTTP API, Notion, OpenAI | 11 | Scheduled curation of trending Hugging Face models and papers straight into your Notion database. |

### 🛒 E-commerce

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 15 | Printify Catalog Updater | HTTP API, Google Sheets | 26 | Bulk-updates Printify product titles and descriptions from Google Sheets — scale your POD catalog fast. |

### 💬 Communication

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 16 | Agentic Telegram AI bot with LangChain nodes and new tools | OpenAI, Memory, Telegram, HTTP API | 8 | Lightweight agentic Telegram bot with LangChain — tools, memory and fast replies. |
| 17 | Discord AI Bot | OpenAI, Discord | 9 | Discord bot powered by OpenAI — answers questions in your server on demand or via webhook. |
| 18 | Slack AI Agent (Gemini) | Gemini, Memory, Slack, AI Agent | 10 | Slack bot with a Gemini agent brain — answers team questions via webhook trigger. |

### 📊 Data & Analytics

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 19 | Chat with Postgresql Database | AI Agent, OpenAI, Postgres, Memory | 11 | Ask questions about your Postgres database in plain English — AI agent translates to SQL and answers. |
| 20 | Generate SQL queries from schema only - AI-powered | OpenAI, Memory, MySQL, AI Agent | 29 | Point AI at your MySQL schema and generate correct SQL queries from plain-English requests. |
| 21 | Anomaly Detection Monitor | HTTP API | 17 | Detects anomalies in datasets on a schedule — flags outliers from HTTP data sources. |

### 🧑‍💼 HR & Recruiting

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 22 | HR Policy Q&A Bot (BambooHR) | Doc Loader, OpenAI, Text Splitter, Memory | 50 | Employees ask HR policy questions in chat — AI answers from BambooHR data with embeddings. |

### 🛠️ Support & Ops

| # | Workflow | Integrations | Nodes | What it does |
|---|----------|--------------|-------|--------------|
| 23 | Linear → Slack AI Triage | Slack, OpenAI, Structured Output, Linear | 19 | New Linear issues get AI-analyzed and summarized into Slack — triage without the meeting. |
| 24 | Zoom AI Meeting Assistant | OpenAI, Zoom, HTTP API, Email | 24 | Pulls Zoom meeting data and generates AI summaries and action items automatically. |
| 25 | Smart Form Processor | Typeform, Google NLP, Notion, Slack | 6 | Form submissions flow into Airtable and trigger Gmail follow-ups — intake to response in one flow. |

## How to import

1. Find a workflow in the [vault](https://n8n-enterprise-suite.pages.dev/) (or request one below)
2. Copy the workflow JSON
3. Click your n8n canvas and press **Ctrl+V** (Cmd+V on Mac) — all nodes appear
4. Connect your credentials when prompted → Execute → toggle Active

## 📊 By the numbers

From analyzing 2,046 workflows in the index:
- Median workflow: **11 nodes** — 76% are under 20 nodes
- #1 node overall: **HTTP Request** (the universal adapter)
- **Google Sheets** used 2.3x more than Airtable — the spreadsheet is the database of automation
- **Telegram** beats Slack 2:1 for notifications
- **181 chat triggers** — the AI agent wave, quantified

Full analysis + reusable script: [`n8n-workflow-stats/`](./n8n-workflow-stats/)

## Contributing

Found a great workflow? PRs welcome — one workflow per PR:
- Paste the sanitized JSON (no credentials, no instance IDs) as a `.json` file
- Add a row to the table above: name, integrations, node count, one-line description
- Confirm it imports cleanly into n8n 1.x via Ctrl+V paste

## License

Workflows are shared as-is for learning and commercial use. Individual templates may depend on third-party APIs with their own terms.
