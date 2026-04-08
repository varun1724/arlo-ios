---
name: ios-product-guardrails
description: Guardrails for making Arlo feel like a polished real iOS app instead of a generic AI-generated prototype.
---

# Purpose
Use this skill whenever designing screens, flows, interaction patterns, or visual styling.

# Product identity
Arlo is a voice-first, notification-driven personal operator.
It must feel:
- calm
- premium
- native
- focused
- practical

It must not feel:
- cluttered
- gimmicky
- over-animated
- card-spammed
- gradient-heavy
- chatbot-first

# Design rules
- Prefer native SwiftUI controls and navigation patterns
- Keep one clear primary action per screen
- Use restrained spacing and typography
- Avoid stacking too many cards or pills
- Avoid decorative glass, glow, shadows, and novelty UI unless there is strong product value
- Use concise copy
- Default to plain backgrounds and structured layout
- Favor hierarchy over ornament

# Today screen rules
The Today screen should show:
- non-negotiables
- next up
- progress
- one learning item
- one idea item

At first glance, it should answer:
- what matters today?
- what should I do next?
- what is done already?

# Voice screen rules
Voice UI should be simple:
- large mic affordance
- clear active/listening state
- compact transcript
- short responses

# Notification rules
Notifications should:
- be short
- be specific
- map to one action
- support done/snooze/skip
- avoid long paragraphs

# Anti-vibe-code checklist
Before finalizing a UI, check:
- Is there a clear hierarchy?
- Does the app use mostly native patterns?
- Can I remove 20 to 30 percent of UI and improve clarity?
- Is there a single obvious next action?
- Does this look like an actual utility app someone would trust daily?
