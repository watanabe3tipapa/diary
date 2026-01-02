#!/usr/bin/env bash
set -euo pipefail
DIR=${1:-diary}
DATE=${2:-$(date -u +%F)}
TEMPLATE=${3:-templates/diary.md}
mkdir -p "$DIR"
TARGET="$DIR/$DATE.md"
if [ -e "$TARGET" ]; then
  echo "Exists: $TARGET" && exit 0
fi
if [ -f "$TEMPLATE" ]; then
  sed "s/{{date}}/$DATE/g" "$TEMPLATE" > "$TARGET"
else
  echo "# $DATE" > "$TARGET"
fi
echo "Created: $TARGET"
${EDITOR:-:} "$TARGET"
