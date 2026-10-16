# Regenerate: python3 channel/branding/make_branding.py channel/branding tools/MoneyPrinterTurbo/resource/fonts  (needs Pillow)
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
OUT, FONTS = sys.argv[1], sys.argv[2]
BOLD, MED = f"{FONTS}/BeVietnamPro-Bold.ttf", f"{FONTS}/BeVietnamPro-Medium.ttf"
NAVY, NAVY2, CYAN, VIOLET, WHITE = (11,16,32), (24,30,66), (34,211,238), (139,92,246), (240,248,255)

def bg(w, h):
    im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
    cx, cy, R = w*0.62, h*0.5, max(w, h)*0.7
    for i in range(60, 0, -1):            # soft radial glow
        t = i/60; r = R*t
        c = tuple(int(NAVY[k] + (NAVY2[k]-NAVY[k])*(1-t)) for k in range(3))
        d.ellipse([cx-r, cy-r*0.8, cx+r, cy+r*0.8], fill=c)
    return im

def network(im, box, n, seed, node_r, width):
    rnd = random.Random(seed); x0, y0, x1, y1 = box
    pts = [(rnd.uniform(x0, x1), rnd.uniform(y0, y1)) for _ in range(n)]
    glow = Image.new("RGBA", im.size, (0,0,0,0)); g = ImageDraw.Draw(glow)
    sharp = Image.new("RGBA", im.size, (0,0,0,0)); s = ImageDraw.Draw(sharp)
    span = max(x1-x0, y1-y0)
    for i, a in enumerate(pts):
        near = sorted(pts, key=lambda b: (a[0]-b[0])**2 + (a[1]-b[1])**2)[1:4]
        for b in near:
            dist = math.dist(a, b); alpha = int(max(40, 170 - dist/span*400))
            col = CYAN if (i % 3) else VIOLET
            s.line([a, b], fill=col + (alpha,), width=width)
    for i, (x, y) in enumerate(pts):
        r = node_r * rnd.uniform(0.6, 1.4); col = CYAN if (i % 4) else VIOLET
        g.ellipse([x-r*3, y-r*3, x+r*3, y+r*3], fill=col + (90,))
        s.ellipse([x-r, y-r, x+r, y+r], fill=WHITE + (235,))
    glow = glow.filter(ImageFilter.GaussianBlur(node_r*2))
    im.paste(glow, (0,0), glow); im.paste(sharp, (0,0), sharp)

def glow_text(im, xy, text, font, fill, glow_col, blur, anchor="mm"):
    layer = Image.new("RGBA", im.size, (0,0,0,0)); ImageDraw.Draw(layer).text(xy, text, font=font, fill=glow_col+(200,), anchor=anchor)
    layer = layer.filter(ImageFilter.GaussianBlur(blur)); im.paste(layer, (0,0), layer)
    ImageDraw.Draw(im).text(xy, text, font=font, fill=fill, anchor=anchor)

# Profile picture 800x800 (shown as a circle)
p = bg(800, 800)
network(p, (60, 60, 740, 740), 26, 7, 7, 3)
veil = Image.new("RGBA", p.size, (0,0,0,0)); ImageDraw.Draw(veil).ellipse([170,170,630,630], fill=NAVY+(215,))
veil = veil.filter(ImageFilter.GaussianBlur(30)); p.paste(veil, (0,0), veil)
ImageDraw.Draw(p).ellipse([190,190,610,610], outline=CYAN, width=10)
glow_text(p, (400, 392), "M", ImageFont.truetype(BOLD, 330), WHITE, CYAN, 22)
p.save(f"{OUT}/profile-800.png")

# Watermark 150x150
p.resize((150,150), Image.LANCZOS).save(f"{OUT}/watermark-150.png")

# Banner 2560x1440, text inside centre safe area 1546x423 (x 507-2053, y 508-931)
b = bg(2560, 1440)
network(b, (1350, 120, 2500, 1320), 70, 11, 8, 3)
network(b, (40, 80, 700, 1360), 22, 3, 6, 2)
veil = Image.new("RGBA", b.size, (0,0,0,0)); ImageDraw.Draw(veil).rectangle([480, 470, 1500, 970], fill=NAVY+(200,))
veil = veil.filter(ImageFilter.GaussianBlur(60)); b.paste(veil, (0,0), veil)
glow_text(b, (560, 640), "MAHABUDDHI", ImageFont.truetype(BOLD, 150), WHITE, CYAN, 18, anchor="lm")
ImageDraw.Draw(b).text((566, 760), "Superintelligence, simply explained.", font=ImageFont.truetype(MED, 64), fill=CYAN, anchor="lm")
ImageDraw.Draw(b).text((568, 870), "New explainers every week  ·  Hindi + English", font=ImageFont.truetype(MED, 42), fill=(180,190,220), anchor="lm")
b.save(f"{OUT}/banner-2560x1440.png")

# Safe-area preview so you can check what phones show
prev = b.copy(); ImageDraw.Draw(prev).rectangle([507, 508, 2053, 931], outline=(255,80,80), width=6)
prev.resize((1280, 720)).save(f"{OUT}/../banner-safe-area-preview.png")
print("ok")
