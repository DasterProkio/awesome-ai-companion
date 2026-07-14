#!/usr/bin/env python3
"""Render a self-hosted star-history SVG from GitHub's stargazer timestamps."""

import datetime as dt
import json
import os
import pathlib
import urllib.parse
import urllib.request
from collections import Counter
from xml.sax.saxutils import escape

OWNER = os.environ.get("STAR_HISTORY_OWNER", "DasterProkio")
REPO = os.environ.get("STAR_HISTORY_REPO", "awesome-ai-companion")
OUTPUT = pathlib.Path(os.environ.get("STAR_HISTORY_OUTPUT", "assets/star-history.svg"))


def fetch_stars():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required")
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/stargazers?per_page=100"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github.star+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-ai-companion-star-history",
        },
    )
    stars = []
    while url:
        request.full_url = url
        with urllib.request.urlopen(request, timeout=30) as response:
            stars.extend(json.load(response))
            link = response.headers.get("Link", "")
        url = next(
            (part.split(";", 1)[0].strip("<>") for part in link.split(",") if 'rel="next"' in part),
            None,
        )
    dates = []
    for item in stars:
        value = item.get("starred_at")
        if value:
            dates.append(dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date())
    return sorted(dates)


def render(dates):
    width, height = 960, 460
    left, right, top, bottom = 76, 36, 76, 72
    chart_w, chart_h = width - left - right, height - top - bottom
    count = len(dates)
    today = dt.date.today()
    start = dates[0] - dt.timedelta(days=1) if dates else today
    span = max((today - start).days, 1)
    daily = Counter(dates)
    points = []
    cumulative = 0
    for offset in range(span + 1):
        date = start + dt.timedelta(days=offset)
        cumulative += daily[date]
        x = left + ((date - start).days / span) * chart_w
        y = top + chart_h - (cumulative / max(count, 1)) * chart_h
        points.append((x, y))
    path = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        middle = (x0 + x1) / 2
        path.append(f"C {middle:.1f} {y0:.1f}, {middle:.1f} {y1:.1f}, {x1:.1f} {y1:.1f}")
    line = " ".join(path)
    area = f"M {left:.1f} {top + chart_h:.1f} L {points[0][0]:.1f} {points[0][1]:.1f} " + " ".join(path[1:]) + f" L {points[-1][0]:.1f} {top + chart_h:.1f} Z"
    year_labels = []
    for year in range(start.year, today.year + 1):
        date = dt.date(year, 1, 1)
        x = left + max(0, (date - start).days) / span * chart_w
        year_labels.append(f'<text x="{x:.1f}" y="{height - 30}" class="axis">{year}</text>')
    last = points[-1]
    latest = dates[-1].isoformat() if dates else "No stars yet"
    title = escape(f"{OWNER}/{REPO} · Star History")
    subtitle = escape(f"Updated {today.isoformat()} · latest star {latest}")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title><desc id="desc">{count} GitHub stars over time, updated by GitHub Actions.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#111827"/><stop offset="1" stop-color="#24143d"/></linearGradient>
    <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#f9c74f" stop-opacity=".42"/><stop offset="1" stop-color="#f9c74f" stop-opacity="0"/></linearGradient>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#f9c74f"/><stop offset="1" stop-color="#f9844a"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="4" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="{width}" height="{height}" rx="24" fill="url(#bg)"/>
  <g transform="translate(40 27)"><path d="M12 1.8l3.05 6.18 6.82 1-4.94 4.81 1.17 6.79L12 17.38l-6.1 3.2 1.17-6.79-4.94-4.81 6.82-1L12 1.8z" fill="#f9c74f"/><circle cx="12" cy="12" r="16" fill="none" stroke="#f9c74f" stroke-opacity=".18" stroke-width="2"/></g>
  <text x="80" y="46" class="title">{title}</text><text x="80" y="66" class="subtitle">{subtitle}</text>
  <text x="{width - 40}" y="48" text-anchor="end" class="count">{count}</text><text x="{width - 40}" y="68" text-anchor="end" class="count-label">STARS</text>
  <g class="grid"><line x1="{left}" y1="{top}" x2="{left}" y2="{top + chart_h}"/><line x1="{left}" y1="{top + chart_h}" x2="{left + chart_w}" y2="{top + chart_h}"/><line x1="{left}" y1="{top + chart_h * .5}" x2="{left + chart_w}" y2="{top + chart_h * .5}"/></g>
  <path d="{area}" fill="url(#fill)"/><path d="{line}" fill="none" stroke="url(#line)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)"/>
  <circle cx="{last[0]:.1f}" cy="{last[1]:.1f}" r="7" fill="#fff3bf" stroke="#f9844a" stroke-width="3"/>
  <text x="{left - 14}" y="{top + 5}" text-anchor="end" class="axis">{count}</text><text x="{left - 14}" y="{top + chart_h * .5 + 5}" text-anchor="end" class="axis">{count // 2}</text><text x="{left - 14}" y="{top + chart_h + 5}" text-anchor="end" class="axis">0</text>
  {''.join(year_labels)}
  <text x="{width - 40}" y="{height - 24}" text-anchor="end" class="footer">Generated from GitHub stargazers · github.com/{OWNER}/{REPO}</text>
  <style>.title{{font:600 22px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#fff}}.subtitle,.footer{{font:12px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#a5b4fc}}.count{{font:700 30px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#f9c74f}}.count-label,.axis{{font:11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#94a3b8;letter-spacing:.08em}}.grid line{{stroke:#94a3b8;stroke-opacity:.18;stroke-dasharray:4 8}}</style>
</svg>\n'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render(fetch_stars())
