#!/usr/bin/env python3
"""
Usage:
  python scripts/create_diary.py [--dir diary] [--date YYYY-MM-DD] [--template templates/diary.md]
Creates YYYY-MM-DD.md in target dir if not exists and opens with $EDITOR if available.
"""
import argparse
from datetime import datetime
from pathlib import Path
import os
import subprocess
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", default="diary")
    p.add_argument("--date", default=None)
    p.add_argument("--template", default="templates/diary.md")
    args = p.parse_args()

    date_str = args.date or datetime.utcnow().date().isoformat()
    target_dir = Path(args.dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{date_str}.md"

    if target_file.exists():
        print(f"Exists: {target_file}")
        sys.exit(0)

    template_path = Path(args.template)
    if template_path.exists():
        content = template_path.read_text()
        content = content.replace("{{date}}", date_str)
    else:
        content = f"# {date_str}\n\n"

    target_file.write_text(content)
    print(f"Created: {target_file}")

    editor = os.environ.get("EDITOR")
    if editor:
        subprocess.run([editor, str(target_file)])
    else:
        print("No $EDITOR set; file created but not opened.")

if __name__ == "__main__":
    main()
