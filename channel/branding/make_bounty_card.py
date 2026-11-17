# Regenerate: python3 channel/branding/make_bounty_card.py channel/branding tools/MoneyPrinterTurbo/resource/fonts  (needs Pillow)
# Photo for the RentAHuman feedback bounty: 1080x1350 PNG. Reuses the drawing helpers from make_branding.py.
import math, random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
OUT, FONTS = sys.argv[1], sys.argv[2]
src = (Path(__file__).parent / "make_branding.py").read_text(encoding="utf-8")
exec(src[src.index("BOLD, MED"):src.index("# Profile picture")].replace("BOLD, MED =", "BOLD, MED =", 1), globals())
GREY, RED = (180, 190, 220), (248, 113, 113)
W, H = 1080, 1350
im = bg(W, H)
network(im, (880, 230, 1060, 500), 9, 5, 6, 2)
network(im, (20, 1080, 1060, 1330), 16, 9, 5, 2)
d = ImageDraw.Draw(im)
f = lambda bold, size: ImageFont.truetype(BOLD if bold else MED, size)

logo = Image.open(f"{OUT}/profile-800.png").resize((150, 150), Image.LANCZOS)
mask = Image.new("L", logo.size, 0); ImageDraw.Draw(mask).ellipse([0, 0, 149, 149], fill=255)
im.paste(logo, (80, 80), mask)
d.text((260, 125), "MAHABUDDHI", font=f(True, 56), fill=WHITE, anchor="lm")
d.text((262, 185), "Superintelligence, simply explained.", font=f(False, 30), fill=CYAN, anchor="lm")

glow_text(im, (80, 360), "Feedback task", f(True, 96), WHITE, CYAN, 14, anchor="lm")
d.text((82, 450), "Watch 5 short AI videos. Tell us the truth.", font=f(False, 38), fill=GREY, anchor="lm")

steps = [("1", "Watch 5 unlisted Shorts", "under 60 seconds each, on your phone"),
         ("2", "Answer 4 quick questions", "for each video, in your own words"),
         ("3", "Send your answers", "within 48 hours of getting the links")]
y = 580
for n, head, sub in steps:
    d.ellipse([80, y - 42, 164, y + 42], outline=CYAN, width=5)
    d.text((122, y), n, font=f(True, 44), fill=CYAN, anchor="mm")
    d.text((200, y - 18), head, font=f(True, 44), fill=WHITE, anchor="lm")
    d.text((200, y + 30), sub, font=f(False, 30), fill=GREY, anchor="lm")
    y += 140

y = 1010
x = 80
for text in ["about 20 min", "$12 fixed", "Remote"]:
    w = d.textlength(text, font=f(True, 38)) + 60
    d.rounded_rectangle([x, y - 40, x + w, y + 40], radius=40, fill=NAVY2, outline=CYAN, width=3)
    d.text((x + w / 2, y), text, font=f(True, 38), fill=WHITE, anchor="mm")
    x += w + 28

veil = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(veil).rectangle([0, 1090, W, 1250], fill=NAVY + (230,))
im.paste(veil, (0, 0), veil); d = ImageDraw.Draw(im)
d.text((W / 2, 1140), "Feedback only:", font=f(True, 36), fill=RED, anchor="mm")
d.text((W / 2, 1195), "please do not like, comment or subscribe", font=f(False, 36), fill=WHITE, anchor="mm")
im.convert("RGB").save(f"{OUT}/bounty-feedback-1080x1350.png", optimize=True)
print("ok")
