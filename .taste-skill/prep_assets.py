"""Prepare the client's own brand assets for the web build.

- crops the wordmark out of its square PNG so it can sit in a nav bar
- writes optimised 400/800/1600 JPEG + WebP derivatives for srcset
- makes the poster/stand-ins the browser needs

Every source file is the client's own artwork; nothing is generated.
"""
import os
from PIL import Image

SRC = r"C:\Users\kwena\Downloads\euclidean capital\assets"
OUT = os.path.join(SRC, "web")
os.makedirs(OUT, exist_ok=True)


def alpha_crop(im, pad=0):
    """Crop to the opaque content, with a little padding."""
    if im.mode != "RGBA":
        return im
    bbox = im.getbbox()
    if not bbox:
        return im
    l, t, r, b = bbox
    l = max(0, l - pad); t = max(0, t - pad)
    r = min(im.width, r + pad); b = min(im.height, b + pad)
    return im.crop((l, t, r, b))


def derivatives(name, src, widths=(400, 800, 1600), flat=True):
    im = Image.open(os.path.join(SRC, src)).convert("RGBA")
    if flat:
        # flatten onto the brand's dark navy so a transparent PNG prints as the
        # brand sees it; the webp/jpg pair keeps the alpha where it matters
        pass
    stem = name
    for w in widths:
        if w > im.width:
            continue
        h = round(im.height * w / im.width)
        r = im.resize((w, h), Image.LANCZOS)
        # jpeg: flatten on navy
        bg = Image.new("RGB", r.size, (18, 24, 43))
        bg.paste(r, (0, 0), r)
        bg.save(os.path.join(OUT, f"{stem}-{w}.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
        # webp: keep the alpha
        r.save(os.path.join(OUT, f"{stem}-{w}.webp"), "WEBP", quality=80, method=6)
    # the original stays as the largest
    print(f"  {stem}: {im.width}x{im.height} -> " + ", ".join(f"{w}" for w in widths if w <= im.width))


print("wordmark (crop the transparent square)")
wm = alpha_crop(Image.open(os.path.join(SRC, "logo.png")))
wm.save(os.path.join(OUT, "wordmark.png"))
print(f"  logo.png -> wordmark.png {wm.width}x{wm.height}")
for w in (400, 800):
    h = round(wm.height * w / wm.width)
    r = wm.resize((w, h), Image.LANCZOS)
    bg = Image.new("RGB", r.size, (18, 24, 43))
    bg.paste(r, (0, 0), r)
    bg.save(os.path.join(OUT, f"wordmark-{w}.jpg"), "JPEG", quality=88, optimize=True)
    r.save(os.path.join(OUT, f"wordmark-{w}.webp"), "WEBP", quality=85, method=6)

print("photographs")
for name, src in [
    ("globe", "globe.png"),
    ("network", "hero-network.png"),
    ("silver-bar", "insights-silver-bar.png"),
    ("folio", "leather-portfolio.png"),
    ("cufflink", "cufflink-ec.png"),
    ("card", "Rectangle_10_f2c2769d.png"),
    ("nodes", "background.png"),
    ("sibo", "team-sibo-khumalo.png"),
    ("langa", "team-langa-malimela.png"),
    ("bryan", "team-bryan-shuping.png"),
    ("diagrams", "approach-diagrams.png"),
]:
    derivatives(name, src)

print("done ->", OUT)
