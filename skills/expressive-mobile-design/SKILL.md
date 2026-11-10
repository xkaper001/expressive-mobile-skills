---
name: expressive-mobile-design
description: Designs and reviews expressive mobile interfaces with warm surfaces, bold rounded typography, deliberate accent colors, and accessible light and dark themes. Use when choosing a mobile visual direction, designing screens, or reviewing mobile UI independent of framework.
license: MIT
---

# Expressive Mobile Design

Turn the user's product and content into a coherent mobile interface. The reference
language comes from study of Fix Yo Yap, but the result should have its own identity.

## Establish the task

Read the existing brief, screens, design tokens, and project conventions. Infer
the framework and platform targets when available. Ask only for missing product
information that changes the design. Do not make the user repeat existing context.

Name the main task, primary action, content hierarchy, and relevant states. For
a redesign, preserve working behavior and the established identity. For a new
app, develop the real core screen before a large suite of secondary screens.

Read [the design reference](references/design-system.md) before choosing tokens
or components. It distinguishes observed colors and patterns from suggested
dimensions, accessibility improvements, and unmeasured motion.

## Design the screen

- Choose a quiet neutral canvas and intentional light/dark surface roles.
- Build hierarchy with weight, size, and space before adding decoration.
- Give the main action a strong contrast and a concrete verb.
- Use saturated panels where a feature deserves emphasis; keep utility work calm.
- Choose meaningful grouping instead of making every element a card.
- Treat a floating dock, a mascot, diagonal ribbons, and card rotation as optional.
- Keep original product text, symbols, and assets; do not copy the reference brand.

For example, a practice app might use one colored practice panel, neutral history
rows, and a persistent main action. A finance app may need only the typography,
spacing, and surface discipline, with a more restrained accent strategy.

## Translate to a framework

If implementation is requested, use the project's existing stack. Companion
skills for Flutter, React Native, Compose, and SwiftUI add framework-specific
guidance when installed; they are not required dependencies. Never rewrite the
app just to match the reference app's React Native implementation.

Make semantic tokens and reusable components only where repetition justifies
them. Preserve native navigation, text scaling, accessibility semantics, input,
permissions, and keyboard behavior. Adapt layout at narrow widths and large type.

## Review and deliver

Review an actual render when the environment supports it, checking themes,
large text, long labels, keyboard insets, action states, and scroll clearance.
Explain concrete visual decisions and any observed usability issues. Separate
source evidence, new design choices, and behavior that was not verified.

When presenting a new direction, show the core screen and briefly explain its
hierarchy so the user can review it before extending the design. Do not block
already-authorized implementation with an additional approval gate.
