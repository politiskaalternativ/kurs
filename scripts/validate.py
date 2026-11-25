from pathlib import Path
import re
from build import build, ROOT


def check_perspective_choices(path, text):
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    sections = dict(zip(parts[1::2], parts[2::2]))
    heading = "Utforska perspektiv"
    if path.stem != "02" and heading not in sections:
        return
    assert heading in sections, (path, "missing perspective question")
    named_row = r"^- (.+?) – .+$"
    scene = re.findall(named_row, sections["Scen"], re.MULTILINE)
    if path.stem == "02":
        assert {"Amina", "Erik", "Sofia"} <= set(scene), (path, "missing M02 perspective")
    assert scene, (path, "missing perspectives in scene")

    keys = []
    choices = []
    for row in sections[heading].splitlines():
        if row.startswith("- "):
            choice = re.fullmatch(r"- ([A-Z]+)\. (.+?) – .+", row)
            assert choice, (path, "invalid perspective choice", row)
            keys.append(choice[1])
            choices.append(choice[2])
    feedback = re.findall(named_row, sections["Förklaring och återkoppling"], re.MULTILINE)
    assert len(keys) == len(set(keys)), (path, "duplicate choice key", keys)
    assert len(scene) == len(set(scene)), (path, "duplicate perspective", scene)
    assert sorted(scene) == sorted(choices) == sorted(feedback), (path, scene, choices, feedback)


modules = sorted((ROOT / "discovery").glob("*.md"))
assert len(modules) == 6
for i, path in enumerate(modules, 1):
    text = path.read_text(encoding="utf-8")
    assert f"objective: L{i:02d}" in text
    for marker in ["status: draft", "## Scen", "## Utforska"]:
        assert marker in text, (path, marker)
    assert "återkoppling" in text.lower()
    check_perspective_choices(path, text)
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts: continue
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if "://" not in target and not target.startswith("#"):
            assert (path.parent / target.split("#")[0]).exists(), (path, target)
assert (ROOT / "COURSE.md").read_text(encoding="utf-8") == build(), "Rebuild COURSE.md"
assert build().count("## Ämnesbilaga:") == 5
print("PASS: 6 modules, objectives, teaching sections, perspective choices and feedback, local links, 5 subject appendices, reproducible COURSE.md")
