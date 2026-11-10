# Repository Rules

This repository is a public collection of reusable AI agent skills. Keep the structure predictable and low-friction for people arriving from search, GitHub links, or hosted Claude upload flows.

## Skill Organization

- Every skill lives in exactly one folder under `skills/<skill-name>/`.
- Each skill folder is the landing page for that skill and must include a `README.md`.
- Each skill folder must include the source `SKILL.md` unless it is explicitly documentation-only.
- Any installable artifacts for a skill, such as `.skill` files, belong inside `skills/<skill-name>/package/`.
- Packaged `.skill` files must use the standard format: a zip archive renamed with the `.skill` extension. Do not create plain-text `.skill` files.
- Do not put skill-specific install artifacts in a repo-level `packages/` folder. That separates the download from the skill explanation and creates a confusing user journey.
- Do not split one skill across multiple sibling folders unless one folder is explicitly a separate skill with a separate audience.

## Licensing

- Skill text (`SKILL.md`, reference files, READMEs, worked examples) is CC BY-SA 4.0 (`LICENSE`). Code (script files and code blocks in Markdown) is MIT (`LICENSE-MIT`).
- Every skill folder has a `LICENSE.txt` with the copyright line, the CC BY-SA terms, a credit line and any third-party notices. Include it in the `.skill` package.
- Set `license:` in the `SKILL.md` frontmatter: `CC-BY-SA-4.0`, or `CC-BY-SA-4.0 AND MIT` when the skill ships scripts or substantial code.
- When a skill uses third-party material, credit it in the skill's README `## Attribution` and copy its licence notice into `LICENSE.txt`. Material under CC BY-SA, MIT or another CC BY-SA-compatible licence is fine. Do not copy text under a NonCommercial, NoDerivatives or unknown licence; paraphrase and link instead.

## Root README

- Keep the root `README.md` focused on the repo's purpose and a catalog of available skills.
- Do not turn the root README into the install guide for one specific skill.
- Link each catalog entry to that skill's folder.
- Installation details belong in the skill folder's `README.md`.

## Skill Landing Pages

Each `skills/<skill-name>/README.md` should answer, near the top:

- What is this skill?
- Who is it for?
- What file do I install or upload?
- Where do I install or upload it?
- What is source versus packaged artifact?
- Who should be credited?

For hosted Claude organization skills, the landing page should make the `.skill` upload path obvious before explaining implementation details.

## Versioning

Every skill has its own semantic version. Repo-level files (`README.md`, `AGENTS.md`, `docs/`) are not versioned.

### Where the version lives

- The current version is in the `SKILL.md` frontmatter as `metadata.version`, always quoted:

  ```yaml
  metadata:
    version: "1.2.0"
  ```

  Never use a top-level `version` key. The Agent Skills spec does not define one, and strict validators such as the hosted Claude upload reject unknown keys.
- The released version is the newest tag for the skill: `git tag -l '<skill-name>-v*' --sort=-v:refname | head -1`.

### When to bump

- Bump when anything the agent loads changes: `SKILL.md` (body or frontmatter) or any file in `references/`, `reference/`, `scripts/` or `assets/`. Every file in those folders counts, including a `README.md` inside them.
- Do not bump for a change to the skill's `README.md` alone, or for repo-level files.
- Bump only the skills that changed. When one commit changes several skills, each one gets its own bump, changelog entry, package rebuild and tag.

### Picking the number

1. Read `metadata.version` and the newest tag for the skill.
2. **Version equals the newest tag:** the change is new work. Bump from that version:
   - **major** (`1.2.3` → `2.0.0`): behaviour users rely on changes or disappears, such as a removed mode, a changed output format or a rule that now gives the opposite result.
   - **minor** (`1.2.3` → `1.3.0`): something new is added and existing behaviour stays, such as a new rule, mode, check or reference file.
   - **patch** (`1.2.3` → `1.2.4`): fixes, wording, examples and typos.

   A minor bump resets patch to 0. A major bump resets minor and patch to 0.
3. **Version is higher than the newest tag:** an earlier, unpushed commit already bumped it. Do not bump again. Add the change to that version's changelog entry. Raise the number only if the new change needs a higher level, for example a pending `1.2.4` plus a new rule becomes `1.3.0`, and rename the changelog entry to match.
4. **Version is lower than the newest tag, or an existing skill has no tag:** stop and ask the maintainer.
5. **New skill:** start at `metadata.version: "1.0.0"`, add a `- **1.0.0:** First release.` changelog entry, and tag it like any other release.
6. Keep any suffix and bump the numbers in front of it: `0.3.0-ms` becomes `0.3.1-ms` or `0.4.0-ms`.

### Changelog

- Add the entry at the top of `## Changelog` in the skill's `README.md`, in the same commit as the bump. If the section is missing, add it just before `## Attribution`.
- Format: `- **1.3.0:** What changed, written for someone who uses the skill.` One entry per version, newest first.

### Package

Rebuild `package/<skill-name>.skill` in every commit that changes a packaged file, whether or not that commit bumps the version (see case 3 above).

- Include every file the agent loads, including files added in this change. Do not rebuild from the old zip's file list alone, or new files will be missing.
- Keep the existing layout. Check it with `unzip -Z1 package/<skill-name>.skill`: some packages prefix every path with `<skill-name>/`, some don't, and not all of them include `README.md`.
- Never put `package/` inside the package.
- Verify before committing: `unzip -t` passes, the packaged `SKILL.md` shows the new `metadata.version`, and every packaged file is identical to its source (`cmp`).
- A README-only change needs no bump, but rebuild the package if it contains `README.md`.

### Commit, tag and push

- Name the skill and version in the commit message, for example `feat(danisher): add range rules (v1.3.0)`. When one commit changes several skills, name each: `fix: typo in englisher (v1.0.1), new reference in danisher (v1.3.0)`.
- A release happens when the change is pushed to `main`. Tag the last commit that changes the skill: `git tag -a <skill-name>-v<version> -m "<skill-name> <version>"`.
- Check first that the tag doesn't exist: `git tag -l <skill-name>-v<version>`.
- Push `main` first, then each tag by name: `git push origin <skill-name>-v<version>`.
- Never move, delete or reuse a pushed tag. If a release turns out to be wrong, fix it with a new patch version.
