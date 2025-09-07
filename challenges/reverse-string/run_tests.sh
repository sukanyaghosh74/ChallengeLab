#!/bin/bash
# Test runner for reverse-string challenge

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Check if challenge.sh exists
if [ ! -f "/app/challenge.sh" ]; then
    print_status $RED "Error: challenge.sh not found!"
    exit 1
fi

# Make challenge.sh executable
chmod +x /app/challenge.sh

# Run the test
print_status $YELLOW "Running reverse-string challenge test..."

# Get input and expected output
input=$(cat /app/tests/input.txt)
expected=$(cat /app/tests/expected.txt)

# Run the challenge
actual=$(echo "$input" | /app/challenge.sh)

# Compare outputs
if [ "$actual" = "$expected" ]; then
    print_status $GREEN "✓ Test PASSED"
    print_status $GREEN "All tests passed!"
    exit 0
else
    print_status $RED "✗ Test FAILED"
    print_status $RED "Expected:"
    echo "$expected"
    print_status $RED "Actual:"
    echo "$actual"
    exit 1
fi
