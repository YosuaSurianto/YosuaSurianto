"""Generates the project cards in assets/cards/. Run: python scripts/build_cards.py"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "cards"

W, H = 480, 270
SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, 'SFMono-Regular', Menlo, monospace"

CARDS = [
    {
        "slug": "hydrafit",
        "track": "WEB / FULL-STACK",
        "title": "HydraFit",
        "tagline": "Health and fitness tracking platform",
        "desc": [
            "BMI and weight-progress tracking with Bcrypt auth,",
            "PHPMailer OTP verification and Chart.js analytics.",
            "Native PHP and MySQL, no framework.",
        ],
        "tags": ["PHP", "MySQL", "Chart.js", "JavaScript"],
        "badge": "CAPSTONE PROJECT",
    },
    {
        "slug": "polysui",
        "track": "ON-CHAIN / SUI",
        "title": "PolySui",
        "tagline": "Decentralized betting & governance",
        "desc": [
            "Markets and proposals where every bet, vote and",
            "payout is verifiable on-chain. Move contracts,",
            "no middleman.",
        ],
        "tags": ["Move", "Sui", "React", "TypeScript"],
        "badge": "2ND PLACE · SUI HACKATHON",
        "gold": True,
    },
    {
        "slug": "suiraffle",
        "track": "ON-CHAIN / SUI",
        "title": "SuiRaffle",
        "tagline": "Tamper-proof on-chain raffles",
        "desc": [
            "Native randomness (sui::random), multi-winner",
            "draws via swap_remove, and auto-settlement the",
            "moment the ticket cap is reached.",
        ],
        "tags": ["Move", "Sui", "React 19", "Vite"],
        "badge": "LIVE",
    },
    {
        "slug": "tipfy",
        "track": "ON-CHAIN / MONAD",
        "title": "TipFy",
        "tagline": "Streamer donations that earn yield",
        "desc": [
            "Tips go direct or into a vault staked on Aave V3,",
            "with real-time alerts, overlays and leaderboards",
            "for streamers.",
        ],
        "tags": ["Solidity", "viem", "wagmi", "TanStack"],
        "badge": "LIVE",
    },
    {
        "slug": "novacast",
        "track": "AI / ML",
        "title": "NovaCast",
        "tagline": "Healthcare volume forecasting engine",
        "desc": [
            "Tweedie LightGBM pipeline that beat the LOGEX",
            "SQL baseline by 10.77% relative",
            "(WMAPE 35.97% vs 40.31%).",
        ],
        "tags": ["Python", "LightGBM", "Forecasting"],
        "badge": "-10.77% WMAPE",
    },
    {
        "slug": "aesa",
        "track": "AI / WEB",
        "title": "AESA",
        "tagline": "Content analysis for a game studio",
        "desc": [
            "Analyzes content and audience signals with Gemini",
            "and links every insight back to the source data",
            "it came from. Supabase backend.",
        ],
        "tags": ["Next.js", "Supabase", "Gemini", "TS"],
        "badge": "LIVE",
    },
    {
        "slug": "exp-maua",
        "track": "INTERNSHIP / REMOTE",
        "title": "Full-Stack Developer",
        "tagline": "Maua.ai",
        "desc": [
            "Full-stack work on client apps, web platforms",
            "and games. Currently assigned to the frontend",
            "of a client's game apps.",
        ],
        "tags": ["React Native", "TypeScript", "Firebase"],
        "badge": "JUL 2026 - NOW",
    },
    {
        "slug": "exp-client-games",
        "track": "CLIENT WORK / PRIVATE",
        "title": "Escape-Room Game Apps",
        "tagline": "Offline-first team puzzle games",
        "desc": [
            "Frontend for team escape-room games. Works offline,",
            "syncs results when back online, and loads puzzles",
            "and images from a CMS without a new release.",
        ],
        "tags": ["React Native", "TypeScript", "Firebase"],
        "badge": "NDA · CODE PRIVATE",
        "locked": True,
    },
]


def chip_width(text, size=12):
    return int(len(text) * size * 0.62) + 22


def card_svg(c):
    cyan = "#5EB8FF"
    badge_color = "#FFC857" if c.get("gold") else cyan
    uid = c["slug"].replace("-", "")

    desc = "\n".join(
        f'<text x="28" y="{150 + i * 21}" class="d">{escape(line)}</text>'
        for i, line in enumerate(c["desc"])
    )

    chips, x = [], 28
    for t in c["tags"]:
        w = chip_width(t)
        chips.append(
            f'<g transform="translate({x},222)"><rect width="{w}" height="26" rx="13" class="chip"/>'
            f'<text x="{w / 2}" y="17.5" text-anchor="middle" class="ct">{escape(t)}</text></g>'
        )
        x += w + 8

    badge = ""
    if c.get("badge"):
        bw = chip_width(c["badge"], 10.5) + 6
        icon = ""
        if c.get("locked"):
            icon = (
                f'<g transform="translate(-20,5)" fill="none" stroke="{badge_color}" stroke-width="1.6">'
                '<rect x="0" y="6" width="12" height="9" rx="2"/><path d="M3 6V4a3 3 0 0 1 6 0v2"/></g>'
            )
        badge = (
            f'<g transform="translate({W - 24 - bw},24)">{icon}'
            f'<rect width="{bw}" height="24" rx="6" fill="{badge_color}" fill-opacity=".12" stroke="{badge_color}" stroke-opacity=".6"/>'
            f'<text x="{bw / 2}" y="16" text-anchor="middle" class="b" fill="{badge_color}">{escape(c["badge"])}</text></g>'
        )

    title_size = 30 if len(c["title"]) <= 14 else 25

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(c['title'])}: {escape(c['tagline'])}">
<title>{escape(c['title'])}: {escape(c['tagline'])}</title>
<defs>
  <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0D1526"/><stop offset="1" stop-color="#070B14"/>
  </linearGradient>
  <radialGradient id="glow{uid}" cx="0.9" cy="0" r="0.8">
    <stop offset="0" stop-color="{cyan}" stop-opacity=".18"/><stop offset="1" stop-color="{cyan}" stop-opacity="0"/>
  </radialGradient>
</defs>
<style>
  .k {{ font: 700 11px {MONO}; letter-spacing: 2px; fill: {cyan}; }}
  .t {{ font: 800 {title_size}px {SANS}; fill: #EAF4FF; }}
  .g {{ font: 600 15px {SANS}; fill: #A9C7E8; }}
  .d {{ font: 400 13.5px {SANS}; fill: #7F93B2; }}
  .b {{ font: 700 10.5px {MONO}; letter-spacing: 1px; }}
  .chip {{ fill: #5EB8FF; fill-opacity: .08; stroke: #5EB8FF; stroke-opacity: .35; }}
  .ct {{ font: 600 12px {MONO}; fill: #CFE6FF; }}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#bg{uid})" stroke="#1B2A44" stroke-width="1.5"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#glow{uid})"/>
<rect x="28" y="1" width="96" height="2" rx="1" fill="{cyan}"/>
<path d="M28 34 l6 -9 h-4 l3 -7" fill="none" stroke="{cyan}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
<text x="44" y="34" class="k">{escape(c['track'])}</text>
{badge}
<text x="28" y="86" class="t">{escape(c['title'])}</text>
<text x="28" y="114" class="g">{escape(c['tagline'])}</text>
{desc}
{''.join(chips)}
</svg>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CARDS:
        (OUT / f"{c['slug']}.svg").write_text(card_svg(c), encoding="utf-8")
        print("wrote", c["slug"])


if __name__ == "__main__":
    main()
