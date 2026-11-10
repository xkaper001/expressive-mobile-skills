# Reference analysis and evidence boundaries

## Source material

The supplied Android package identifies **Fix Yo Yap 2.1.0**, package
`com.eightxsocial.yap`. Static resource inspection establishes React Native,
Expo SDK 54, and Hermes bytecode, rather than Flutter. No application was
executed during this study.

| Observation | Evidence | What it establishes |
| --- | --- | --- |
| Expo SDK 54 and app version 2.1.0 | `base.apk` → `assets/app.config` | Packaged configuration, not the running OTA update |
| React Native and Hermes | `assets/index.android.bundle` bytecode header; ARM64 split libraries `libreactnative.so`, `libhermes.so`, `libexpo-modules-core.so` | Shipped framework/runtime components |
| Bricolage Grotesque weights 200–800 | Named `.ttf` resources under `res/raw/` | Available font files; the visual family match is a strong inference, not a recovered text-style mapping |
| Warm splash surface | `app.config` → splash background `#1E1A16` | Configured splash color |
| Light and dark UI variants | Supplied Android screenshot pairs | Rendered appearance at the captured states |

Base APK SHA-256:
`1531e7ff879a04f4b154c9a4422f03d1c590abe087658713f446185e407309db`.

REA archive inspection parent Evidence:
`ev_cb316863cb817b5898cb9b27263d2cb368514b86a417f6a7239c101a33664961`.
REA archive inventory Evidence:
`ev_759b5cf092795804ac6986740b0da97db357e2ff781f3c50e0dc01102a58047b`.
These IDs identify the original analysis session; they are not public fetch URLs.
The archive tool inventories entries and hashes. It does not establish UI behavior
or decompile Hermes. The Android JADX tool was unavailable because its caller-
supplied JAR was not configured; no Java decompilation result is claimed.

## Screenshot coverage

Eighteen PNGs, each 1080 × 2400 physical pixels, were inspected visually. Solid
colors were also counted directly from decoded pixels. The original images remain
local and are not part of this distribution.

| Capture suffix | Captured state | Reusable lesson |
| --- | --- | --- |
| `153115` | Entry screen | Oversized diagonal ribbons can carry a brand moment above a plain primary action |
| `153120`, `153124` | Email entry with and without keyboard | Clear field label, large field, explicit disabled action, keyboard-aware composition |
| `153224` | Six-digit verification entry | Strong focus treatment and separate resend/change-address actions |
| `153257` | Onboarding name and goal | Optional input is labeled; choice chips keep the task concrete |
| `153310` | Topic selection | Whole-row choice cards pair a colored icon tile with concise explanation |
| `153323` | Personalization loading snapshot | A task list communicates completed/current/pending work |
| `153335`, `153422` | Home, dark/light | Quiet onboarding panel plus one expressive card stack and a clear main action |
| `153338`, `153425` | Competition, dark/light | A colored feature panel separates a live action from a secondary code flow |
| `153341` | Empty history | Empty state explains the next action; muted chart placeholders do not invent measurements |
| `153344` | Leaderboard | Rank, identity, badge, and right-aligned score form an efficient row hierarchy |
| `153347`, `153415`, `153431` | Profile, dark/light | Statistics, promotion, and grouped utility rows have different emphasis |
| `153358` | Settings | Segmented appearance choice, switches, grouped legal/help rows |
| `153440` | Support, light | A contact panel and readable expandable FAQs share the same surface language |

The suffixes refer to `Screenshot_20261110-<suffix>.png`. Two light profile
captures are nearly identical; they are not evidence for extra screens.
Capture order suggests a walkthrough, but screenshots alone do not prove the
transition graph or what was tapped between them.

## Design findings

### Typography does most of the work

Large, heavy, rounded headings contrast with small uppercase section labels and
muted explanatory text. Headings sometimes split into a foreground line and a
muted line. The content remains left aligned and direct. Secondary text is used
heavily; its contrast should be improved where a new product's use case needs it.

### Neutral surfaces make the accents useful

Most screens use a warm brown or cream canvas. Neutral raised panels contain
routine work. Lime highlights primary actions and selected controls. Blue, pink,
orange, lavender, and cyan distinguish featured panels and icon families. The
home screen is unusually colorful; settings and support are much quieter.

### Shape and spacing establish hierarchy

Large rounded panels, fully rounded actions, circular icon controls, and grouped
rows recur. Panel fill and generous gaps usually separate content without strong
borders or shadows. The home feature stack uses visible offset and rotation;
utility rows stay aligned. The outer gutter is roughly 54 physical pixels in many
captures, or 5% of image width. This is a ratio observation, not a recovered dp value.

### Navigation carries state explicitly

Five main destinations share a floating rounded dock. The active destination
expands into an icon-and-label pill; inactive destinations show icons. Dark mode
uses lime fill and dark foreground for the active pill. Light mode uses dark fill
and lime foreground. The dock consumes space and can obscure nearby content if
implemented without sufficient scroll padding. At large type sizes, a standard
labeled navigation treatment can be more usable than the compact reference.

### Light mode is designed, not inverted

The canvas, panels, raised surfaces, text, and selected dock are remapped by role.
Blue, pink, orange, lavender, cyan, and lime keep their visual identity. The
profile and competition pairs demonstrate this clearly. A settings caption says
recording stays dark; that is observed copy, not a verified recording screen.

### Feedback can be specific without being noisy

Disabled actions, OTP focus, onboarding segments, a loading task list, progress
tracks, and an expanded FAQ are visible. Their animation timing and interaction
implementation are unknown. New implementations should use actual state changes,
not fake progress or artificial loading delays.

## Extraction into skills

The shared design system records observed colors and patterns. Logical dimensions,
type sizes, motion ranges, accessibility improvements, and platform mappings are
explicitly authored recommendations. They can be adapted to a new product's
identity; the goal is reusable judgment rather than a screenshot clone.

The implementation skills translate that guidance to Flutter, React Native,
Jetpack Compose, and SwiftUI. The app's original source, component tree, router
behavior, accessibility tree, exact spacing tokens, backend, scoring, subscriptions,
and runtime performance have not been reconstructed.
