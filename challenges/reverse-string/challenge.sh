#!/bin/bash
# Challenge: Reverse String
# Description: Read lines from stdin and output each line reversed

# Read each line from stdin and reverse it
while IFS= read -r line; do
    # Reverse the line using rev command
    echo "$line" | rev
done
