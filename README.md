# n00bSKILL

`n00bSKILL` is a public home for random skills I make over time.

The name is half "noob skill" and half "noobs kill," which is exactly the right level of serious for this repo.

## Download

If you are here to install the combined Humanizer + Danish skill in Claude, download:

[`packages/humanizer-danish.skill`](packages/humanizer-danish.skill)

That file is the uploadable Claude skill package. The `skills/humanizer-danish/` folder is the editable source version, not the file you upload.

## Skills

- [`humanizer-danish-addendum`](skills/humanizer-danish-addendum/) — a discoverable bolt-on skill for humanizing Danish text with Humanizer-style agents. It complements the original [Humanizer skill by blader](https://github.com/blader/humanizer), catches Danish-specific AI tells, and includes instructions for using it alongside or merging it into an existing Humanizer skill.
- [`humanizer-danish`](skills/humanizer-danish/) — source for the combined Humanizer + Danish skill intended for Claude.ai Team and Enterprise organization skill provisioning. Upload `packages/humanizer-danish.skill` from `Organization settings > Skills`.

## Claude Organization Skill Upload

Use this option when you want the combined Humanizer + Danish skill available to everyone in a Claude Team or Enterprise organization.

Upload this file:

```text
packages/humanizer-danish.skill
```

Owner provisioning flow:

1. Open `Organization settings > Skills` in Claude.
2. Enable `Code execution and file creation` and `Skills` if they are not already enabled.
3. In `Organization skills`, click `+ Add`.
4. Upload `packages/humanizer-danish.skill`.

The `.skill` file is a ZIP-format archive and includes `humanizer-danish/SKILL.md`.

## Layout

- `skills/` is where skills will live.
- `packages/` contains generated `.skill` upload artifacts for hosted Claude skill installs.

## License

MIT
