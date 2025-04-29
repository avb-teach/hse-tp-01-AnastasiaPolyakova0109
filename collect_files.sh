#!/bin/bash

input="$1"
out="$2"
dep=""

if [[ "$3" == "--max_depth" ]]; then
	dep="$4"
fi

python3 main.py "$input" "$out" "$dep"