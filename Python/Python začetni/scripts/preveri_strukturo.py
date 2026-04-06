from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"^\d{2}_.+")
required = [
    "01_ucni_nacrt.md",
    "02_ucni_list.md",
    "03_resitev.md",
    "04_dodatne_naloge.md",
    "05_domaca_naloga.md",
    "08_uciteljski_scenarij_ure.md",
]

sklopi = sorted([p for p in root.iterdir() if p.is_dir() and pattern.match(p.name)])
missing_report = []

for sklop in sklopi:
    missing = [name for name in required if not (sklop / name).exists()]
    if missing:
        missing_report.append((sklop.name, missing))

print(f"Najdenih sklopov: {len(sklopi)}")

if missing_report:
    print("\nManjkajoče datoteke:")
    for sklop_name, missing in missing_report:
        print(f"- {sklop_name}: {', '.join(missing)}")
    sys.exit(1)

print("Vsi sklopi imajo obvezno Markdown strukturo.")
