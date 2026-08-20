---
name: self-contained-output
description: Use whenever creating or editing content that lives as a file or artifact outside the chat - scripts (PowerShell/Python/Bash), source files, notebooks, README/Markdown, Word/PDF, HTML/CSS/JS/React and UI copy, Dockerfiles, IaC, CI/CD YAML, config, SQL - anything bound for GitHub, another org, or a teammate. Use when draft artifact text mentions "you", "we discussed", "as requested", "the file you sent", or other conversation references. Do NOT use for in-chat conversational answers.
license: MIT
compatibility: claude-code opencode
---

# Self-Contained Output

## Overview

Files leave the chat; the reader has none of its context. Text inside an artifact that addresses the requester or references the conversation is a defect. Canonical bug: a header reading "One trade-off you already signed off on: ..." - the reader does not know who "you" is or what was signed off.

## Scope

Governs text INSIDE the artifact: comments, docstrings, headers, doc prose, UI copy, help text, error messages, sample data. Not the chat message alongside it - talk normally there. When editing, apply to changed text and fix bleed in touched sections.

## Rules

1. **No requester references or assumed history.** Ban "as we discussed", "per our chat", "earlier we decided", "you asked for", "as requested", "you signed off/accepted", "your test user", "your tenant", "the file you sent", and equivalents. Rewrite as neutral fact or delete.

2. **No assistant voice or meta-commentary.** Ban "I", "we", "let me", "as an AI", apologies, "here's the updated version", "now with the fix you requested", changelog asides to the reader. Exception: a real CHANGELOG or version-history section about the artifact, written neutrally ("1.2.0 - Added retry logic for 429s").

3. **Caveats go in a neutral "Known issues" or "Limitations" section.** State trade-offs and risks as facts; acceptance is the reader's call. Not "a trade-off you accepted" - write "Known issue: X. Impact: Y."

4. **Artifact stands alone.** Every sentence must make sense to someone who never saw the chat. No dangling references to prior messages, uploads, decisions, or "the previous version". Required context gets restated inside the artifact.

5. **Generic placeholders.** Use `<tenant>`, `your-org.com`, `user@example.com`, contoso-style values - not values recalled from chat - unless a concrete value is genuinely part of the deliverable (for example a config file written for one named environment, where the user asked for that exact value).

## Second person: allowed vs forbidden

- ALLOWED - instructional voice for any future reader: "You must be a Global Administrator", "Run this once per tenant", "Set `-WhatIf` to preview."
- FORBIDDEN - "you" presuming this requester or this conversation: "the account you mentioned", "you already approved this".
- Test: if the sentence still holds for a stranger cloning the repo in a year, it passes.

## Do not over-correct

Technical terminology is not bleed. Keep domain terms, exact cmdlet/API names, RFC references, product jargon. The rule targets register and references, not vocabulary. Do not strip specifics that belong in the deliverable. First-person plural in quoted academic or standards prose ("we show that...") is source content, not assistant voice.

## Pre-finalize self-check

1. Scan for: I, we, you, our, "as discussed", "as requested", "signed off", "uploaded", "earlier", "previous version". Judge each hit against the rules - instructional "you" passes.
2. Every caveat or risk sits in a neutral Known issues / Limitations section.
3. A zero-context reader understands every sentence.
4. Placeholders are generic unless the concrete value is part of the deliverable.

Fix violations, then emit.

## Examples

**1 - script header caveat**

Before:
```powershell
# One trade-off you already signed off on: links are removed
# permanently; there is no undo.
```
After:
```powershell
# Known issues
# - Link removal is permanent; no undo. Export and review the
#   BEFORE CSV before running against production.
```

**2 - README rationale**

Before: "As we discussed, this uses delegated permissions because you preferred audit trails."
After: "Uses delegated permissions so every action is attributable to the signed-in operator in the audit log."

**3 - code comment meta-commentary**

Before: `// Here's the updated version with the retry logic you asked for`
After: `// Retries transient 429/503 responses with exponential backoff (max 5 attempts)`

**4 - UI copy**

Before: "Upload the CSV you sent earlier to continue."
After: "Upload a CSV export (see Format requirements below) to continue."

**5 - config sample data**

Before:
```yaml
tenant: contoso-inciro.onmicrosoft.com  # your tenant
```
After:
```yaml
tenant: <tenant>.onmicrosoft.com
```
