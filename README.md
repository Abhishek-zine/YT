# YT

My YouTube workflow, run with Claude Code.

`.claude/skills/` holds the 11 `/yt-*` skills from
[youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) (MIT, commit a2feb21).
They write scripts, titles, edit lists, SEO text and so on. They never log in to YouTube or upload anything.

## Setup
1. Fill in `youtube/voice.md`. Every skill reads it, through `~/.claude/youtube/voice.md`; a SessionStart hook in `.claude/settings.json` links that path to this file.
2. Python 3 is needed for the built-in tools. No extra packages.

## Weekly workflow
1. `/yt-viral`: find what's working in your niche
2. `/yt-plan`: plan the week around your real hours
3. `/yt-script`: write the script and pick the strongest hook
4. `/yt-package`: title and thumbnail text together
5. `/yt-edit`: cut list from the recording's `.srt`
6. `/yt-seo` + `/yt-chapters`: description and chapters
7. `/yt-shorts`: 3 Shorts from the same video
8. `/yt-retention`: after 2–3 days, find where viewers left (Studio CSV export)

Also: `/yt-comment` (reply to comments), `/yt-audit` (channel review that ends in one fix).
