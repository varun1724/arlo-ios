---
name: notification-engine
description: Implement Arlo's actionable, adaptive notification workflows.
---

# Purpose
Use this skill for all reminder, scheduling, and task-prompt work.

# Product behavior
Notifications are Arlo's primary driver of action.

Each notification should:
- be short
- be contextual
- point to one action
- support quick actions:
  - done
  - snooze
  - skip

# MVP behaviors
Support:
- day start prompt
- workout prompt
- post-gym prompt
- lunch prompt
- steps reminder
- posture reminder

# Adaptation
If a task is skipped:
- do not escalate harshly
- update the plan
- move tasks forward if appropriate

# Technical guidance
- isolate scheduling logic from view code
- centralize notification identifiers and categories
- make notification payloads predictable
- support quick action handling cleanly

# UX guidance
Notification copy should sound like Arlo:
- direct
- useful
- calm
- not robotic
- not guilt-heavy
