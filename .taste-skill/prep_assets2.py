"""Second pass on the client's own assets: the crops the build needs.

- the three partners' portraits, cropped to 4:5 and written large enough for
  the column they sit in
- the blue particle field, written as the research matrix's flow picture
- the client's own research diagrams, kept at their native size

Every source file is the client's own artwork; nothing is generated.
"""
import os
from PIL import Image

SRC = r"C:\Users\kwena\Downloads\euclidean capital\assets"
OUT = os.path.join(SRC, "web")
os.makedirs(OUT, exist_ok=True)


def portrait(name, src, w=800, h=1000):
    """Crop to 4:5, taking the head, and write it large enough to print sharp."""
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    target = w / h
    cw, ch = im.size
    if cw / ch > target:            # too wide: cut the sides
        nw = round(ch * target)
        left = (cw - nw) // 2
        im = im.crop((left, 0, left + nw, ch))
    else:                            # too tall: cut the top and the foot
        nh = round(cw / target)
        top = max(0, round((ch - nh) * 0.12))
        im = im.crop((0, top, cw, top + nh))
    im = im.resize((w, h), Image.LANCZOS)
    im.save(os.path.join(OUT, f"{name}-{w}.jpg"), "JPEG", quality=88, optimize=True, progressive=True)
    print(f"  {name}-{w}.jpg  {w}x{h}  (from {src})")


def plain(name, src, width=None, quality=86):
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    if width and width < im.width:
        h = round(im.height * width / im.width)
        im = im.resize((width, h), Image.LANCZOS)
    im.save(os.path.join(OUT, f"{name}.jpg"), "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"  {name}.jpg  {im.width}x{im.height}  (from {src})")


print("portraits")
portrait("sibo", "team-sibo-khumalo.png")
portrait("langa", "team-langa-malimela.png")
portrait("bryan", "team-bryan-shuping.png")

print("research pictures")
plain("flows-736", "img_05b41afc.png")
plain("flows-400", "img_05b41afc.png", width=400)
plain("diagrams-558", "approach-diagrams.png")

print("done")
