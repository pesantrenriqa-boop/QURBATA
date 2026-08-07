from pathlib import Path
import csv

root = Path(".")
master_path = root / "content/qwo/production/generated/MASTER-QURAN-OBJECTS-V1.csv"
foundation_path = root / "content/qwo/production/generated/JILID-1-FOUNDATION-OBJECTS-V2.csv"
output_path = root / "content/qwo/production/generated/MASTER-QURAN-OBJECTS-WITH-FOUNDATION-V2.csv"

fieldnames = [
    "CanonicalKey",
    "ObjectType",
    "Text",
    "SourceRef",
    "WordCount",
]

objects: dict[str, dict[str, str]] = {}

for path in (master_path, foundation_path):
    if not path.is_file():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            key = row["CanonicalKey"]
            objects.setdefault(
                key,
                {field: row.get(field, "") for field in fieldnames},
            )

output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(objects.values())

type_counts: dict[str, int] = {}

for row in objects.values():
    object_type = row["ObjectType"]
    type_counts[object_type] = type_counts.get(object_type, 0) + 1

print(f"TOTAL_OBJECTS={len(objects)}")
for object_type in sorted(type_counts):
    print(f"{object_type}={type_counts[object_type]}")
print(f"OUTPUT={output_path}")
