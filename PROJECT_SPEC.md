# ARLO — MASTER PRODUCT SPEC

## Product Summary
Arlo is a voice-first, notification-driven personal operator for iPhone.

Its purpose is to reduce decision fatigue, reduce passive phone usage, and proactively guide the user through the day based on goals, routines, and real-time context.

Arlo is not a generic habit tracker, not a simple chatbot, and not a passive planner. It is an adaptive assistant that tells the user what to do next, reminds them at the right time, lets them respond naturally by voice, and updates the day accordingly.

## Core Product Philosophy

### Layer 1: Non-Negotiables
- workout
- steps/activity
- meals/nutrition
- posture/mobility

### Layer 2: Adaptive Intelligence
- tech/news learning
- startup ideas
- product/building tasks
- research and interesting things to explore

### Layer 3: Context Engine
- time of day
- first phone interaction
- location
- gym arrival/departure
- completion status
- remembered preferences
- voice input

## User Goals
Arlo is initially built for a user who wants to:
- get into peak shape over the next few months
- enforce fitness, meals, steps, posture, and mobility every day
- stay current on tech, AI, startups, and interesting developments
- receive startup ideas that are fewer, deeper, and more researched
- stay off the phone and be told the next right thing
- use voice naturally to update plans and ask questions
- eventually turn startup ideas into MVP specs and coding handoffs

## Primary Interaction Model

### 1. Notifications
Examples:
- Pull day. Leave for gym in 20 min.
- Just got home. Take creatine + protein now.
- Lunch at home: tofu rice bowl.
- You still need 3,200 steps.
- 8 min posture reset tonight.

Quick actions:
- Done
- Snooze
- Skip

### 2. Voice
Examples:
- What should I do now?
- I already worked out
- I played tennis
- What should I eat?
- Give me the tech brief
- Give me startup ideas
- Adjust tomorrow

### 3. Today Screen
Should show:
- today’s non-negotiables
- next up
- progress
- one learning brief
- one idea or build prompt

### 4. Audio Briefs
Use cases:
- driving home from gym
- walking
- passive afternoon learning

Length:
- 2–3 min typical
- 10 min max

## Daily Lifecycle

### Day Start
Triggered by the first meaningful phone interaction in the morning.
Arlo should confirm activation with:
- You up?

### Gym Flow
User defines one main gym location.
Use geofencing to detect:
- arrival
- departure

### Meal Flow
Meals should be:
- conversational
- flexible
- rotational
- grocery-aware

### Steps / Activity Flow
Track where possible, but allow manual voice correction:
- I played tennis today
- I got cardio in already
- I walked but didn’t have my phone

### Posture / Mobility Flow
Short daily reminders and guided routines.

## Learning Engine
Content categories:
- AI models and releases
- AI infrastructure and tooling
- developer tools
- startups and fundraising
- consumer tech when interesting
- research papers
- career-relevant trends

## Startup Idea Engine
Generate fewer, better, more researched ideas.

Each idea should ideally include:
- problem
- target user
- why now
- wedge
- feasibility
- why it suits the user
- next action

## Adaptation Behavior
If the user skips something:
- do not escalate harshly
- do not shame
- adjust the day
- move tasks forward if reasonable
- keep momentum

## Memory System
Remember only relevant long-term context:
- routines
- schedule patterns
- goals
- meal preferences
- favorite foods
- dislikes
- learning interests
- startup themes
- recurring constraints
- behavior patterns

## Modes
Future support for:
- Lock-In Mode
- Work Mode
- Travel Mode
- Weekend Mode

User should also be able to adjust plans conversationally.

## Siri / Voice Entry
MVP options:
- tap mic in app
- tap mic from widget
- Siri Shortcut / App Shortcut path:
  Hey Siri, talk to Arlo

## Builder Mode / Claude Code Handoff
Future feature, not core MVP.

### Phase A
Arlo generates:
- product summary
- target user
- feature list
- MVP scope
- stack recommendation
- milestone plan
- Claude Code prompt

### Phase B
Arlo hands a task to Claude Code / agent workflow.

### Phase C
Arlo tracks background build tasks and reports back.

## Core MVP Scope

### Must-Have
- onboarding for goals/routines/gym
- Today screen
- notification engine
- notification quick actions
- task model
- daily plan generation
- workout split support
- steps/activity support
- meal suggestion system
- posture/mobility tasks
- voice input and basic conversational loop
- relevant memory layer
- gym geofence
- widget with next action and mic entry

### Should-Have
- Siri Shortcut / App Shortcut integration
- short readable learning briefs
- startup idea summaries
- short audio brief generation hooks in product design, even if mocked first

### Future
- richer learning engine
- researched startup engine
- Builder Mode
- autonomous Claude Code handoff
- adaptive notification timing based on behavior
- better personalization over time

## Product Principles
- Reduce decisions
- Keep the next action obvious
- Be proactive but not overwhelming
- Minimize screen time
- Prefer short interactions
- Adapt based on real life
- Keep fitness non-negotiables strong
- Keep learning and ideas useful, not noisy
- Make the app feel calm, premium, and real
- Never let the interface feel cluttered or generic

---

## Expanded Product Vision: Arlo as a Personal Operator Platform

Arlo should not be limited to health, routines, and daily guidance.

Long-term, Arlo should become a generalized personal operator that can help the user across multiple domains by combining:
- memory
- research
- ranking
- recommendations
- drafted actions
- tool-based execution with approval

The product vision is not “an AI that can do anything blindly.”
The product vision is “an assistant that can coordinate many kinds of real-world tasks in a structured, trustworthy way.”

---

## Core Domains

### 1. Health and execution
- workouts
- meals
- posture/mobility
- steps/activity
- routines
- daily planning

### 2. Learning and briefings
- tech/news summaries
- AI/dev/startup/research updates
- short briefs
- audio brief generation

### 3. Ideas and building
- startup ideas
- MVP specs
- build plans
- Claude Code handoff
- Builder Mode

### 4. Career
- find relevant jobs
- rank jobs by fit
- track applications
- draft tailored applications
- prepare outreach
- eventually submit applications with approval

### 5. Opportunities and research
- scan properties in an area
- compare listings
- estimate flip potential using structured criteria
- shortlist candidates
- generate underwriting-style summaries
- support decisions, not replace judgment

### 6. Side hustles and automation
- research automatable side hustles
- rank them by feasibility
- generate execution frameworks
- scaffold workflows, tools, or MVPs for testing

---

## General Operating Pattern

For every domain, Arlo should follow the same progression:

1. Clarify goal  
2. Gather relevant context  
3. Research and collect options  
4. Score and rank options  
5. Draft recommended actions  
6. Execute only when permitted  

---

## Tooling Model

Arlo should act as an orchestration layer over specialized tools and agent workflows.

Examples:
- web research tools
- MCP connectors
- browser / computer-use workflows
- Claude Code / Agent SDK build workflows
- structured ranking systems
- persistent user memory

---

## Approval Model

Arlo should not automatically take high-impact actions without user confirmation.

Sensitive actions require explicit approval:
- submitting job applications
- sending emails or outreach
- financial decisions
- modifying external accounts
- launching long-running tasks
- sharing or storing sensitive data

---

## Product Principle

Arlo should be ambitious in capability but conservative in execution.

It should:
- research broadly  
- reason clearly  
- draft aggressively  
- execute carefully  

I want to add a real AI backend architecture to Arlo.

Do not turn the app into a giant monolithic AI agent.

Instead, design a clean backend system that supports:
- structured user memory
- behavioral learning over time
- voice intent parsing
- daily plan generation
- brief generation
- startup idea generation
- planner adaptation based on user events

I want:
1. a backend architecture proposal
2. recommended stack for MVP
3. core database models
4. service boundaries
5. what should stay on-device vs backend
6. a phased implementation plan

Keep it practical and MVP-focused.
Do not overbuild autonomous multi-agent systems yet.
Before writing code, show the architecture and plan first.