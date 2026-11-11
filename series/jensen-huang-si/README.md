# Series: Jensen Huang on AGI and superintelligence

Five English Shorts (9:16, under 60 seconds each) for a US and international audience. Each one
takes one thing Nvidia's CEO said on the record and shows what definition sits underneath it.

The channel's point of view across the series: **Huang is not lying, he is redefining.** Every time
he says AGI or superintelligence "is here", he is using a narrower meaning than researchers do, and
he sells the chips the race runs on.

## Render

```bash
./make-series.sh series/jensen-huang-si        # all five, US male voice, 9:16
```

Each `.txt` file is the exact narration. `make-series.sh` passes it to MoneyPrinterTurbo unchanged,
so the AI does not rewrite it. Videos land in `tools/MoneyPrinterTurbo/storage/tasks/<id>/final-1.mp4`.

## The five Shorts

| # | File | Title | Words | Hook score |
|---|---|---|---|---|
| 1 | `01-the-agi-date-that-moved.txt` | Nvidia's CEO Moved His AGI Date by 5 Years | 143 | 58 workable |
| 2 | `02-eight-words.txt` | The 8 Words Behind "We've Achieved AGI" | 146 | 73 strong |
| 3 | `03-superintelligence-on-the-road.txt` | Is Superintelligence Already Here? 2 Definitions | 149 | 46 weak |
| 4 | `04-zero-percent.txt` | Why Jensen Huang Puts AI Doom at 0% | 156 | 69 workable |
| 5 | `05-two-ceos-one-job.txt` | 2 AI CEOs, 1 Question: Will AI Take Your Job? | 151 | 76 strong |

Hook scores come from `.claude/skills/yt-script/hookscore.py`. Number 3 scored weak; rewrite its
first line before recording if you want (the scorer wants a cost to the viewer in the first sentence).

Runner-up hooks, if you want to A/B the first line:

- 1: "If you plan your career around AGI being 5 years away, you are late. Nvidia's CEO says it's already here, and he changed 1 word to say it." (49)
- 2: "If you think AGI means a machine that does everything, you will miss it. Nvidia's CEO declared it achieved with 7 words. Why?" (58; change 7 to 8 if used)
- 3: "If you are waiting for superintelligence to arrive, you may have already ridden in it. Why does Nvidia's CEO say that?" (48)
- 4: "If you stop learning because AI doom is coming, you lose 5 years. Nvidia's CEO puts that risk at 0%. Is he right?" (60)
- 5: "If you have an entry-level office job, 2 AI CEOs just bet on your future, and they disagree on almost everything. Why?" (60)

## On screen, beat by beat

Stock footage will not carry these on its own. Add the text cards in an editor (CapCut, DaVinci)
after MoneyPrinterTurbo renders the base video.

**All five:** every quote appears as a text card with speaker, venue and date under it. Do not use
AI-generated footage or an AI voice of Huang, Amodei or anyone else.

1. **The AGI date that moved**
   - Hook: `[ON SCREEN: "AGI: 5 years away" crossed out, replaced by "already here"]`
   - 2024 beat: `[ON SCREEN: quote card, "Stanford, March 2024"]`
   - 2026 beat: `[ON SCREEN: quote card, "Lex Fridman Podcast, March 2026"]`
   - Twist: `[ON SCREEN: two columns, "2024 test: every human exam" vs "2026 test: build a $1B company"]`
   - Close: `[ON SCREEN: "Whose definition?"]`
2. **Eight words**
   - Hook: `[ON SCREEN: eight blank boxes]`
   - Question beat: `[ON SCREEN: "Start, grow and run a $1B+ tech company"]`
   - Payoff: `[ON SCREEN: the eight boxes fill: "You said billion, and you didn't say forever."]`
   - Contrast: `[ON SCREEN: "His AGI: reach $1B once" vs "Usual AGI: match humans at almost everything"]`
3. **Superintelligence on the road**
   - Hook: `[ON SCREEN: a self-driving car, label "Superintelligence?"]`
   - CES beat: `[ON SCREEN: quote card, "CES, January 2025"]`
   - All-In beat: `[ON SCREEN: "1/10 the accident rate (Huang's claim)"]`
   - Contrast: `[ON SCREEN: "Bostrom: virtually all domains" vs "Huang: one narrow job"]`
4. **Zero percent**
   - Hook: `[ON SCREEN: big "0%"]`
   - CBS beat: `[ON SCREEN: quote card, "CBS Sunday Morning, September 2026"]`
   - God AI beat: `[ON SCREEN: quote card, "No Priors podcast, January 2026"]`
   - Caveats: `[ON SCREEN: "1. Nvidia sells the chips"  "2. Hinton, Bengio: 2023 risk statement"]`
5. **Two CEOs, one job**
   - Hook: `[ON SCREEN: split screen, "Amodei: half of entry-level jobs" vs "Huang: disagree"]`
   - VivaTech beat: `[ON SCREEN: quote card, "VivaTech, Paris, June 2025"]`
   - Condition: `[ON SCREEN: quote card, "If the world runs out of ideas..." "CNN"]`
   - Close: `[ON SCREEN: "Learn the tools now"]`

## Sources (paste the relevant ones into each description)

Every quote below came from press reports found by web search in November 2026. **None was checked
against the original video or transcript**, because the news sites were not reachable from the
session that wrote these scripts. Before publishing, open each link and confirm the wording; if a
quote does not match, change the script to a paraphrase.

| Short | Claim | Source |
|---|---|---|
| 1 | Stanford, 1 March 2024: "I'm guessing in five years we'll do well on every single one" | Reuters, via https://www.businesslive.co.za/bd/companies/telecoms-and-technology/2024-03-03-nvidia-ceo-backs-computers-to-think-like-humans-in-five-years/ |
| 1, 2 | Lex Fridman Podcast #494, March 2026: "I think we've achieved AGI"; "You said billion, and you didn't say forever" | https://finance.yahoo.com/news/nvidia-ceo-jensen-huang-claims-agi-has-been-achieved-can-create-billion-dollar-businesses-172225126.html and https://www.tomsguide.com/ai/i-think-weve-achieved-agi-nvidias-ceo-believes-weve-finally-achieved-artificial-general-intelligence |
| 2 | Critics on his definition | https://www.techspot.com/news/111797-weve-achieved-agi-nvidia-ceo-but-own-examples.html |
| 3 | CES, January 2025: "I'm surrounded by superintelligence" | https://www.engadget.com/ai/nvidia-ceo-jensen-huang-welcomes-the-rise-of-superintelligent-ai-at-ces-2025-002827074.html |
| 3 | All-In Summit, September 2026: self-driving as narrow superintelligence, one tenth the accident rate. Only found in translated coverage, so the script paraphrases it | https://eu.36kr.com/en/p/3985513458875143 |
| 3 | Bostrom's definition: "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest" | Nick Bostrom, *Superintelligence* (2014), chapter 2. Written from memory; check the book |
| 4 | CBS Sunday Morning, aired 20 September 2026: "2030 is not going to be the end of the world. There is 0% chance..." | https://www.foxbusiness.com/technology/nvidias-jensen-huang-rejects-ai-doomsday-fears-2030-not-going-end-world |
| 4 | No Priors podcast, January 2026: "I guess someday we will have God AI"; no researcher has "any reasonable ability" to create it | https://www.pcgamer.com/software/ai/nvidia-ceo-jensun-huang-critiques-well-respected-people-who-have-painted-a-doomer-narrative-around-ai-right-after-saying-i-guess-someday-we-will-have-god-ai and https://www.techradar.com/pro/dont-be-a-doomer-nvidia-ceo-jensen-huang-says-no-one-currently-has-any-reasonable-ability-to-create-god-ai-so-we-should-all-just-relax |
| 4 | 2023 Center for AI Safety statement signed by Hinton and Bengio | https://www.safe.ai/work/statement-on-ai-risk (written from memory; check the page) |
| 5 | Amodei, May 2025: AI could wipe out half of entry-level white-collar jobs in one to five years | Axios interview, May 2025 (written from memory; find and link the article) |
| 5 | VivaTech, 11 June 2025: "pretty much disagree with almost everything"; "It's changed mine" | https://fortune.com/2025/06/11/nvidia-jensen-huang-disagress-anthropic-ceo-dario-amodei-ai-jobs/ |
| 5 | CNN: "If the world runs out of ideas, then productivity gains translate to job loss" | https://www.windowscentral.com/artificial-intelligence/nvidia-ceo-cnn-everybodys-job-affected-ideas |

## Before publishing each one

- [ ] Quotes checked against the original (see above)
- [ ] Sources pasted into the description
- [ ] "Altered or synthetic content" set to Yes (AI voice)
- [ ] Text cards added; no stock clip implies it shows Huang when it does not
- [ ] `/yt-package` and `/yt-seo` run on the final title and description
