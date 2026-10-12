"""Draw value-curve.svg from the scores in README.md. Standard library only.

Run: python3 supporting/value-curve/make_value_curve.py
Score codes: a number = score; "i" suffix = interpretation; None = unknown (gap).
"""
from pathlib import Path

FACTORS = [
    ("F1", "Listings in", "one search"),
    ("F2", "Landlord", "checks"),
    ("F3", "Property", "checks"),
    ("F4", "Payment held", "to move-in"),
    ("F5", "English", "access"),
    ("F6", "Student", "filters"),
    ("F7", "Low tenant", "fee"),
    ("F8", "Cross-source", "discovery"),
    ("F9", "Arrival-date", "planning"),
]

# Keep in sync with the score table in README.md.
SERIES = [
    # name, colour, marker, scores F1..F9
    ("Idealista", "#2a78d6", "circle",
     [None, None, None, "2", None, None, "3i", "0i", None]),
    ("Spotahome", "#eb6834", "square",
     ["4", "3i", "2", "4", "4", "3", None, "0i", "2"]),
    ("HousingAnywhere", "#1baf7a", "triangle",
     ["4", "3", "1", "4", "5", "4", "2", "0i", "2"]),
]
TARGET = ("Our platform (hypothetical target)", "#6250d6", "diamond",
          ["4", "4", "2", "0", "5", "5", "5", "5", "5"])

W, H = 1000, 650
L, R, T, B = 70, 30, 215, 530  # plot box: left, right, top, bottom (y px)
INK, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
OFFSETS = [-12, -4, 4, 12]


def x_of(i):
    return L + (i + 0.5) * (W - L - R) / len(FACTORS)


def y_of(v):
    return B - v * (B - T) / 5


def marker(shape, x, y, colour, hollow=False, r=6):
    fill = SURF if hollow else colour
    style = f'fill="{fill}" stroke="{colour}" stroke-width="2"'
    if shape == "circle":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" {style}/>'
    if shape == "square":
        return f'<rect x="{x - r:.1f}" y="{y - r:.1f}" width="{2 * r}" height="{2 * r}" {style}/>'
    if shape == "triangle":
        pts = f"{x:.1f},{y - r - 1:.1f} {x + r + 1:.1f},{y + r:.1f} {x - r - 1:.1f},{y + r:.1f}"
        return f'<polygon points="{pts}" {style}/>'
    pts = f"{x:.1f},{y - r - 2:.1f} {x + r + 2:.1f},{y:.1f} {x:.1f},{y + r + 2:.1f} {x - r - 2:.1f},{y:.1f}"
    return f'<polygon points="{pts}" {style}/>'


def series_svg(k, name, colour, shape, scores, dashed=False):
    out, run = [], []
    dash = ' stroke-dasharray="7 5"' if dashed else ""

    def flush():
        if len(run) > 1:
            pts = " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in run)
            out.append(f'<polyline points="{pts}" fill="none" stroke="{colour}" stroke-width="2"{dash}/>')
        run.clear()

    for i, s in enumerate(scores):
        if s is None:
            flush()
            continue
        run.append((x_of(i) + OFFSETS[k], y_of(int(s[0])), s))
    flush()
    for i, s in enumerate(scores):
        if s is None:
            continue
        x, y = x_of(i) + OFFSETS[k], y_of(int(s[0]))
        out.append(marker(shape, x, y, colour, hollow=dashed))
        if s.endswith("i"):  # interpretation: white centre dot
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{SURF}"/>')
    return out


def legend_item(x, y, shape, colour, label, dashed=False, interp=False):
    dash = ' stroke-dasharray="7 5"' if dashed else ""
    parts = [f'<line x1="{x}" y1="{y}" x2="{x + 34}" y2="{y}" stroke="{colour}" stroke-width="2"{dash}/>',
             marker(shape, x + 17, y, colour, hollow=dashed)]
    if interp:
        parts.append(f'<circle cx="{x + 17}" cy="{y}" r="2.6" fill="{SURF}"/>')
    parts.append(f'<text x="{x + 42}" y="{y + 4}" font-size="13" fill="{INK}">{label}</text>')
    return parts


def build():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'font-family="Helvetica, Arial, sans-serif" role="img" aria-labelledby="t d">',
         '<title id="t">Strategy canvas: student housing in Madrid</title>',
         '<desc id="d">Offering level 0 to 5 on nine factors for Idealista, Spotahome and HousingAnywhere '
         '(scored from sources dated 2026-10-12) and our platform (hypothetical target, dashed). '
         'Gaps are unknown scores, not zero. Agent comparison unavailable: evidence missing. Full table in README.md.</desc>',
         f'<rect width="{W}" height="{H}" fill="{SURF}"/>',
         f'<text x="{L}" y="34" font-size="20" font-weight="bold" fill="{INK}">Strategy canvas: housing options for an international student in Madrid</text>',
         f'<text x="{L}" y="56" font-size="13" fill="{MUTED}">Offering level 0–5 per factor. Competitor scores from their own sites, accessed 2026-10-12. '
         'Our platform is a target, not a measured level.</text>']
    # legend: series
    s += legend_item(L, 86, "circle", SERIES[0][1], "Idealista")
    s += legend_item(L + 150, 86, "square", SERIES[1][1], "Spotahome")
    s += legend_item(L + 310, 86, "triangle", SERIES[2][1], "HousingAnywhere")
    s += legend_item(L + 500, 86, "diamond", TARGET[1], "Our platform: hypothetical target level, not measured", dashed=True)
    # legend: how to read scores
    s += [f'<text x="{L}" y="120" font-size="13" font-weight="bold" fill="{INK}">How to read</text>',
          f'<line x1="{L + 100}" y1="116" x2="{L + 134}" y2="116" stroke="{MUTED}" stroke-width="2"/>',
          marker("circle", L + 117, 116, MUTED),
          f'<text x="{L + 142}" y="120" font-size="13" fill="{INK}">Solid, filled = sourced competitor score</text>',
          marker("circle", L + 437, 116, MUTED), f'<circle cx="{L + 437}" cy="116" r="2.6" fill="{SURF}"/>',
          f'<text x="{L + 450}" y="120" font-size="13" fill="{INK}">White centre = interpreted score (source incomplete)</text>',
          f'<line x1="{L + 100}" y1="142" x2="{L + 134}" y2="142" stroke="{MUTED}" stroke-width="2" stroke-dasharray="7 5"/>',
          marker("diamond", L + 117, 142, MUTED, hollow=True),
          f'<text x="{L + 142}" y="146" font-size="13" fill="{INK}">Dashed, hollow = target level (HYPOTHESIS)</text>',
          f'<text x="{L + 437}" y="146" font-size="13" fill="{INK}" text-anchor="middle">?</text>',
          f'<text x="{L + 450}" y="146" font-size="13" fill="{INK}">Line break / "? Name" = unknown, no source (not 0)</text>',
          f'<rect x="{L}" y="158" width="{W - L - R}" height="24" rx="4" fill="none" stroke="{MUTED}" stroke-width="1" stroke-dasharray="4 3"/>',
          f'<text x="{L + 10}" y="175" font-size="13" fill="{INK}"><tspan font-weight="bold">Agent: comparison unavailable, evidence missing.</tspan> '
          'Not plotted because no source describes agents\' offer. This does not mean agents score 0.</text>']
    # grid and y axis
    for v in range(6):
        y = y_of(v)
        s.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - R}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{L - 12}" y="{y + 4:.1f}" font-size="12" fill="{MUTED}" text-anchor="end">{v}</text>')
    s.append(f'<text x="22" y="{(T + B) / 2:.0f}" font-size="12" fill="{MUTED}" text-anchor="middle" '
             f'transform="rotate(-90 22 {(T + B) / 2:.0f})">Offering level (0 = none, 5 = high)</text>')
    # x labels and unknown notes
    for i, (code, a, b) in enumerate(FACTORS):
        x = x_of(i)
        s.append(f'<text x="{x:.1f}" y="{B + 24}" font-size="13" fill="{INK}" text-anchor="middle">{a}</text>')
        s.append(f'<text x="{x:.1f}" y="{B + 40}" font-size="13" fill="{INK}" text-anchor="middle">{b}</text>')
        s.append(f'<text x="{x:.1f}" y="{B + 56}" font-size="11" fill="{MUTED}" text-anchor="middle">{code}</text>')
        unknown = [n for n, _, _, sc in SERIES if sc[i] is None]
        for j, n in enumerate(unknown):
            s.append(f'<text x="{x:.1f}" y="{B + 78 + 14 * j}" font-size="11" fill="{MUTED}" '
                     f'text-anchor="middle">? {n}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="11" fill="{MUTED}">"? Name" = unknown for that option. '
             'Factor definitions, every score, its basis and source: supporting/value-curve/README.md</text>')
    # series (target last so it sits on top)
    for k, (n, c, m, sc) in enumerate(SERIES):
        s += series_svg(k, n, c, m, sc)
    s += series_svg(3, *TARGET, dashed=True)
    s.append("</svg>")
    return "\n".join(s) + "\n"


if __name__ == "__main__":
    out = Path(__file__).with_name("value-curve.svg")
    out.write_text(build(), encoding="utf-8")
    print(f"wrote {out}")
