# Reverse String Challenge

## Description
Create a script that reads lines from stdin and outputs each line with its characters reversed.

## Instructions
1. Edit `challenge.sh` to implement your solution
2. Your script should read from stdin and write to stdout
3. Each line should be reversed character by character
4. Run `challengelab test reverse-string` to test your solution

## Example
```bash
echo "hello" | ./challenge.sh
# Output: olleh
```

## Test Cases
The challenge includes the following test cases:
- "hello world" → "dlrow olleh"
- "challenge" → "egnellahc"
- "docker" → "rekcod"
- "bash scripting" → "gnitpircs hsab"
- "12345" → "54321"

## Hints
- Use the `rev` command or implement your own string reversal logic
- Handle empty lines appropriately
- Ensure your solution works with multi-line input

## Solution Approach
You can solve this challenge in several ways:
1. Use the built-in `rev` command
2. Implement a custom reversal function in bash
3. Use other Unix utilities creatively

Good luck!
