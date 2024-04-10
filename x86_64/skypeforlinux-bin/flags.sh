#!/bin/bash

FLAGS_FILE="${XDG_CONFIG_HOME:-"${HOME}/.config"}/@NAME@-flags.conf"

[ -f "${FLAGS_FILE}" ] || exec '@EXEC@' "$@"

mapfile -t FLAGS_LINES < "${FLAGS_FILE}"
declare -a FLAGS

for line in "${FLAGS_LINES[@]}"; do
    [[ "${line}" =~ ^[[:space:]]*#.* ]] && continue
    FLAGS+=("${line}")
done

exec '@EXEC@' "${FLAGS[@]}" "$@"
