Notemine Project Scope Document
1. Overview

Notemine is a local-first system that processes Obsidian Markdown notes and enriches them using LLMs (local via Ollama or remote APIs such as OpenAI/Claude). The system extracts structured metadata from each note and writes it back into the original files.

Supported note languages: Dutch, English, French.

All semantic outputs (NER, tags, summaries) are always generated in English regardless of source language.

2. Core Objectives
Parse .md files from an Obsidian vault
Perform LLM-based enrichment per note:
Named Entity Recognition (NER)
Tag generation
Structured summary
Write results back into the original Markdown file (in-place modification)
3. Processing Pipeline
3.1 Execution Model

Linear batch pipeline:

Scan vault (full traversal each run)
Load note content
Send to LLM
Extract structured metadata
Write back into Markdown frontmatter

No incremental processing, no event-driven updates.

4. Language Policy
Input notes: multilingual (NL, EN, FR)
Output metadata: always English
No translation of full note content
Only extracted semantic artifacts are normalized to English
5. LLM Integration
5.1 Supported backends
Local models via Ollama
Remote APIs (OpenAI, Claude)
5.2 Mode
Fully configurable backend selection per run or task
No fallback logic specified at system level
6. Data Storage
No external database
Notes remain single source of truth
Metadata stored directly in Markdown frontmatter
7. NLP Enrichment Per Note

For each note:

7.1 Named Entity Recognition (NER)
Output format: flat list
Structure: ["entity", "type"]
No entity resolution or linking across notes
7.2 Tags
Generated as free-form tags
No taxonomy constraints
LLM decides tagging schema implicitly
7.3 Summary
Structured summary (bullet points)
Focus on key ideas and entities
No strict length constraint beyond conciseness requirement
8. Orchestration
Simple sequential batch pipeline
Deterministic execution order
No DAG, no parallelization, no agent planning
9. Output Format (Markdown Frontmatter)

Each note is updated with enriched metadata, e.g.:

entities: list of [entity, type]
tags: list of strings
summary: bullet list structure
10. System Properties
Local-first design
Deterministic batch execution
No external indexing layer
No embeddings or clustering
Minimal architectural complexity
Optimized for reproducible enrichment runs
