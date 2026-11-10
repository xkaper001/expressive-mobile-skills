---
name: expressive-swiftui
description: Builds expressive native iPhone interfaces in SwiftUI with warm semantic themes, bold scalable typography, rounded components, and accessible actions. Use for native SwiftUI screen implementation or refinement, rather than Flutter or React Native projects.
license: MIT
---

# Expressive SwiftUI

Translate the visual principles to an iPhone app while preserving native behavior.
This is an authored platform adaptation. The reference evidence is Android only;
no original iOS app behavior or SwiftUI implementation was inspected.

## Read and scope

Read [the design reference](references/design-system.md) and
[SwiftUI implementation guidance](references/swiftui.md). This skill includes
its own visual guidance and has no required sibling dependency.

Inspect the app's deployment target, appearance model, navigation, component
library, and state ownership. Keep those decisions unless changing them is part
of the request. Do not force the latest iOS visual treatment onto an older target.

## Implement

- Map colors by semantic role using dynamic asset colors or the existing theme.
- Use custom typography only with Dynamic Type scaling and suitable fallback.
- Give content a clear hierarchy and use vivid panels selectively.
- Build actions with `Button`, inputs with real text controls, and selection with
  semantic state. Preserve focus, accessibility actions, and native feedback.
- Respect safe areas, keyboards, navigation gestures, and system sheets.

For example, a `ScrollView` can contain a neutral summary panel, one expressive
feature panel, and grouped rows. Use `safeAreaInset(edge: .bottom)` for a dock
when custom navigation is justified, or preserve the existing `TabView` when it
better serves the product. Do not place essential controls behind the home indicator.

At accessibility text sizes, let rows stack and titles wrap. Offer a standard
labeled navigation treatment if a compact dock cannot fit. Keep VoiceOver labels
and selected traits on every destination even when only one visible label appears.

## Finish

Run the documented Xcode build/checks when permitted. If simulator or device
access is available, inspect light/dark, Dynamic Type, keyboard-open forms,
VoiceOver semantics, and interactive back behavior. Report which were exercised.
Do not present suggested timings or layouts as measurements of the source iOS app.
