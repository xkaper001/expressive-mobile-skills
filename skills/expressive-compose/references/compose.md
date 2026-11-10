# Jetpack Compose implementation notes

This is a native Android interpretation of a visual language observed in a
React Native app. Match APIs to the project's Compose BOM and minimum SDK.

## Theme roles

Build `lightColorScheme` and `darkColorScheme` around semantic roles, then use
`MaterialTheme` for type, shape, and components. If the app intentionally uses
dynamic color, reconcile the brief with that behavior rather than silently
turning it off. A fixed reference-inspired palette should not be accidentally
overridden by a wallpaper palette.

For example, a dark palette can start with:

```kotlin
private val ExpressiveDark = darkColorScheme(
    primary = Color(0xFFCCFF00),
    onPrimary = Color(0xFF14110E),
    background = Color(0xFF1E1A16),
    onBackground = Color(0xFFF6F1EA),
    surface = Color(0xFF2A251F),
    onSurface = Color(0xFFF6F1EA),
    onSurfaceVariant = Color(0xFF9A9186),
)
```

This is a theme fragment, not the source app's palette code. Review all actually
used Material roles, especially variant/disabled colors and tonal elevation.
An explicit fixed surface may be appropriate for a neutral panel; otherwise
Material elevation can tint it away from the intended fill.

Use a small theme-local extension for feature accents and special dock roles
only when needed. The light dock's active state is dark with lime foreground;
it is not the same fill as a normal light-theme primary button.

## Typography and sizing

Supply a real `FontFamily` when a custom family is in scope, with accurate weight
mapping and licensed upstream font files. Use `sp` through `TextStyle`, not dp
converted to text size. Avoid disabling font scaling or capping all headings.
Let `Text` wrap, and avoid `maxLines = 1` for essential long labels.

Use `heightIn(min = 56.dp)` and content padding on a primary `Button` instead
of a fixed height. Use a fully rounded shape for actions and a 28–36dp starting
radius for panels, adapted to content. Keep at least 48dp interactive targets.

## Screen and insets

Use `Scaffold` with explicit understanding of its `contentWindowInsets` and
`innerPadding`. A `LazyColumn` can receive that padding as content padding. Do
not also add `statusBarsPadding` and bottom navigation padding for the same
insets unless the layout contract requires it. Account for edge-to-edge rendering
with the app's target SDK and window setup.

Use `imePadding` where the form must avoid the IME, and verify how it combines
with scaffold and system bar insets. Ensure the focused field and submit action
remain reachable on smaller phones. Reflow stat pairs at large font sizes;
don't require two columns at every width.

Put backing decorative cards in non-clickable layout nodes. `graphicsLayer`
rotation can create the hero effect, but focus, clipping, and visible hit regions
still need review. Do not implement essential text or controls solely in `Canvas`.

## Semantics, navigation, and state

Use `Button`, `IconButton`, `Switch`, `selectable`, or `toggleable` as appropriate.
Provide useful descriptions for action icons and null descriptions for purely
decorative icons. Merge row semantics intentionally. A switch with a row click
should expose one clear semantic action rather than two conflicting actions.

Keep selection single-source: remember/restore local presentation state with
`rememberSaveable` where appropriate, while durable state belongs to the existing
state holder/ViewModel. A custom dock should retain the Navigation component's
top-level destination behavior, back stack, save/restore handling, and deep links.
Expose selected semantics and accessible labels for icon-only destinations.

Honor system back and predictive back where supported by the existing stack.
The source config disables predictive back, but that is not a recommendation to
disable it in a new native app.

For OTP, keep a real text input for keyboard, autofill, paste, and deletion. Draw
segmented cells around that state if desired. Avoid six independent input nodes
that create focus traps or read in an unintelligible order.

## Motion and review

Use Compose motion APIs for meaningful state changes. Follow system animation
settings and avoid replacing duration scaling with an unconditional custom loop.
Keep information present when animation is disabled. For unmeasurable work, show
an indeterminate state rather than fabricated completion percentages.

Run the existing Gradle checks/build. Device review should cover target SDK
edge-to-edge behavior, large fonts, TalkBack, IME, back, both themes, and the last
list item. Compilation alone does not verify any of those interactions.
