# Claude Code Prompt Sequence

## Prompt 1 — bootstrap
Read the project spec in CLAUDE.md and PROJECT_SPEC.md and help me bootstrap Arlo as a real SwiftUI iOS app.

Goals for this task:
- inspect the repo
- propose a clean folder structure
- create the initial folder structure
- create the app entry point and root navigation
- create a minimal Today screen shell
- create placeholder feature folders for onboarding, notifications, voice, meals, activity, learning, ideas, settings, widget, and intents
- do not over-engineer
- keep the UI calm, native, and minimal
- summarize what you created and what the next milestone should be

## Prompt 2 — design foundation
Implement a lightweight design foundation for Arlo.

Requirements:
- create spacing, typography, color, and container primitives only if genuinely useful
- keep everything native-feeling
- avoid generic AI app aesthetics
- do not add flashy gradients or decorative UI
- build a simple design system that supports the Today screen and future features
- provide a short rationale for each design choice

## Prompt 3 — Today screen
Build the MVP Today screen for Arlo.

The Today screen should show:
- a greeting / current state
- non-negotiables section
- next up section
- progress section
- one learning brief card
- one startup idea card
- expandable details only where useful

Requirements:
- use realistic mock data
- prioritize hierarchy and calm UI
- make the next action obvious
- keep copy concise
- do not make it look like a card soup dashboard
- provide SwiftUI previews

## Prompt 4 — task and routine model
Design and implement the core task and routine model for Arlo.

Need:
- daily tasks
- task categories
- completion state
- snooze/skip state
- recurring routines
- push/pull/legs support
- meal tasks
- posture tasks
- learning tasks

Requirements:
- keep models simple
- separate planner logic from view code
- create a sample planner that generates a day from mock user preferences
- explain the model briefly after implementation

## Prompt 5 — notifications
Implement the MVP notification engine for Arlo.

Needs:
- day start prompt
- workout reminder
- post-gym reminder
- lunch reminder
- steps reminder
- posture reminder

Requirements:
- define notification categories and identifiers cleanly
- include quick actions: done, snooze, skip
- structure code so handling notification actions can update task state
- do not build every future notification
- keep it clean and extensible
- summarize any iOS permission/setup steps I need

## Prompt 6 — onboarding and geofence
Build onboarding for Arlo focused on MVP setup.

Need screens for:
- core goals
- workout split
- meal style
- step target
- posture/mobility preference
- gym location setup
- learning interests

Requirements:
- keep onboarding short
- avoid too many questions
- support one main gym geofence for MVP
- explain what would be mocked versus production-ready

## Prompt 7 — voice input
Build the MVP voice interaction flow for Arlo.

Need:
- simple tap-to-talk screen or sheet
- transcript display
- placeholder assistant response rendering
- basic intent routing for example commands like:
  - what should I do now
  - I already worked out
  - I played tennis
  - what should I eat
  - give me the tech brief

Requirements:
- keep the UI minimal
- short responses only
- architecture should support future real speech and intent parsing

## Prompt 8 — widget and shortcuts
Plan and begin implementation for Arlo's widget and App Shortcut integration.

Need:
- a simple widget concept showing next up and a quick entry into Arlo
- a realistic App Shortcut strategy for:
  - Talk to Arlo
  - Start my day
  - Log workout complete
  - Play today’s brief

Requirements:
- follow iOS conventions
- keep the shortcut count limited to the highest-value flows
- explain what is practical for MVP versus later

## Prompt 9 — learning and ideas
Create the MVP structure for learning briefs and startup ideas.

Need:
- model types for briefs and ideas
- Today screen integration with mock data
- simple detail views
- architecture that allows future fetched or generated content

Requirements:
- focus on product shape, not backend completeness
- keep details useful but lightweight
- do not build a huge feed

## Prompt 10 — builder mode
Add the product architecture for Builder Mode without fully implementing it.

Need:
- a Builder Mode model layer
- a structured MVP spec generator format
- a placeholder screen or action flow that shows how Arlo would turn an idea into:
  - summary
  - target user
  - features
  - MVP scope
  - Claude Code prompt

Requirements:
- design the flow cleanly
- keep it future-facing
- do not overbuild autonomous coding yet