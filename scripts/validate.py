from pathlib import Path
import re
from build import build, ROOT
modules = sorted((ROOT / "discovery").glob("*.md"))
assert len(modules) == 6
for i, path in enumerate(modules, 1):
    text = path.read_text()
    assert f"objective: L{i:02d}" in text
    for marker in ["status: draft", "## Scen", "## Utforska"]:
        assert marker in text, (path, marker)
    assert "återkoppling" in text.lower()
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts: continue
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if "://" not in target and not target.startswith("#"):
            assert (path.parent / target.split("#")[0]).exists(), (path, target)
assert (ROOT / "COURSE.md").read_text() == build(), "Rebuild COURSE.md"
assert build().count("## Ämnesbilaga:") == 5
print("PASS: 6 modules, objectives, teaching sections, local links, 5 source snapshots, reproducible COURSE.md")
