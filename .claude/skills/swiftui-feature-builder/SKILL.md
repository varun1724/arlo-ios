---
name: swiftui-feature-builder
description: Build SwiftUI features for Arlo with clean separation of view, state, and services.
---

# Purpose
Use this skill when implementing new SwiftUI features.

# Rules
- Keep business logic out of views
- Use small observable models or view models only where needed
- Prefer feature-local files
- Avoid giant all-in-one view files
- Compose from smaller reusable pieces
- Keep navigation simple and native

# Output expectations
When building a feature:
1. identify required models
2. identify service dependencies
3. build a minimal view tree
4. wire state
5. provide preview data
6. summarize what remains

# For Arlo specifically
Prioritize these flows:
- Today screen
- task list and completion
- workout and meal prompts
- voice entry
- simple progress status

# UI constraints
- Keep typography restrained
- Avoid overly decorative containers
- Use standard SwiftUI building blocks first
- Prefer a calm utility-app feel over a flashy AI feel
