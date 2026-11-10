# Flutter implementation notes

These are implementation recommendations, not decompiled Flutter code. Use APIs
compatible with the project's Flutter SDK and existing architecture.

## Theme roles

Use `ThemeData`/`ColorScheme` for normal component roles and a small
`ThemeExtension` for feature accents or dock colors if needed. Supply `theme`,
`darkTheme`, and the persisted `ThemeMode` at the application boundary. For a
fixed brand palette, avoid accidental platform dynamic-color replacement.

Configure scaffold background, surface, on-surface, primary, on-primary,
typography, button shape, input fill, and switch roles explicitly. A theme
generated from one lime seed will not reproduce the observed warm neutrals.
Keep error colors independent from decorative pink and category colors.

For example, within an existing theme builder:

```dart
final colors = ColorScheme.fromSeed(
  seedColor: const Color(0xFFCCFF00),
  brightness: brightness,
).copyWith(
  primary: const Color(0xFFCCFF00),
  onPrimary: const Color(0xFF14110E),
  surface: isDark ? const Color(0xFF2A251F) : const Color(0xFFE9E2D7),
  onSurface: isDark ? const Color(0xFFF6F1EA) : const Color(0xFF1B1712),
);
```

This is a fragment; `brightness` and `isDark` belong to the existing theme builder.
Also configure the canvas and secondary text roles. Do not treat this fragment
as a complete app theme or infer a built example from its presence.

## Type and controls

Use actual bundled font faces declared in `pubspec.yaml`, or the project's
existing licensed typeface. Load Bricolage from upstream only if the brand calls
for it; don't copy extracted app fonts. Set text roles in `TextTheme`. Allow
the ambient `TextScaler`; do not replace it with `TextScaler.noScaling`.

A primary pill can use `FilledButton` with `StadiumBorder`, horizontal padding,
and a minimum rather than fixed height. Let its child contain a wrapping label
and optional icon. Native disabled/loading behavior and focus should remain clear.
Avoid `FittedBox` around essential labels to hide overflow.

Use `TextField`/`TextFormField` with labels, `AutofillHints.email`, appropriate
keyboard, validators, and inline error text. For OTP, use one backing input
with `AutofillHints.oneTimeCode`, digit formatting, paste support, and accessible
reading order. Draw cells as a presentation layer if needed.

## Screen structure

Prefer `Scaffold` + `CustomScrollView` or `ListView` for scrollable task screens.
Use `LayoutBuilder` to reflow rather than copying screenshot pixels. Wide layouts
can center a constrained reading column, with navigation adapting to the app.

Place a custom dock in `bottomNavigationBar` so body layout accounts for its
height, then give it bottom safe-area padding. If it deliberately overlays the
body with `extendBody`, reserve the actual dock extent in the scroll content.
Do not add both strategies' padding without checking the result.

Keep `resizeToAvoidBottomInset` consistent with the form architecture. A form
must still scroll when `MediaQuery.viewInsetsOf(context).bottom` grows. Use
`SafeArea` for system obstruction, not as a substitute for keyboard handling.

For a rotated feature stack, put the decorative backing cards in `IgnorePointer`
and `ExcludeSemantics`. Keep a clear semantic action on the foreground card.
Use clipping boundaries deliberately; avoid cutting off focus and touch regions.

## Navigation and platform behavior

Preserve the existing route model. Use stable destination identity and state
restoration; an `IndexedStack` may help a simple shell, while a routed shell
should retain its router's state model. A navigation bar must not create new
copies of its root screen on each tap. Inactive icon-only destinations still
need names and selected state in `Semantics`.

Honor Android's `PopScope`/router back model and iOS swipe-back where the app
supports them. Don't consume every back event to keep a custom screen visible.
Use platform-appropriate text editing, switches, permissions, and presentation
where these affect user expectations. Target minimum hit areas of 48 logical
pixels on Android and 44 on iOS, with larger content-driven bounds as needed.

## Motion and review

Use small implicit state transitions where they clarify selection or completion.
Check `MediaQuery.disableAnimationsOf(context)` and simplify motion. Animations
must not own business state or block a user's next action. Progress reflects real
work; do not animate fake personalization delays.

Check narrow screens, both themes, large text, long translations, empty and error
states, keyboard forms, TalkBack/VoiceOver order, and the last row above the dock.
Use the repo's formatter/analyzer/build commands. A passing analyzer is not
evidence of an Android or iOS device render.
