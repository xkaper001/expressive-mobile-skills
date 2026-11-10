---
name: expressive-flutter
description: Builds expressive Flutter mobile interfaces with warm light and dark themes, bold typography, clear actions, and accessible custom components. Use when implementing or refining Flutter UI for Android, iOS, or both; it does not require native Compose or SwiftUI companion skills.
license: MIT
---

# Expressive Flutter

Build in the existing Flutter app. Keep its router, state management, dependency
choices, and product scope unless the user asks to change them.

## Read and choose

Read [the design reference](references/design-system.md) for the visual language,
including evidence limits and accessible color adaptations. Read
[Flutter implementation guidance](references/flutter.md) before implementation.
This skill is complete when installed alone; shared design discovery is optional.

Inspect `pubspec.yaml`, theme setup, screen structure, and SDK constraints. Infer
Android/iOS targets from the project. Ask only if a missing decision materially
changes the work. Do not add Riverpod, Bloc, GoRouter, or a new component package
merely because the screen is being redesigned.

## Implement

1. Map semantic roles into `ThemeData` and a small `ThemeExtension` where needed.
2. Establish the real screen's hierarchy and one main action before decoration.
3. Use large neutral panels, weighted type, and saturated feature areas selectively.
4. Give custom controls proper focus, semantics, hit targets, and state feedback.
5. Keep Android and iOS system navigation, keyboard, and safe-area behavior intact.

Use layout constraints and scrollable content instead of fixed screenshot
coordinates. A 1080px image is not a 1080dp screen. Let text scale and controls
grow. Resolve platform differences intentionally; an app-wide Material scaffold
does not require every control to look stock, and a custom dock must still work
with accessibility, restoration, and native back behavior.

For example: a `CustomScrollView` contains a neutral introduction panel and a
colored main feature; `Scaffold.bottomNavigationBar` contains the app's existing
destinations in a styled dock, with a `SafeArea` handling the bottom inset.

## Finish

Run the project's relevant format, analysis, and build checks when permitted.
If runtime tools are available, inspect both themes, large text, keyboard-open
forms, last-row clearance, and TalkBack/VoiceOver labels. Respect explicit user
limits on testing. Report precisely which checks ran and which device behavior
remains unverified. Never claim the reference app was built with Flutter.
