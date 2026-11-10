#!/bin/sh
# Run from a terminal with working GitHub connectivity and an authenticated gh CLI.
# Publishes only this authored repository, never the sibling research material.
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(dirname "$script_dir")
cd "$repo_dir"

python3 scripts/validate.py
gh auth status
account=$(gh api user --jq .login)
if [ "$account" != "xkaper001" ]; then
  printf '%s\n' "Expected GitHub account xkaper001; active account is $account. No publication performed." >&2
  exit 1
fi
destination="$account/expressive-mobile-skills"

if [ ! -d .git ]; then
  git init -b main
fi
if [ "$(git rev-parse --show-toplevel)" != "$repo_dir" ]; then
  printf '%s\n' 'Refusing to publish from a different repository root.' >&2
  exit 1
fi
if [ "$(git branch --show-current)" != main ]; then
  printf '%s\n' 'Expected the main branch; no publication performed.' >&2
  exit 1
fi

# Explicit paths: do not stage local research inputs from the parent workspace.
git add -- .gitignore LICENSE README.md docs skills scripts .github
if ! git diff --cached --quiet; then
  git commit -m 'feat: add expressive mobile design skills'
fi

if git remote get-url origin >/dev/null 2>&1; then
  origin=$(git remote get-url origin)
  case "$origin" in
    "https://github.com/$destination"|"https://github.com/$destination.git"|"git@github.com:$destination.git") ;;
    *) printf '%s\n' "Unexpected origin: $origin. No push performed." >&2; exit 1 ;;
  esac
  # Do not silently turn an existing private repository into a public one.
  visibility=$(gh repo view "$destination" --json visibility --jq .visibility)
  if [ "$visibility" != PUBLIC ]; then
    printf '%s\n' 'Destination is not public; no push performed.' >&2
    exit 1
  fi
  git push --set-upstream origin main
else
  # An existing remote repository causes create to fail; it is never overwritten.
  gh repo create "$destination" --public --source . --remote origin \
    --description 'Selective agent skills for expressive mobile design, Flutter, React Native, Compose, and SwiftUI' \
    --push
fi

gh repo view "$destination" --json url,visibility --jq '"\(.url) (\(.visibility))"'
printf '\nInstall picker:\nnpx skills add %s\n' "$destination"
