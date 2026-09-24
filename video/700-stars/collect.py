"""Builds wall.json (every entry in the list, for the overview scene) from the READMEs.

    python3 collect.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
SKIP = {"Contents", "Related Lists", "Contributing", "Footnotes"}
tl = json.loads((HERE / "timeline.json").read_text())
new_names = {p["name"] for p in tl["projects"]}
hidden = set(tl.get("wallHidden", []))

en_secs = [l[3:].strip() for l in (ROOT / "README.md").read_text().splitlines() if l.startswith("## ")]
zh_secs = [l[3:].strip() for l in (ROOT / "README.zh-CN.md").read_text().splitlines() if l.startswith("## ")]
zh_of = dict(zip(en_secs, zh_secs))

sec, names, cats = None, [], {}
for line in (ROOT / "README.md").read_text().splitlines():
    if line.startswith("## "):
        sec = line[3:].strip()
        continue
    m = re.match(r"- \[([^\]]+)\]\(http", line)
    if not m or sec in SKIP:
        continue
    name = m.group(1)
    cats[sec] = cats.get(sec, 0) + 1
    if not any(name == h or name.startswith(h + " ") for h in hidden):
        names.append({"name": name, "cat": len(cats) - 1,
                      "new": any(name == n or name.startswith(n + " ") for n in new_names)})

out = {"total": sum(cats.values()),
       "categories": [{"en": k, "zh": zh_of.get(k, k), "count": v} for k, v in cats.items()],
       "names": names}
(HERE / "wall.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print(f"{out['total']} entries in {len(cats)} categories, {len(names)} shown, "
      f"{sum(n['new'] for n in names)} highlighted as new")
