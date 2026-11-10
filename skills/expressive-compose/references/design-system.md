# Expressive mobile design reference

This is an authored design system informed by Android screenshots of Fix Yo Yap
and packaged resource inspection. **Observed** means visible in the supplied
screenshots or present in the package. **Suggested** values are starting points
for a new app, not recovered source tokens. Framework mappings are adaptations.
No source artwork or font binaries are included. Use your own product identity.

## Decide what the screen is for

Start with the user's task and real content. Name the primary action, the current
state, and what must remain visible when the keyboard or large text is active.
Use a screen's expressive budget where it supports the task: a bold feature
panel on a discovery screen, calm grouped rows on settings, a focused form for
authentication. Preserve the project's router, state model, and existing brand
unless changing them is part of the request.

For a new direction, show a useful core screen before extending the system.
For a redesign, inspect the current screen and preserve behavior that works.
Do not turn every surface into a rotated card or add a mascot because the source
app has one. Avoid source-specific copy, speech-bubble faces, and brand marks.

## Color roles

The following are **observed flat pixel colors**, with roles inferred from
the rendered screenshots. They are not recovered variable names. Gradients,
antialiasing, images, and disabled controls create additional colors.

| Role | Dark | Light |
| --- | --- | --- |
| Canvas | `#1E1A16` | `#F2ECE3` |
| Surface / grouped panel | `#2A251F` | `#E9E2D7` |
| Raised / inactive fill | `#352F28` | `#DFD7CB` |
| Main text | `#F6F1EA` | `#1B1712` |
| Muted text | `#9A9186` | `#7D7468` |
| Primary action fill | `#CCFF00` | `#CCFF00` |
| Ink on lime | `#14110E` | `#14110E` |
| Active dock fill | `#CCFF00` | `#1B1712` |
| Active dock foreground | `#14110E` | `#CCFF00` |

Feature accents observed across the screenshots:

| Blue | Pink | Orange | Lavender | Cyan |
| --- | --- | --- | --- | --- |
| `#1B88F8` | `#F1228D` | `#E28E26` | `#D79BFB` | `#32E2DE` |

**Suggested accessibility adjustment:** on the light `#E9E2D7` surface and
`#DFD7CB` raised fill, use `#62594F` for ordinary secondary text. The observed
`#7D7468` does not reach 4.5:1 on those fills. Likewise, use the dark theme's main
text for body copy on its raised fill; the observed dark muted color is marginal
there. Disabled controls can be subdued but still need a separate readable
explanation when the reason for being disabled matters.

Validate contrast for the actual pair and size. A vivid panel usually needs dark
ink, not white type. Do not assign meaning by color alone. Keep accent roles
stable across themes; use semantic error/success roles for actual status rather
than reusing a category's pink or green indiscriminately.

## Typography

**Observed:** the APK bundles Bricolage Grotesque weights 200 through 800. The
screens visually match a heavy rounded grotesque. Their exact weight and text
size mapping was not recovered.

**Suggested scale in logical units:**

| Role | Size | Weight | Line-height ratio |
| --- | --- | --- | --- |
| Display / entry title | 36–44 | 750–800, or nearest real font face | 1.05–1.15 |
| Screen title | 28–34 | 700–800 | 1.10–1.20 |
| Panel title | 22–26 | 700 | 1.15–1.25 |
| Body | 16–18 | 400–500 | 1.35–1.50 |
| Action label | 16–18 | 600–700 | 1.20–1.35 |
| Eyebrow / metadata | 11–13 | 600–700 | 1.25–1.40 |

Use the platform's text scaling. On narrow screens or at large accessibility
sizes, let headings wrap, actions grow, and labels become multiline. Never
shrink all text to fit a reference screenshot. Avoid excessive tracking on body
text; modest tracking belongs on short uppercase eyebrows. Typography should
have contrast in size and weight before it gains extra colors or decoration.

Use Bricolage Grotesque only when it fits the new brand, from an upstream source
with its license. A suitable installed or licensed font is a valid alternative.
Do not extract app-bundled fonts for distribution. Test fallback glyphs for the
actual language, not just an English sample.

## Layout and geometry

**Observed:** left-aligned text, generous gutters, broad rounded panels, pills,
circular icon buttons, a vertical scroll rhythm, and little heavy elevation.
Many screenshots use a 54px outer gutter in a 1080px-wide image. Device density
and font scale were not captured, so physical pixels are not dp/pt values.

**Suggested initial tokens:**

| Token | Starting value in dp / pt / Flutter logical px |
| --- | --- |
| Outer gutter | 20–24 |
| Panel inset | 20–24 |
| Spacing rhythm | 4, 8, 12, 16, 24, 32 |
| Panel corner radius | 28–36 |
| Icon tile corner radius | 16–20 |
| Main action minimum height | 52–56, growing with text |
| Dock outer inset | 12–16 plus system safe area |

Respect system bars, display cutouts, keyboards, and the bottom home indicator.
When a dock overlays content, reserve its actual height plus a gap in the scroll
content. A floating dock must never cover the last row or a focused field.
Constrain reading width on large displays. Reflow stat tiles and horizontal
choices when text becomes large; keep touch targets intact.

## Component recipes

### Primary action

One broad pill with a clear verb, strong label, optional trailing arrow, and
high-contrast fill. Define enabled, pressed, loading, disabled, and keyboard-
focus states. Loading keeps the action's width stable and prevents duplicate
submissions. A disabled state explains its requirement near the control when
the requirement is not obvious. At long translations, let the label wrap or
grow vertically. Reserve repeated identical actions for an established need.

### Neutral panel and grouped rows

Use a panel for a meaningful group, not a wrapper around every piece of text.
Pair a short title with an explanation or a task. In settings, related rows
share a surface with subtle dividers, a leading icon where useful, and either a
value/chevron or a native switch. The entire row can be a target, but do not nest
two independent tappable controls with ambiguous semantics. Destructive actions
need their own placement and copy, not the same lime treatment as forward progress.

### Feature panel

Use a saturated fill for a main feature or category. Put its title, short value
statement, and action in a readable hierarchy. Decorative overlap or rotation
belongs to a limited hero region with clipping and hit regions considered.
Keep actual text upright in utility screens. Do not stretch decorative cards to
hide missing content or invent a carousel interaction without a purpose.

### Choice chips and topic rows

Chips support short choices; rich rows support a title and explanation. Specify
single- versus multi-selection in behavior and accessibility semantics. Selection
uses a check, border, or label as well as fill. Preserve enough space for a
translated label. The source screenshots do not establish every selected state;
these are implementation recommendations.

### Form and verification entry

Use a persistent field label, appropriate keyboard, visible focus, inline errors,
and autofill. A segmented OTP appearance should generally be backed by one real
text input with paste, autofill, deletion, and screen-reader support. A code field
is not six unrelated focus traps. Keep the primary action reachable with the
keyboard open and preserve input after a recoverable error.

### Floating navigation

The reference shows five top-level destinations in a rounded dock. Only the active
item shows a visible text label. That styling is optional: choose the number of
destinations from the product, keep accessible labels on every item, expose selected
state, and preserve destination state and native back behavior. With long labels,
large text, or too many destinations, adapt to a conventional labeled bar, rail,
or sidebar instead of squeezing icons. In light mode, a dark active pill with lime
foreground maintains clear separation from the cream dock.

### Empty, progress, and support states

An empty state names what will appear and offers the next useful action. Do not
render fake measurements as historical data. Progress indicates real work; use an
indeterminate state when completion cannot be measured. A task list can distinguish
completed/current/pending steps with text and icons. FAQs expose expanded state
and remain readable without animation. A contact panel needs a real action wired
to the product's destination, not the source app's email address.

## Theme and motion behavior

Map roles independently for light and dark. Keep saturated feature fills where
they still pass contrast; change text and panel roles deliberately. Respect the
user's System/Light/Dark choice when those modes are in scope. If a task-specific
screen stays dark, document the reason as a product decision. The recording-dark
caption in the reference does not make that behavior mandatory for other apps.

**Motion is not measured:** no recording was supplied. As an authored starting
point, use brief feedback around 100–160ms and simple state changes around
180–260ms, tuned to native conventions. Do not claim these are the source app's
durations. Avoid perpetual bobbing, decorative progress delays, or springs on
every component. Reduced-motion users should receive the same state information
with positional motion removed or simplified. Interactive controls still need
visible press/focus feedback.

## Review the rendered result

Review a narrow phone and a larger width, both themes when supported, large text,
long labels, keyboard-open forms, empty/loading/error states, and the last scroll
row above navigation. Check screen-reader order, semantic labels, contrast, and
platform-sized targets (at least 48dp on Android, 44pt on iOS). At large text, some
components should reflow rather than preserve the source composition.

Compare hierarchy, breathing room, type weight, action prominence, and neutral-
to-accent balance. A useful adaptation should still read as the new product.
Report what was actually rendered, built, and exercised. A code snippet or build
pass alone does not verify device layout, native gestures, or accessibility.
