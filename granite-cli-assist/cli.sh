#!/bin/bash
API_URL=${API_URL:-http://127.0.0.1:8000}
HIST_FILE=${HIST_FILE:-$HOME/.granite_cli_history}
last=""

function clip_last(){
    command -v xclip >/dev/null && echo -n "$last" | xclip -selection clipboard
}

function stash_last(){
    python - <<'PY'
import sys
from granite_cli_assist import snippet
snippet.stash(sys.stdin.read())
PY
}

function list_snippets(){
    ls -1 "$HOME/granite-snippets" 2>/dev/null | fzf
}

function search_history(){
    python - <<'PY'
import sys
from granite_cli_assist import chat_history
res = chat_history.search(sys.argv[1])
for k,v in res.items():
    print(f"{k}: {v}")
PY
}

while read -rp "‣ " input; do
    case "$input" in
        /exit) break;;
        /clip) clip_last;;
        /stash) echo "$last" | stash_last;;
        /list) list_snippets;;
        /search*) term=${input#/search }; search_history "$term";;
        *) resp=$(curl -s -X POST "$API_URL/generate" -H 'Content-Type: application/json' -d "{\"prompt\":\"$input\"}"); last=$(echo "$resp" | jq -r .response); echo "$last";;
    esac
done
