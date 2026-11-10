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

Every skill is versioned on its own with semantic versioning.

- Store the version in the `SKILL.md` frontmatter as `metadata.version`, quoted: `metadata:` then `  version: "1.2.0"`. Do not use a top-level `version` key; the Agent Skills spec does not define one, and strict validators reject unknown keys.
- Bump the version in the same commit as any change to a skill's `SKILL.md` or bundled files. Use major for changed or removed behaviour that users rely on, minor for new rules or modes, and patch for fixes and wording.
- Add an entry at the top of the `## Changelog` section in the skill's `README.md`.
- Rebuild `package/<skill-name>.skill` from the source files after the bump, keeping the package's existing file layout.
- Tag the commit `<skill-name>-v<version>`, for example `danisher-v1.2.0`, and push the tag.
- README-only changes need no bump. Rebuild the package if it contains the README.
