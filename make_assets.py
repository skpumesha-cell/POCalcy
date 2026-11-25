import os
import shutil
from PIL import Image, ImageDraw

os.makedirs("assets", exist_ok=True)


def draw(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size / 256.0
    d.rounded_rectangle([8 * s, 8 * s, 248 * s, 248 * s], radius=48 * s, fill=(204, 0, 0, 255))
    # envelope
    d.rectangle([48 * s, 80 * s, 208 * s, 176 * s], fill=(255, 255, 255, 255))
    d.line([48 * s, 80 * s, 128 * s, 140 * s, 208 * s, 80 * s], fill=(204, 0, 0, 255), width=max(2, int(8 * s)))
    # rupee-style bars
    d.rectangle([88 * s, 190 * s, 168 * s, 202 * s], fill=(255, 255, 255, 255))
    d.rectangle([88 * s, 212 * s, 168 * s, 224 * s], fill=(255, 255, 255, 255))
    return img


# logo.png (shown in the app header) - keep it small
if not os.path.exists("assets/logo.png"):
    draw(256).resize((110, 110), Image.LANCZOS).save("assets/logo.png")
else:
    im = Image.open("assets/logo.png")
    if im.height > 120:  # repo copy is 1408x768 - far too big for the header
        im = im.convert("RGBA")
        im.thumbnail((400, 110), Image.LANCZOS)
        im.save("assets/logo.png")

# icon.ico (exe icon + MSI icon) - prefer the project's own logo.ico
if not os.path.exists("assets/icon.ico"):
    if os.path.exists("assets/logo.ico"):
        shutil.copyfile("assets/logo.ico", "assets/icon.ico")
    else:
        draw(256).save("assets/icon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("assets ready")
