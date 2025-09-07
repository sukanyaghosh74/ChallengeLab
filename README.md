# ChallengeLab

A platform for containerized CLI coding challenges with automated test harnesses, reproducible Docker environments, and concise documentation.

## 🚀 Features

- **Containerized Execution**: Each challenge runs in isolated Docker containers
- **Deterministic Testing**: Automated test harness with input/output verification
- **CLI Management**: Easy-to-use command-line interface for challenge management
- **CI/CD Integration**: GitHub Actions for automated validation
- **Reproducible Environments**: Pinned Docker images ensure consistent results
- **Extensible Architecture**: Easy to add new challenges and test cases

## 📋 Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Git

## 🛠️ Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/sukanyaghosh74/ChallengeLab.git
cd ChallengeLab

# Install dependencies
pip install -r requirements.txt

# Install ChallengeLab CLI
pip install -e .
```

### Using pip (when published)

```bash
pip install challengelab
```

## 🎯 Quick Start

1. **List available challenges:**
   ```bash
   challengelab list
   ```

2. **Create a new challenge:**
   ```bash
   challengelab init my-challenge --description "A sample challenge"
   ```

3. **Test a challenge:**
   ```bash
   challengelab test reverse-string
   ```

4. **Run a challenge:**
   ```bash
   echo "hello world" | challengelab run reverse-string --input "hello world"
   ```

## 📚 CLI Commands

### `challengelab init <name>`
Create a new challenge with boilerplate code.

**Options:**
- `--description, -d`: Challenge description

**Example:**
```bash
challengelab init fibonacci --description "Calculate Fibonacci numbers"
```

### `challengelab run <name>`
Run a challenge in a Docker container.

**Options:**
- `--input, -i`: Input data to pass to the challenge

**Example:**
```bash
challengelab run reverse-string --input "hello"
```

### `challengelab test <name>`
Execute deterministic tests for a challenge.

**Example:**
```bash
challengelab test reverse-string
```

### `challengelab list`
List all available challenges.

**Example:**
```bash
challengelab list
```

## 🏗️ Project Structure

```
challengelab/
├── challenge_manager/          # Core Python CLI
│   ├── __init__.py
│   ├── cli.py                 # Main CLI implementation
│   └── __main__.py
├── challenges/                # Challenge definitions
│   └── reverse-string/        # Example challenge
│       ├── challenge.sh       # Challenge implementation
│       ├── tests/             # Test cases
│       │   ├── input.txt      # Test input
│       │   └── expected.txt   # Expected output
│       ├── run_tests.sh       # Test runner
│       └── README.md          # Challenge documentation
├── docker/                    # Docker configuration
│   ├── Dockerfile.base        # Base Docker image
│   └── run_tests.sh           # Generic test runner
├── .github/workflows/         # CI/CD configuration
│   └── ci.yml
├── docker-compose.yml         # Docker Compose setup
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── pyproject.toml            # Modern Python packaging
└── README.md                 # This file
```

## 🧪 Creating Challenges

### Challenge Structure

Each challenge should follow this structure:

```
challenges/my-challenge/
├── challenge.sh              # Main challenge script
├── tests/
│   ├── input.txt            # Test input data
│   └── expected.txt         # Expected output
├── run_tests.sh             # Custom test runner (optional)
└── README.md                # Challenge documentation
```

### Challenge Script Requirements

- Must be executable (`chmod +x challenge.sh`)
- Should read from stdin and write to stdout
- Handle input/output deterministically
- Work in a Unix-like environment

### Example Challenge Script

```bash
#!/bin/bash
# Challenge: Word Count
# Description: Count words in input

while IFS= read -r line; do
    echo "$line" | wc -w
done
```

### Test Files

- **input.txt**: Contains test input data
- **expected.txt**: Contains expected output (must match exactly)

## 🐳 Docker Integration

### Base Image

All challenges run in a Ubuntu 22.04 container with:
- Bash shell
- Core utilities (coreutils, diffutils)
- Python 3
- Basic development tools

### Custom Dockerfiles

You can create custom Dockerfiles for specific challenges:

```dockerfile
FROM ubuntu:22.04

# Install challenge-specific dependencies
RUN apt-get update && apt-get install -y \
    your-specific-tool \
    && rm -rf /var/lib/apt/lists/*

# Copy challenge files
COPY challenge.sh /app/challenge.sh
COPY tests/ /app/tests/
COPY run_tests.sh /app/run_tests.sh

# Make executable
RUN chmod +x /app/challenge.sh /app/run_tests.sh

WORKDIR /app
CMD ["/app/challenge.sh"]
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Builds Docker images** for each challenge
2. **Runs tests** in isolated containers
3. **Validates output** against expected results
4. **Reports failures** with detailed error messages

### Workflow Triggers

- Push to `main` or `develop` branches
- Pull requests to `main` branch

### Matrix Testing

Tests run in parallel for multiple challenges using GitHub Actions matrix strategy.

## 🧪 Testing

### Running Tests Locally

```bash
# Test a specific challenge
challengelab test reverse-string

# Test all challenges
for challenge in $(challengelab list | grep "  -" | sed 's/  - //'); do
    challengelab test "$challenge"
done
```

### Using Docker Compose

```bash
# Test with Docker Compose
docker-compose up --build reverse-string
```

### Test Output

Tests provide colored output:
- 🟢 **Green**: Test passed
- 🔴 **Red**: Test failed (with diff)
- 🟡 **Yellow**: Test information

## 📖 Available Challenges

### reverse-string
**Description**: Reverse each line of input character by character.

**Example**:
```bash
echo "hello" | ./challenge.sh
# Output: olleh
```

**Test Cases**:
- "hello world" → "dlrow olleh"
- "challenge" → "egnellahc"
- "docker" → "rekcod"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-challenge`)
3. Add your challenge following the structure guidelines
4. Add comprehensive tests
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing challenge'`)
7. Push to the branch (`git push origin feature/amazing-challenge`)
8. Open a Pull Request

### Challenge Guidelines

- **Clear Problem Statement**: Provide a concise description
- **Deterministic Output**: Ensure consistent results
- **Comprehensive Tests**: Include edge cases
- **Good Documentation**: Explain the challenge and solution approach
- **Reasonable Difficulty**: Balance challenge with accessibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI functionality
- Containerized with [Docker](https://www.docker.com/)
- CI/CD powered by [GitHub Actions](https://github.com/features/actions)
- Testing framework uses [pytest](https://pytest.org/)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/challengelab/challengelab/issues)
- **Discussions**: [GitHub Discussions](https://github.com/challengelab/challengelab/discussions)
- **Email**: sukanyaghosh2006@gmail.com

---

**ChallengeLab** - Making coding challenges reproducible, testable, and fun! 🎯
