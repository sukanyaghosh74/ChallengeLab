#!/bin/bash
# ChallengeLab Installation Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_status $BLUE "ChallengeLab Installation Script"
echo "=================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    print_status $RED "Error: Python 3 is required but not installed."
    print_status $YELLOW "Please install Python 3.8+ and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    print_status $RED "Error: Python 3.8+ is required, but you have Python $python_version"
    exit 1
fi

print_status $GREEN "✓ Python $python_version found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    print_status $RED "Error: pip3 is required but not installed."
    print_status $YELLOW "Please install pip3 and try again."
    exit 1
fi

print_status $GREEN "✓ pip3 found"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_status $RED "Error: Docker is required but not installed."
    print_status $YELLOW "Please install Docker and try again."
    exit 1
fi

print_status $GREEN "✓ Docker found"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_status $RED "Error: Docker Compose is required but not installed."
    print_status $YELLOW "Please install Docker Compose and try again."
    exit 1
fi

print_status $GREEN "✓ Docker Compose found"

# Install Python dependencies
print_status $YELLOW "Installing Python dependencies..."
pip3 install -r requirements.txt

# Install ChallengeLab
print_status $YELLOW "Installing ChallengeLab..."
pip3 install -e .

# Verify installation
print_status $YELLOW "Verifying installation..."
if command -v challengelab &> /dev/null; then
    print_status $GREEN "✓ ChallengeLab CLI installed successfully"
else
    print_status $RED "Error: ChallengeLab CLI not found after installation"
    exit 1
fi

# Test the installation
print_status $YELLOW "Testing installation..."
challengelab --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_status $GREEN "✓ ChallengeLab CLI is working"
else
    print_status $RED "Error: ChallengeLab CLI is not working properly"
    exit 1
fi

# Build Docker images for existing challenges
print_status $YELLOW "Building Docker images for challenges..."
if [ -d "challenges" ]; then
    for challenge in challenges/*/; do
        if [ -d "$challenge" ]; then
            challenge_name=$(basename "$challenge")
            print_status $YELLOW "Building image for challenge: $challenge_name"
            docker build -f docker/Dockerfile.base -t "challengelab-$challenge_name:latest" "$challenge" || {
                print_status $RED "Warning: Failed to build image for $challenge_name"
            }
        fi
    done
fi

print_status $GREEN "Installation completed successfully!"
echo ""
print_status $BLUE "Quick Start:"
echo "1. List challenges: challengelab list"
echo "2. Create a challenge: challengelab init my-challenge"
echo "3. Test a challenge: challengelab test reverse-string"
echo "4. Run a challenge: echo 'hello' | challengelab run reverse-string --input 'hello'"
echo ""
print_status $BLUE "For more information, see README.md"
