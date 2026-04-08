---
name: builder-mode-spec
description: Convert product or startup ideas into structured MVP specs and Claude Code handoff prompts.
---

# Purpose
Use this skill when the user wants Arlo to turn an idea into something buildable.

# Output format
For each idea produce:
- summary
- target user
- problem
- why now
- core features
- MVP boundary
- suggested stack
- milestone plan
- Claude Code implementation prompt

# Guardrails
- prefer fewer better features
- make the scope realistic
- define what is explicitly not in MVP
- bias toward a one-week to two-week scaffold rather than a huge build

# For Arlo specifically
Builder Mode is not core MVP.
Design the data flow and product shape cleanly, but do not overbuild autonomous coding workflows in the first version.
