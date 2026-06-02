# n00bSKILL

`n00bSKILL` is a public home for random skills I make over time.

The name is half "noob skill" and half "noobs kill," which is exactly the right level of serious for this repo.

## Skills

- [`humanizer-danish-addendum`](skills/humanizer-danish-addendum/) — a discoverable bolt-on skill for humanizing Danish text with Humanizer-style agents. It complements the original [Humanizer skill by blader](https://github.com/blader/humanizer), catches Danish-specific AI tells, and includes instructions for using it alongside or merging it into an existing Humanizer skill.
- [`humanizer-danish`](skills/humanizer-danish/) — a combined Humanizer + Danish skill intended for Claude.ai Team and Enterprise organization skill provisioning. Upload `packages/humanizer-danish.skill` from `Organization settings > Skills`; `packages/humanizer-danish.zip` is included as a compatibility copy.

## Claude Organization Skill Upload

Use this option when you want the combined Humanizer + Danish skill available to everyone in a Claude Team or Enterprise organization.

Upload artifact:

```text
packages/humanizer-danish.skill
```

Compatibility artifact:

```text
packages/humanizer-danish.zip
```

Owner provisioning flow:

1. Open `Organization settings > Skills` in Claude.
2. Enable `Code execution and file creation` and `Skills` if they are not already enabled.
3. In `Organization skills`, click `+ Add`.
4. Upload `packages/humanizer-danish.skill`.
5. If the UI rejects `.skill`, upload `packages/humanizer-danish.zip` instead.

Both artifacts are ZIP-format archives and include `humanizer-danish/SKILL.md`.

## Layout

- `skills/` is where skills will live.
- `packages/` contains generated upload artifacts for hosted Claude skill installs.

## License

MIT
