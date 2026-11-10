# Expressive Mobile Skills

Agent skills for building mobile interfaces with warm surfaces, assertive typography,
clear actions, playful feature panels, and deliberate light and dark themes.

Developed from static inspection of Fix Yo Yap's Android package and study of 18
user-provided screenshots. The guidance extracts reusable design decisions and
adapts them to each framework. It does not reproduce the app or supply its code,
branding, assets, or backend.

## Install only what you need

Use the [Skills CLI](https://github.com/vercel-labs/skills) from your project:

```sh
npx skills add xkaper001/expressive-mobile-skills
```

The interactive installer lets you choose the skills, coding agents, and scope.
Use Space to select items where the CLI presents a multiselect. Add `-g` if you
want a user-level installation across projects.

| Skill | Choose it for |
| --- | --- |
| `expressive-mobile-design` | Framework-independent visual direction, screen design, and design review |
| `expressive-flutter` | Flutter interfaces for Android and iOS |
| `expressive-react-native` | React Native or Expo interfaces for Android and iOS |
| `expressive-compose` | Native Android interfaces in Kotlin and Jetpack Compose |
| `expressive-swiftui` | Native iPhone interfaces in SwiftUI |

**For Flutter on both phones, install `expressive-flutter`.** You do not need
Compose or SwiftUI skills just because your Flutter app targets those platforms.
Each implementation skill includes its own design reference; the shared design
skill is optional when you also want dedicated design exploration and critique.

```sh
# Browse without installing
npx skills add xkaper001/expressive-mobile-skills --list

# One framework, one agent
npx skills add xkaper001/expressive-mobile-skills --skill expressive-flutter -a codex

# Design work plus native Android implementation
npx skills add xkaper001/expressive-mobile-skills \
  --skill expressive-mobile-design --skill expressive-compose
```

There is no automatic dependency installation or bundled app runtime. These are
portable `SKILL.md` instructions and supporting Markdown references.

## Try it

```text
Use expressive-flutter to design and build the main screen of a language
practice app. Keep the existing router and state management. Use a warm light
theme and a dark theme, a single strong practice action, and accessible text.
```

```text
Use expressive-mobile-design to review this onboarding flow. Preserve the
product's identity. Explain the hierarchy and propose concrete changes before
implementing them.
```

```text
Use expressive-swiftui to build a settings screen with grouped rows and an
appearance selector. Preserve Dynamic Type and standard back navigation.
```

The skills infer the stack from the existing project before asking questions.
They preserve product scope and adapt the visual language to the brief. Bright
cards, a mascot, and a floating dock are choices, not requirements for every app.

## What is supported by evidence?

The reference app is React Native + Expo, with Hermes bytecode. The screenshots
show Android screens. Flutter, Compose, and SwiftUI guidance is an authored
translation of the visual principles, not recovered implementation code.
Motion timings, exact logical dimensions, recording screens, and iPhone behavior
were not verified. See [the analysis](docs/reference-analysis.md) and
[the design system](docs/design-system.md).

## Maintain the collection

```sh
python3 scripts/sync-design-reference.py
python3 scripts/validate.py
```

The sync command copies the canonical design reference into each skill so each
remains complete when installed alone. Validation checks discovery metadata,
reference isolation, the public file allowlist, synchronized copies, and the
contrast of the recommended foreground/background pairs. It does not build apps.

For a local installation before publishing:

```sh
npx skills add . --list
npx skills add . --skill expressive-flutter -a codex
```

To publish this authored checkout to the maintainer's GitHub account, authenticate
with `gh auth login -h github.com` if necessary, then run:

```sh
sh scripts/publish.sh
```

The script validates the public files, checks the active account, creates the
public `expressive-mobile-skills` repository, and pushes `main`. It will not
overwrite an unrelated repository, force-push, or change a private repo's visibility.

## Attribution and license

Independent study inspired by [Fix Yo Yap](https://fixyoyap.com). No affiliation
or endorsement is implied. The MIT license applies to the original guidance in
this repository. No APKs, extracted fonts, app artwork, user screenshots, or
decompiled code are distributed. Source materials retain their owners' rights.
