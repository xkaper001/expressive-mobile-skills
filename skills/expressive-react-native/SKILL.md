---
name: expressive-react-native
description: Builds expressive mobile UI in React Native and Expo with semantic themes, rounded components, clear actions, and accessible navigation. Use when implementing or refining React Native or Expo screens for Android, iOS, or both.
license: MIT
---

# Expressive React Native

Work within the existing React Native or Expo project. The reference app ships
React Native, Expo, and Hermes, but its original source was not recovered.

## Read and scope

Read [the design reference](references/design-system.md) and
[React Native guidance](references/react-native.md). Each is bundled here, so
this skill works without another installed skill.

Inspect package versions, navigation, theme, safe-area handling, and state
management. Preserve Expo Router or React Navigation if already in use. Do not
introduce Expo, NativeWind, Reanimated, or a new state library just for visual styling.

## Build

- Use semantic palette roles that resolve from the app's appearance preference.
- Use weighted, scalable type and deliberate neutral-to-accent balance.
- Make shared controls where repetition exists; keep the core task obvious.
- Keep `Pressable` feedback, focus, disabled/loading states, and native semantics.
- Use layout measurement and safe-area insets rather than absolute device pixels.
- Preserve deep links, back behavior, route state, and keyboard interactions.

For example, a task screen can use a neutral introductory panel, one saturated
feature panel, and a primary pill. A settings screen uses calm grouped rows and
native switches. Neither needs the source app's mascot or copy.

For a custom dock, preserve the router's navigation events and selected state.
Use labels for assistive technology on inactive destinations. At large font sizes
or long translations, prefer a layout that can display labels without clipping.

## Verify and report

Use the project's existing lint, type, and build commands when permitted. Inspect
the actual screen on the requested platforms when runtime access is available.
Check appearance changes, large text, forms with the keyboard, scroll clearance,
and screen-reader semantics. State what was built versus actually exercised.
Do not report SDK behavior or original motion timings from a screenshot.
