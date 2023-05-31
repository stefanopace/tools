#!/usr/bin/env bash

frg_preview () {
output="$1"
IFS=':' command eval 'output=($output)'
fname="${output[0]}"
row="${output[1]}"
start_line=$(( $row - (($FZF_PREVIEW_LINES - 1) / 2) ))
end_line=$(( $start_line + $FZF_PREVIEW_LINES - 2 ))
if [ $start_line -le 0 ]; then
    start_line=0
    end_line=$(( $FZF_PREVIEW_LINES - 1 ))
fi
batcat --style="numbers,header" --color=always --highlight-line="$row" --line-range "$start_line:$end_line" "$fname"
}

export -f frg_preview

INITIAL_QUERY=""
RG_PREFIX="rg --column --line-number --no-heading --color=always --smart-case "
FZF_DEFAULT_COMMAND="$RG_PREFIX '$INITIAL_QUERY'" \
fzf --bind "change:reload:$RG_PREFIX {q} || true" \
    --ansi --phony --query "$INITIAL_QUERY" \
    --layout=reverse --preview-window 'down' --preview 'frg_preview {}'
