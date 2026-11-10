# SwiftUI implementation notes

This is an authored iOS adaptation. No iOS package, screenshot, or runtime was
inspected. Use APIs supported by the project's deployment target.

## Theme and type

Prefer semantic dynamic colors in the asset catalog or the project's existing
theme model. Map light/dark canvas, surface, raised, foreground, secondary text,
primary action, and dock roles independently. Apply the user's appearance choice
through the existing root appearance model; don't force a scheme per row.

A custom font needs Dynamic Type scaling. For example:

```swift
Text(title)
    .font(.custom("BrandDisplay-Bold", size: 32, relativeTo: .largeTitle))
    .fixedSize(horizontal: false, vertical: true)
```

`BrandDisplay-Bold` is illustrative, not a supplied font. Replace it with an
actual registered and licensed font face or the existing system typography.
Use `@ScaledMetric` for geometry that should grow with text. Do not depend on
`minimumScaleFactor` to fit primary copy into a fixed screenshot composition.

For observed color values and accessibility improvements, read `design-system.md`.
The source muted color on light panels needs a darker adaptation for ordinary
body text. Do not infer that an observed screenshot is an accessibility standard.

## Content-sized components

Use `Button` and a `ButtonStyle` for pills rather than a gesture on a decorative
shape. Keep a minimum 44pt target and sufficient content padding; allow height
to grow with multiline labels. Use `contentShape` where it improves hit testing,
and preserve native keyboard/assistive activation. Loading disables repeat
submissions and communicates state without making the action disappear.

Use rounded panels as meaningful groups and calm grouped rows for settings.
`Toggle`, `Picker`, `TextField`, and native sheets keep expected interaction
semantics. A custom appearance selector should expose selection and fit large
text; it may become a vertical picker if the horizontal version no longer fits.

Decorative rotation and overlap belong in a limited feature area. Keep backing
shapes `allowsHitTesting(false)` and `accessibilityHidden(true)`. Do not rotate
long utility labels or rely on a drawn control with no accessibility action.

## Layout and navigation

Use `NavigationStack` and destination identity already established by the app.
Keep the standard back button/interactive pop gesture unless a real requirement
justifies a custom replacement. Prefer the existing `TabView` where it meets the
brief. A custom dock should preserve destination state and semantic selection.

A bottom dock can reserve layout space using:

```swift
ScrollView {
    screenContent
}
.safeAreaInset(edge: .bottom, spacing: 0) {
    destinationDock
        .padding(.horizontal, 16)
        .padding(.vertical, 8)
}
```

This fragment assumes real views in scope. Inspect the resulting safe area and
scroll affordances; don't also reserve an unrelated fixed dock height in content.
Avoid `ignoresSafeArea` on interactive content. Background decoration may extend
under system areas while labels and controls remain clear.

At accessibility Dynamic Type sizes, allow stat pairs and horizontal rows to
stack. Use the platform's dynamic type environment to choose an appropriate
layout. A compact icon dock may need a conventional labeled treatment. All
destinations retain labels and selected traits regardless of visible text.

## Forms and accessibility

Use `.textContentType(.emailAddress)` and the appropriate keyboard for email,
and `.textContentType(.oneTimeCode)` for an OTP input. Handle paste and deletion
without turning each digit into a separate VoiceOver focus trap. Use
`@FocusState` for purposeful focus management. Avoid forcing focus repeatedly
when the user dismisses the keyboard.

Keep the focused field and submit action visible with keyboard and scrolling.
Give meaningful accessible labels, values, and hints; do not redundantly announce
the same icon and label twice. Use selected traits for navigation/choices and
expanded state for FAQs. Preserve reading order when visual elements overlap.

## Motion and verification

Read `accessibilityReduceMotion` from the environment. Prefer an instantaneous
or opacity-based state change when positional movement is reduced. Use animation
to explain selection or transition, not to delay access to content. No source
animation timing was measured, and the suggested timings are not iOS findings.

Build with the documented Xcode target and deployment configuration. Runtime
review should cover themes, Dynamic Type, VoiceOver, keyboard, safe areas,
interactive back, and destination state. State clearly when only compilation or
a preview was checked; neither establishes physical-device behavior.
