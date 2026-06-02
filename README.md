# n00bSKILL

`n00bSKILL` is a public collection of reusable AI agent skills.

## How This Repo Is Organized

Each skill has its own folder under `skills/`. Treat each folder as the landing page for that skill: it contains the source `SKILL.md`, install instructions, attribution, and any packaged upload artifacts.

The root README stays intentionally small. It explains the repo and lists available skills. Go to a skill folder for installation details.

## Available Skills

| Skill | What it does | Install path |
| --- | --- | --- |
| [`humanizer-danish`](skills/humanizer-danish/) | Combined Humanizer + Danish skill for Claude.ai Team/Enterprise organization provisioning, individual Claude.ai upload, Claude Code, and opencode. | Start on the skill landing page. |
| [`humanizer-danish-addendum`](skills/humanizer-danish-addendum/) | Danish-specific Humanizer addendum, with the ready-made combined `.skill` package mirrored for Claude Teams and simple installs. | Start on the skill landing page. |

## Layout

- `skills/<skill-name>/README.md` is the public landing page for that skill.
- `skills/<skill-name>/SKILL.md` is the source skill file.
- `skills/<skill-name>/package/` contains upload-ready artifacts for that skill, when needed.

## License

MIT
