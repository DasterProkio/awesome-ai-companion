#!/usr/bin/env python3
"""Render a self-hosted star-history SVG from GitHub's stargazer timestamps."""

import datetime as dt
import json
import os
import pathlib
import urllib.parse
import urllib.request
from collections import Counter
import math
from xml.sax.saxutils import escape

OWNER = os.environ.get("STAR_HISTORY_OWNER", "DasterProkio")
REPO = os.environ.get("STAR_HISTORY_REPO", "awesome-ai-companion")
OUTPUT = pathlib.Path(os.environ.get("STAR_HISTORY_OUTPUT", "assets/star-history.svg"))


def next_page_url(link_header):
    for part in link_header.split(","):
        target, *parameters = part.split(";")
        if any(parameter.strip() == 'rel="next"' for parameter in parameters):
            return target.strip().strip("<>")
    return None


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
        url = next_page_url(link)
    dates = []
    for item in stars:
        value = item.get("starred_at")
        if value:
            dates.append(dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date())
    return sorted(dates)


def render(dates):
    width, height = 960, 480
    left, right, top, bottom = 76, 36, 112, 76
    chart_w, chart_h = width - left - right, height - top - bottom
    count = len(dates)
    today = dt.date.today()
    start = dates[0] - dt.timedelta(days=1) if dates else today
    span = max((today - start).days, 1)
    rough_step = max(count, 1) / 5
    magnitude = 10 ** math.floor(math.log10(max(rough_step, 1)))
    normalized = rough_step / magnitude
    nice_factor = 1 if normalized <= 1 else 2 if normalized <= 2 else 2.5 if normalized <= 2.5 else 5 if normalized <= 5 else 10
    y_step = nice_factor * magnitude
    y_max = max(y_step, math.ceil(max(count, 1) / y_step) * y_step)
    daily = Counter(dates)
    points = []
    cumulative = 0
    for offset in range(span + 1):
        date = start + dt.timedelta(days=offset)
        cumulative += daily[date]
        x = left + ((date - start).days / span) * chart_w
        y = top + chart_h - (cumulative / y_max) * chart_h
        points.append((x, y))
    path = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        middle = (x0 + x1) / 2
        path.append(f"C {middle:.1f} {y0:.1f}, {middle:.1f} {y1:.1f}, {x1:.1f} {y1:.1f}")
    line = " ".join(path)
    area = f"M {left:.1f} {top + chart_h:.1f} L {points[0][0]:.1f} {points[0][1]:.1f} " + " ".join(path[1:]) + f" L {points[-1][0]:.1f} {top + chart_h:.1f} Z"
    tick_count = min(6, span + 1)
    tick_offsets = sorted({round(index * span / max(tick_count - 1, 1)) for index in range(tick_count)})
    date_ticks = []
    for offset in tick_offsets:
        date = start + dt.timedelta(days=offset)
        x = left + offset / span * chart_w
        if span <= 120:
            label = date.strftime("%b %-d")
        elif span <= 730:
            label = date.strftime("%b %Y")
        else:
            label = str(date.year)
        date_ticks.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + chart_h}"/><text x="{x:.1f}" y="{top + chart_h + 28}" text-anchor="middle" class="axis">{label}</text>')
    value_ticks = []
    value = 0.0
    while value <= y_max + y_step / 10:
        y = top + chart_h - (value / y_max) * chart_h
        label = str(int(value)) if float(value).is_integer() else f"{value:g}"
        value_ticks.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_w}" y2="{y:.1f}"/><text x="{left - 14}" y="{y + 4:.1f}" text-anchor="end" class="axis">{label}</text>')
        value += y_step
    last = points[-1]
    latest = dates[-1].isoformat() if dates else "No stars yet"
    title = escape(f"{OWNER}/{REPO} · Star History")
    subtitle = escape(f"Updated {today.isoformat()} · latest star {latest}")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title><desc id="desc">{count} GitHub stars over time, updated by GitHub Actions.</desc>
  <defs>
    <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#58a6ff" stop-opacity=".24"/><stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="8" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
  <text x="40" y="42" class="title">Star History</text><text x="40" y="64" class="subtitle">{subtitle}</text>
  <g transform="translate({width - 112} 27)"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.193a.75.75 0 0 1-1.088.79L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z" fill="#e3b341"/></g>
  <text x="{width - 40}" y="42" text-anchor="end" class="count">{count}</text><text x="{width - 40}" y="61" text-anchor="end" class="count-label">GitHub stars</text>
  <g transform="translate({left} {top - 24})"><line x1="0" y1="0" x2="24" y2="0" stroke="#58a6ff" stroke-width="4" stroke-linecap="round"/><circle cx="24" cy="0" r="3" fill="#58a6ff"/><text x="34" y="4" class="legend">{escape(OWNER + '/' + REPO)}</text></g>
  <g class="grid">{''.join(value_ticks)}{''.join(date_ticks)}</g>
  <path d="{area}" fill="url(#fill)"/><path d="{line}" fill="none" stroke="#58a6ff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{last[0]:.1f}" cy="{last[1]:.1f}" r="5" fill="#0d1117" stroke="#58a6ff" stroke-width="3"/>
  <text x="{left}" y="{top + 18}" class="axis-title">STARS</text><text x="{left + chart_w / 2}" y="{top + chart_h + 54}" text-anchor="middle" class="axis-title">DATE</text>
  <style>.title{{font:600 22px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#f0f6fc}}.subtitle,.footer{{font:12px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#8b949e}}.legend{{font:12px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#c9d1d9}}.count{{font:700 27px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#f0f6fc}}.count-label,.axis,.axis-title{{font:11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#8b949e;letter-spacing:.04em}}.axis-title{{font-weight:600;fill:#c9d1d9}}.grid line{{stroke:#30363d;stroke-opacity:.9;stroke-dasharray:3 6}}</style>
</svg>\n'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render(fetch_stars())
