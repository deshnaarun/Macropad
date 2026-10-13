#!/usr/bin/env python3
"""Draws original 48x32 pixel-art cat frames and emits a QMK header."""
import math

W, H = 48, 32


def blank():
    return [[0] * W for _ in range(H)]


def px(g, x, y, v=1):
    if 0 <= x < W and 0 <= y < H:
        g[y][x] = v


def rect(g, x0, y0, x1, y1, v=1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            px(g, x, y, v)


def ellipse(g, cx, cy, rx, ry, v=1):
    for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                px(g, x, y, v)


def line(g, x0, y0, x1, y1, v=1, thick=1):
    n = max(abs(x1 - x0), abs(y1 - y0), 1)
    for i in range(n + 1):
        x = round(x0 + (x1 - x0) * i / n)
        y = round(y0 + (y1 - y0) * i / n)
        for dx in range(thick):
            for dy in range(thick):
                px(g, x + dx, y + dy, v)


def tri(g, a, b, c, v=1):
    xs = [a[0], b[0], c[0]]
    ys = [a[1], b[1], c[1]]

    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            d1, d2, d3 = sign((x, y), a, b), sign((x, y), b, c), sign((x, y), c, a)
            neg = d1 < 0 or d2 < 0 or d3 < 0
            pos = d1 > 0 or d2 > 0 or d3 > 0
            if not (neg and pos):
                px(g, x, y, v)


def head(g, hx, hy, eye="open"):
    """Cat head facing right, centered near (hx, hy)."""
    ellipse(g, hx, hy, 6, 5)
    tri(g, (hx - 5, hy - 3), (hx - 4, hy - 9), (hx - 1, hy - 4))   # back ear
    tri(g, (hx + 0, hy - 4), (hx + 3, hy - 9), (hx + 5, hy - 2))   # front ear
    if eye == "open":
        px(g, hx + 2, hy - 1, 0)
        px(g, hx + 3, hy - 1, 0)
    elif eye == "closed":
        px(g, hx + 1, hy, 0)
        px(g, hx + 2, hy, 0)
        px(g, hx + 3, hy, 0)
    px(g, hx + 6, hy + 1, 0)  # nose notch
    # whiskers
    px(g, hx + 7, hy + 1)
    px(g, hx + 8, hy)
    px(g, hx + 8, hy + 2)


def legs(g, positions, top, bottom):
    for (x, lift) in positions:
        rect(g, x, top, x + 2, bottom - lift)


def cat_sleep(frame):
    g = blank()
    ellipse(g, 21, 23, 16, 7)               # loaf body
    rect(g, 6, 26, 36, 29)                  # flat belly on the ground
    head(g, 35, 23, eye="closed")
    # tail curled round the front
    line(g, 6, 27, 4, 22, thick=2)
    line(g, 4, 22, 8, 18, thick=2)
    # Zs
    if frame == 0:
        line(g, 38, 8, 41, 8)
        line(g, 41, 8, 38, 11)
        line(g, 38, 11, 41, 11)
    else:
        line(g, 41, 3, 43, 3)
        line(g, 43, 3, 41, 5)
        line(g, 41, 5, 43, 5)
        line(g, 36, 10, 39, 10)
        line(g, 39, 10, 36, 13)
        line(g, 36, 13, 39, 13)
    return g


def cat_walk(frame):
    g = blank()
    ellipse(g, 20, 16, 12, 5)
    rect(g, 10, 14, 30, 20)
    head(g, 35, 12)
    tilt = [(-1, 0), (0, 0), (1, 0), (0, 0)][frame % 4]
    # tail up and swaying
    line(g, 8, 15, 5 + tilt[0], 8, thick=2)
    line(g, 5 + tilt[0], 8, 6 + tilt[0] * 2, 4, thick=2)
    sets = [
        [(10, 0), (14, 2), (25, 2), (29, 0)],
        [(11, 0), (15, 0), (24, 0), (28, 0)],
        [(10, 2), (14, 0), (25, 0), (29, 2)],
        [(11, 0), (15, 0), (24, 0), (28, 0)],
    ]
    legs(g, sets[frame % 4], 19, 29)
    return g


def cat_run(frame):
    g = blank()
    ellipse(g, 21, 15, 13, 4)
    rect(g, 10, 13, 32, 18)
    head(g, 38, 11)
    # tail streaming back
    line(g, 9, 14, 2, 12 + (frame % 2) * 2, thick=2)
    if frame % 2 == 0:
        # gathered legs
        line(g, 12, 18, 16, 27, thick=2)
        line(g, 16, 18, 20, 27, thick=2)
        line(g, 26, 18, 31, 26, thick=2)
        line(g, 30, 18, 33, 27, thick=2)
    else:
        # stretched legs
        line(g, 10, 18, 4, 27, thick=2)
        line(g, 14, 18, 8, 28, thick=2)
        line(g, 31, 18, 40, 23, thick=2)
        line(g, 33, 17, 44, 21, thick=2)
    # speed lines
    for i, y in enumerate((8, 21, 26)):
        x = 0 + ((frame * 3 + i * 5) % 8)
        px(g, x, y)
        px(g, x + 1, y)
        px(g, x + 2, y)
    return g


def to_bytes(g):
    out = []
    for page in range(H // 8):
        for x in range(W):
            b = 0
            for bit in range(8):
                if g[page * 8 + bit][x]:
                    b |= 1 << bit
            out.append(b)
    return out


def preview(g):
    return "\n".join("".join("#" if v else "." for v in row) for row in g)


def fmt(name, g):
    data = to_bytes(g)
    rows = []
    for i in range(0, len(data), 12):
        rows.append("    " + ", ".join(f"0x{b:02X}" for b in data[i:i + 12]) + ",")
    return f"static const char PROGMEM {name}[CAT_BYTES] = {{\n" + "\n".join(rows) + "\n};\n"


if __name__ == "__main__":
    import sys

    frames = {
        "cat_sleep_0": cat_sleep(0),
        "cat_sleep_1": cat_sleep(1),
        "cat_walk_0": cat_walk(0),
        "cat_walk_1": cat_walk(1),
        "cat_walk_2": cat_walk(2),
        "cat_walk_3": cat_walk(3),
        "cat_run_0": cat_run(0),
        "cat_run_1": cat_run(1),
    }
    if len(sys.argv) > 1 and sys.argv[1] == "preview":
        for k, g in frames.items():
            print(f"--- {k}")
            print(preview(g))
        sys.exit(0)

    header = [
        "// Generated by gen_cat.py -- original 48x32 pixel-art cat, 1 bit per pixel.",
        "// Layout: 4 pages x 48 columns, LSB = top pixel of each 8-pixel page (SSD1306 native).",
        "#pragma once",
        "#include <stdint.h>",
        "#include \"progmem.h\"",
        "",
        "#define CAT_W 48",
        "#define CAT_H 32",
        "#define CAT_PAGES 4",
        "#define CAT_BYTES (CAT_W * CAT_PAGES)",
        "",
    ]
    body = "\n".join(fmt(k, g) for k, g in frames.items())
    open("../keymaps/default/cat_frames.h", "w").write("\n".join(header) + body)
    print("wrote cat_frames.h")
