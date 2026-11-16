import os
from PIL import Image, ImageDraw, ImageFont
os.makedirs("assets", exist_ok=True)
def font(n):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","DejaVuSans-Bold.ttf"):
        try: return ImageFont.truetype(p, n)
        except Exception: pass
    return ImageFont.load_default()
def grad(n):
    im = Image.new("RGB", (n, n)); px = im.load()
    for y in range(n):
        for x in range(n):
            t = (x + y) / (2 * n)
            px[x, y] = (int(139 + (59 - 139) * t), int(92 + (130 - 92) * t), int(246 + (246 - 246) * t))
    return im
def mark(n, pad):
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w = n // 24; d.ellipse([pad, pad, n - pad, n - pad], outline="white", width=w)
    f = font(int(n * 0.34)); b = d.textbbox((0, 0), "01", font=f)
    d.text(((n - b[2] - b[0]) / 2, (n - b[3] - b[1]) / 2), "01", font=f, fill="white")
    return im
g = grad(1024); g.save("assets/icon-background.png")
mark(1024, 300).save("assets/icon-foreground.png")
full = g.convert("RGBA"); full.alpha_composite(mark(1024, 180)); full.convert("RGB").save("assets/icon-only.png")
for name, bg in (("splash", (9, 9, 18)), ("splash-dark", (9, 9, 18))):
    im = Image.new("RGB", (2732, 2732), bg); ic = full.resize((700, 700)); im.paste(ic, (1016, 1016)); im.save("assets/%s.png" % name)
