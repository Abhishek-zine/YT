# Regenerate: python3 channel/branding/make_bounty_card.py channel/branding tools/MoneyPrinterTurbo/resource/fonts  (needs Pillow)
# Photos for RentAHuman bounties: 1080x1350 PNGs. Reuses the drawing helpers from make_branding.py.
import math, random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
OUT, FONTS = sys.argv[1], sys.argv[2]
src = (Path(__file__).parent / "make_branding.py").read_text(encoding="utf-8")
exec(src[src.index("BOLD, MED"):src.index("# Profile picture")], globals())
GREY, RED, GREEN = (180, 190, 220), (248, 113, 113), (74, 222, 128)
W, H = 1080, 1350

CARDS = {
    "bounty-feedback-1080x1350.png": dict(
        title="Feedback task", sub="Watch 5 short AI videos. Tell us the truth.",
        steps=[("Watch 5 unlisted Shorts", "under 60 seconds each, on your phone"),
               ("Answer 4 quick questions", "for each video, in your own words"),
               ("Send your answers", "within 48 hours of getting the links")],
        chips=["about 20 min", "$12 fixed", "Remote"],
        foot=("Feedback only:", "please do not like, comment or subscribe", RED)),
    "bounty-promote-1080x1350.png": dict(
        title="Recommend us", sub="One post to your followers about AI, in your words.",
        steps=[("Watch 1–2 Mahabuddhi videos", "so your recommendation is genuine"),
               ("Make 1 post on your account", "TikTok, Instagram, X, LinkedIn or Threads"),
               ("Add #ad and the channel link", "then send us the link to your post")],
        chips=["$25 per post", "about 1 hour", "Remote"],
        need="Needs 1,000+ real followers  ·  US, UK, Canada or Australia",
        foot=("Honest promotion:", "no bots, no sub4sub, no rewards for subscribing", GREEN)),
}

f = lambda bold, size: ImageFont.truetype(BOLD if bold else MED, size)
logo = Image.open(f"{OUT}/profile-800.png").resize((150, 150), Image.LANCZOS)
mask = Image.new("L", logo.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 149, 149], fill=255)

for name, c in CARDS.items():
    im = bg(W, H)
    network(im, (880, 230, 1060, 500), 9, 5, 6, 2)
    network(im, (20, 1080, 1060, 1330), 16, 9, 5, 2)
    d = ImageDraw.Draw(im)
    im.paste(logo, (80, 80), mask)
    d.text((260, 125), "MAHABUDDHI", font=f(True, 56), fill=WHITE, anchor="lm")
    d.text((262, 185), "Superintelligence, simply explained.", font=f(False, 30), fill=CYAN, anchor="lm")
    glow_text(im, (80, 360), c["title"], f(True, 96), WHITE, CYAN, 14, anchor="lm")
    d.text((82, 450), c["sub"], font=f(False, 36), fill=GREY, anchor="lm")

    y = 580
    for i, (head, sub) in enumerate(c["steps"], 1):
        d.ellipse([80, y - 42, 164, y + 42], outline=CYAN, width=5)
        d.text((122, y), str(i), font=f(True, 44), fill=CYAN, anchor="mm")
        d.text((200, y - 18), head, font=f(True, 42), fill=WHITE, anchor="lm")
        d.text((200, y + 30), sub, font=f(False, 30), fill=GREY, anchor="lm")
        y += 140

    y = 990 if "need" in c else 1010
    x = 80
    for text in c["chips"]:
        w = d.textlength(text, font=f(True, 38)) + 60
        d.rounded_rectangle([x, y - 40, x + w, y + 40], radius=40, fill=NAVY2, outline=CYAN, width=3)
        d.text((x + w / 2, y), text, font=f(True, 38), fill=WHITE, anchor="mm")
        x += w + 28
    if "need" in c:
        d.text((82, 1068), c["need"], font=f(False, 30), fill=GREY, anchor="lm")

    veil = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(veil).rectangle([0, 1105, W, 1255], fill=NAVY + (230,))
    im.paste(veil, (0, 0), veil); d = ImageDraw.Draw(im)
    head, line, col = c["foot"]
    d.text((W / 2, 1150), head, font=f(True, 36), fill=col, anchor="mm")
    d.text((W / 2, 1205), line, font=f(False, 34), fill=WHITE, anchor="mm")
    im.convert("RGB").save(f"{OUT}/{name}", optimize=True)
print("ok")
