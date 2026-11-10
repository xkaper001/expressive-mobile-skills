# React Native and Expo implementation notes

The reference APK includes React Native, Expo SDK 54, and Hermes. That observation
does not require using those same versions or imply recovery of its source.
Work with the destination project's supported versions.

## Theme and typography

Resolve a semantic palette from the app's System/Light/Dark preference and
`useColorScheme`. Persist the preference in the existing settings layer. Keep
canvas, surface, raised, text, secondary text, primary action, and dock roles
separate; don't scatter hex colors through individual screens.

Use normal `Text` with scaling enabled. Load real font faces via the project's
font setup (`expo-font` when already appropriate). Map font family names and
weights to the actual faces; the same family/weight combination may resolve
differently between Android and iOS. Don't cap accessibility scaling simply to
fit an oversized heading. Let narrow layouts and long labels wrap.

## Accessible actions

A pill can be built on `Pressable`; retain a distinct pressed state, minimum
touch area, accessible button role, and disabled/busy semantics. For example:

```tsx
<Pressable
  accessibilityRole="button"
  accessibilityState={{ disabled, busy }}
  disabled={disabled || busy}
  onPress={onPress}
  style={({ pressed }) => [
    styles.action,
    { backgroundColor: palette.primary },
    pressed && styles.pressed,
    (disabled || busy) && styles.unavailable,
  ]}
>
  <Text style={[styles.actionLabel, { color: palette.onPrimary }]}>
    {busy ? 'Saving…' : 'Save changes'}
  </Text>
</Pressable>
```

This illustrative fragment assumes existing state, styles, and palette. Use a
minimum height and padding, not a fixed height that clips scaled text. Announce
completion/errors through appropriate live regions or platform announcements;
changing only a spinner is insufficient when it conveys necessary state.

## Insets and scrolling

Reuse the project's safe-area provider, commonly `react-native-safe-area-context`.
Do not rely on the core `SafeAreaView` as a universal Android inset solution.
Choose whether the router's tab bar consumes layout space or overlays it, then
apply bottom content padding once. For custom overlays, measure the dock height
and include bottom insets rather than hardcoding one phone's values.

Use `ScrollView` for bounded content and `FlatList`/`SectionList` for longer data.
Avoid nested vertical scrolling for a single screen. With keyboard forms, adapt
`KeyboardAvoidingView`, scroll insets, and Android window behavior to the existing
app; check both platforms rather than prescribing one `behavior` blindly.

Decorative tilted cards can use transforms. Keep backing shapes inaccessible and
non-interactive, and give foreground actions real hit regions. A visually rotated
card's bounds and overflow can differ from its layout box.

## Navigation

Preserve Expo Router or React Navigation, including emitted tab-press events,
prevented navigation, long-press behavior when used, accessibility selected state,
and deep links. Don't replace the navigator with a hand-managed page index just
to style the tab bar. Match route identity, avoid duplicate roots, preserve state
on destination changes, and keep Android back/iOS swipe behavior.

Icon-only inactive destinations need accessible labels. Switch to a labeled or
reflowed treatment when long labels or large text do not fit the dock. Never
disable text scaling on navigation labels as the only overflow fix.

## Forms and state

Use native `TextInput` behavior with appropriate `keyboardType`, autocomplete,
and platform `textContentType`. Handle autofill, paste, selection, deletion, and
IME composition. Segmented OTP presentation should keep a single input model
unless there's a tested accessible reason to split it.

Model loading and validation explicitly. Preserve input on recoverable failures,
prevent duplicate submissions, and clear error text when appropriate. A selected
topic row needs a check or border plus semantic state, not only an accent fill.

## Motion and verification

Use the animation stack already present. If Reanimated is installed, it can drive
necessary gesture-linked motion; its presence does not justify adding motion to
every card. Honor Reduce Motion via the project's accessibility layer, with
`AccessibilityInfo` or compatible animation APIs. Do not claim measured timings.

Use existing lint/type/build scripts. Review both requested platforms when
available, including font loading, keyboard behavior, safe areas, theme changes,
large text, screen-reader focus, and bottom-content reachability. If only Metro
or a web render was checked, report that limitation explicitly.
