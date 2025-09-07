#!/bin/bash
# Generic test runner for ChallengeLab challenges

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

# Check if tests directory exists
if [ ! -d "/app/tests" ]; then
    print_status $RED "Error: tests directory not found!"
    exit 1
fi

# Run tests
print_status $YELLOW "Running tests for challenge..."

test_count=0
passed_count=0
failed_count=0

# Find all test files
for test_file in /app/tests/*.txt; do
    if [ -f "$test_file" ]; then
        test_name=$(basename "$test_file" .txt)
        
        # Skip if it's not an input file
        if [[ "$test_name" != *"input"* ]]; then
            continue
        fi
        
        # Find corresponding expected output file
        expected_file="/app/tests/${test_name/input/expected}.txt"
        if [ ! -f "$expected_file" ]; then
            print_status $RED "Warning: Expected output file not found for $test_name"
            continue
        fi
        
        test_count=$((test_count + 1))
        
        print_status $YELLOW "Running test: $test_name"
        
        # Run the challenge with input and capture output
        actual_output=$(cat "$test_file" | /app/challenge.sh)
        expected_output=$(cat "$expected_file")
        
        # Compare outputs
        if [ "$actual_output" = "$expected_output" ]; then
            print_status $GREEN "✓ Test $test_name PASSED"
            passed_count=$((passed_count + 1))
        else
            print_status $RED "✗ Test $test_name FAILED"
            print_status $RED "Expected:"
            echo "$expected_output"
            print_status $RED "Actual:"
            echo "$actual_output"
            failed_count=$((failed_count + 1))
        fi
    fi
done

# Summary
echo ""
print_status $YELLOW "Test Summary:"
echo "Total tests: $test_count"
print_status $GREEN "Passed: $passed_count"
if [ $failed_count -gt 0 ]; then
    print_status $RED "Failed: $failed_count"
    exit 1
else
    print_status $GREEN "Failed: $failed_count"
    print_status $GREEN "All tests passed!"
    exit 0
fi
