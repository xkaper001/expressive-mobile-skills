---
name: expressive-compose
description: Builds expressive native Android interfaces in Kotlin and Jetpack Compose with semantic themes, bold type, rounded panels, and accessible actions. Use for native Android UI implementation or refinement in Compose, rather than Flutter or React Native projects.
license: MIT
---

# Expressive Compose

Adapt the visual language to native Android. This is an authored Compose mapping;
the reference APK itself uses React Native, not Compose.

## Read the project

Read [the design reference](references/design-system.md) and
[Compose implementation guidance](references/compose.md). No sibling skill is
required. Inspect the existing Compose BOM, Material usage, theme, navigation,
and ViewModel/state structure before editing.

Preserve the app's architecture and minimum SDK. Don't replace its navigation,
dependency injection, or data layer for a visual task. Infer requirements from
the current screen and brief before asking questions.

## Implement the visual system

Use `MaterialTheme` for semantic typography and color roles. Add a compact
theme-local palette for feature accents only when Material roles are insufficient.
Make the requested surface roles explicit instead of letting dynamic color
silently replace a chosen brand palette.

Use content-sized controls with minimum targets, rounded neutral panels, and one
clear primary action. Saturated feature panels should carry useful content, not
replace the whole screen. Read the reference's accessibility adjustments before
using its observed muted colors.

For example, place content in `Scaffold` and a `LazyColumn`, then style its
existing destinations as a dock only if they fit. Respect the `innerPadding`
contract and system insets; don't apply the same inset twice.

## Keep Android behavior

Preserve system back and the project's predictive-back support, IME handling,
state restoration, TalkBack, and native switches/dialogs where appropriate.
Custom drawing is for decoration; retain semantic controls for actions. Allow
font scaling and reflow, use 48dp minimum touch targets, and keep the final list
row reachable above navigation.

## Finish

Run the relevant existing Gradle build and checks when permitted. With device or
emulator access, inspect both themes, large fonts, IME-open forms, and back behavior.
Report compiled results separately from actual device interaction and visual review.
