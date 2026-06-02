# n00bSKILL

`n00bSKILL` is a public collection of reusable AI agent skills.

## How This Repo Is Organized

Each skill has its own folder under `skills/`. Treat each folder as the landing page for that skill: it contains the source `SKILL.md`, install instructions, attribution, and any packaged upload artifacts.

The root README stays intentionally small. It explains the repo and lists available skills. Go to a skill folder for installation details.

## Available Skills

| Skill | What it does | Install path |
| --- | --- | --- |
| [`humanizer-danish`](skills/humanizer-danish/) | Combined Humanizer + Danish skill for Claude.ai Team/Enterprise organization provisioning, individual Claude.ai upload, Claude Code, and opencode. | Start on the skill landing page. |
| [`humanizer-danish-addendum`](skills/humanizer-danish-addendum/) | Bolt-on Danish pass for people who already have the original Humanizer skill installed and want only the Danish-specific tells. | Start on the skill landing page. |

## Choosing a Skill

Use `humanizer-danish` if you want one complete installable skill. This is the normal choice for Claude.ai organization skills.

Use `humanizer-danish-addendum` if you already maintain a separate Humanizer skill and only want to add Danish-specific guidance.

## Layout

- `skills/<skill-name>/README.md` is the public landing page for that skill.
- `skills/<skill-name>/SKILL.md` is the source skill file.
- `skills/<skill-name>/package/` contains upload-ready artifacts for that skill, when needed.

## License

MIT
