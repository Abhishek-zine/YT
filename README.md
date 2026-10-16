# YT

My YouTube workflow: Claude Code skills for scripts, packaging and virality, plus
[MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) (MIT, ~130k stars) for making the videos.

| Part | Tool | Where |
|---|---|---|
| Ideas, virality, scripts, titles, SEO, Shorts, retention | 11 `/yt-*` skills | `.claude/skills/` |
| Video creator: script → footage → subtitles → music → MP4 | MoneyPrinterTurbo | `tools/MoneyPrinterTurbo` (submodule, pinned c3634de) |
| Audio creator: free male voice (Edge TTS) or your own recording | MoneyPrinterTurbo | `voice_name` in config, or `VOICE_FILE=` |
| Upload to YouTube (optional, uploads as **private**) | MoneyPrinterTurbo + upload-post.com | `upload_post_*` in config |

## Video creator setup (on your own computer)

Needs git, Python 3.11+ and ffmpeg.

```bash
git clone --recurse-submodules <this repo> && cd YT
./setup.sh
```

Then edit `tools/MoneyPrinterTurbo/config.toml` (git-ignored, never commit it):
- `anthropic_api_key`: writes the scripts (https://platform.claude.com/settings/keys)
- `pexels_api_keys = ["..."]`: free stock footage (https://www.pexels.com/api/)
- Voice: defaults to `hi-IN-MadhurNeural-Male` (Hindi, male). For English use `en-IN-PrabhatNeural-Male`.

Make a video:

```bash
./make-video.sh "3 money habits nobody teaches you"            # AI writes script, male AI voice
VOICE_FILE=my_voice.mp3 ./make-video.sh "topic" "exact script"  # your own recorded narration
./make-video.sh "topic" --video-aspect 16:9                     # long-form instead of Shorts
./webui.sh                                                      # browser UI at http://127.0.0.1:8501
```

Videos land in `tools/MoneyPrinterTurbo/storage/tasks/<id>/final-1.mp4`.

**Recommended loop:** `/yt-viral` → `/yt-script` (best hook) → feed that script to `make-video.sh` →
`/yt-package` + `/yt-seo` → review the MP4 yourself → upload.

**Before uploading:** YouTube does not pay for "reused" or mass-produced, low-effort videos. Use your
own script and voice, check every clip, and turn on the "altered or synthetic content" label in
Studio when you use an AI voice.

## Claude skills

The `.claude/skills/` folder holds the 11 `/yt-*` skills from
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
