# CLAUDE.md

## Project
This repository is for Arlo, a voice-first, notification-driven iOS personal operator built with SwiftUI.

## Product Summary
Arlo is not a generic productivity app.
Arlo is not just a chatbot with reminders.
Arlo is a proactive daily operator built around:
- non-negotiables: workouts, meals, steps, posture/mobility
- adaptive intelligence: tech learning, startup ideas, building prompts
- short actions, minimal friction, and clear next steps

The app should feel:
- calm
- premium
- native to iPhone
- focused
- useful every day

The app should not feel:
- cluttered
- gimmicky
- over-designed
- card-spammed
- like a generic AI-generated prototype

## Expanded Vision

Arlo is being designed as a long-term personal operator platform.

In addition to health and daily routines, Arlo will eventually support:
- career tasks (job search, applications)
- opportunity analysis (real estate, investments)
- side hustles and automation systems
- product building and MVP creation

However:

MVP MUST remain tightly scoped.

Do not prematurely build:
- complex agent systems
- multi-domain automation pipelines
- background execution engines
- external integrations beyond what is necessary

Always prioritize:
- simplicity
- clarity
- clean architecture
- strong core UX

Future capabilities should be designed for, but not fully implemented.

## Core Product Philosophy

Arlo operates on three layers:

### Layer 1: Non-Negotiables
These are enforced daily and always prioritized:
- workout
- steps/activity
- meals/nutrition
- posture/mobility

### Layer 2: Adaptive Intelligence
This fills the rest of the day:
- tech/news learning
- startup ideas
- product/building tasks
- research and interesting things to explore

### Layer 3: Context Engine
This decides when and how Arlo surfaces actions:
- time of day
- first phone interaction
- location
- gym arrival/departure
- completion status
- remembered preferences
- user voice input

## Primary Surfaces
Arlo has four primary surfaces:
1. Notifications
2. Voice
3. Today screen
4. Widget / shortcut entry

Chat is secondary.
Voice is control.
Notifications drive action.
Today screen is reference.

## UX Principles
Every feature and screen should follow these rules:
- reduce decisions
- keep hierarchy obvious
- avoid clutter
- keep copy concise
- prefer one clear next action
- use native iOS patterns
- avoid “AI app” aesthetics
- default to premium, calm, minimal design
- never add unnecessary cards, pills, gradients, or decorative clutter

## Design Principles
- Use native SwiftUI components unless there is a strong reason not to
- Favor standard spacing and platform conventions
- Maintain clear visual hierarchy
- Use restrained typography
- Avoid over-designing the first version
- Make it feel like a real Apple-quality utility app
- If a screen feels busy, remove 20–30% of visible UI before adding anything else

## Product Behavior

### Day Start
The day generally starts on the first meaningful phone interaction in the morning.
Because the user may check the phone without actually being awake, Arlo should confirm activation with something lightweight like:
- You up?

If yes:
- start the day
- generate the daily plan
- activate reminders

If no:
- delay activation

### Gym Detection
The user has one main gym for MVP.
Use geofencing to detect:
- arrival
- departure

Possible flows:
- pre-gym reminder
- post-gym reminder
- creatine/protein reminder after getting home

### Meal System
Meals should be:
- conversational
- flexible
- rotational
- easy to adapt

Support:
- repeat meals
- new meal suggestions
- grocery-aware suggestions
- recipe / instruction links for new meals

### Adaptation
If the user skips something:
- do not shame
- do not escalate harshly
- do not create guilt-heavy pressure

Instead:
- adjust the day
- move missed tasks forward where appropriate
- keep momentum
- stay aligned with long-term goals

## Memory Rules
Remember relevant long-term context only:
- routines
- goals
- schedule patterns
- meal preferences
- food likes/dislikes
- learning interests
- startup themes
- recurring constraints
- behavior patterns

Do not store random one-off chatter unless it changes planning.

## Voice Rules
Voice is the main control surface.
The user should be able to say things like:
- What should I do now?
- I already worked out
- I played tennis
- What should I eat?
- Give me the tech brief
- Give me startup ideas
- Adjust tomorrow
- I’m going out tonight

Responses should be:
- short
- useful
- slightly conversational
- action-oriented
- never long and rambling

## MVP Priorities
Must prioritize:
1. onboarding
2. Today screen
3. task/routine model
4. daily planner
5. notifications
6. voice input
7. gym geofence
8. widget
9. Siri Shortcut / App Shortcut path
10. lightweight memory

## Builder Mode
Builder Mode is future-facing, not core MVP.

Long-term goal:
If Arlo surfaces a startup idea, the user can say:
- Turn that into an MVP
- Make a spec
- Scaffold this
- Hand this to Claude Code

Builder Mode should eventually support:
- MVP spec generation
- milestone plan generation
- Claude Code-ready handoff prompt
- later, background scaffold/build workflows

Do not overbuild Builder Mode in MVP.
Design for it cleanly, but keep MVP focused.

## Technical Guidance
- Prefer small, clean, testable Swift types
- Keep business logic out of views
- Separate planner, notification, memory, and voice concerns
- Use feature-based folders where reasonable
- Keep models simple
- Do not over-architect before validation
- Do not mix far-future systems deeply into MVP code paths

## Coding Style
- Use straightforward names
- Prefer clarity over indirection
- Keep files cohesive
- Keep view files readable
- Add comments only where they clarify intent

## Before Every Message
1. Read the memory index at `~/.claude/projects/-Users-varunscodingaccount-Desktop-Swift-projects-arlo-trading-engine/memory/MEMORY.md` for user context and prior decisions
2. Check the current plan file if one exists
3. Review git status and recent commits to understand current state

## Working Style
When asked to implement something:
1. inspect existing code
2. explain the plan briefly
3. implement in small steps
4. after completing non-trivial changes, use a sub-agent (Explore type) to verify the changes compile, make sense architecturally, and don't break existing patterns before presenting results
5. verify by building/testing where possible
6. summarize what changed and what remains

## What to Avoid
- giant one-shot rewrites
- over-engineered abstractions too early
- generic AI chat layouts
- multiple competing navigation patterns
- excessive animations
- too many colors
- dense dashboards
- speculative complexity for future features

## Important
Arlo should feel like a polished, real iOS product.
When making UI decisions, bias toward native clarity, consistency, and restraint.
If something feels vibe-coded, simplify it.

## AI Backend Guidance

Arlo requires a real backend intelligence layer, but MVP should not become a giant monolithic AI system.

When designing backend architecture:
- prefer structured data over vague AI memory
- keep memory hybrid: structured, behavioral, semantic
- keep planner logic mostly rule-based at first
- use AI selectively for:
  - voice intent parsing
  - summaries
  - brief generation
  - idea generation
  - recommendation text
- separate backend services by responsibility
- avoid speculative multi-agent systems in MVP

Backend architecture should support future growth into a multi-domain operator platform, but current implementation must stay focused on:
- user profile
- routines and goals
- daily tasks
- task events
- planner updates
- voice intent processing
- lightweight learning over time

Do not overbuild autonomous operators yet.
Design for them, but implement only what MVP needs.