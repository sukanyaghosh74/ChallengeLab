# Contributing to ChallengeLab

Thank you for your interest in contributing to ChallengeLab! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Git

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/challengelab.git
   cd challengelab
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Verify installation:**
   ```bash
   challengelab --help
   ```

## 🧪 Adding New Challenges

### Challenge Structure

Each challenge should follow this structure:

```
challenges/your-challenge-name/
├── challenge.sh              # Main challenge script
├── tests/
│   ├── input.txt            # Test input data
│   └── expected.txt         # Expected output
├── run_tests.sh             # Custom test runner (optional)
└── README.md                # Challenge documentation
```

### Challenge Requirements

1. **Executable Script**: `challenge.sh` must be executable
2. **Standard I/O**: Read from stdin, write to stdout
3. **Deterministic**: Same input should always produce same output
4. **Unix Compatible**: Should work in Unix-like environments
5. **Well Documented**: Clear README with examples

### Creating a Challenge

1. **Use the CLI to create boilerplate:**
   ```bash
   challengelab init your-challenge-name --description "Your challenge description"
   ```

2. **Implement your challenge in `challenge.sh`:**
   ```bash
   #!/bin/bash
   # Your implementation here
   while IFS= read -r line; do
       # Process the line
       echo "$processed_line"
   done
   ```

3. **Add test cases:**
   - Edit `tests/input.txt` with test input
   - Edit `tests/expected.txt` with expected output
   - Ensure exact match between input and expected output

4. **Test your challenge:**
   ```bash
   challengelab test your-challenge-name
   ```

### Challenge Guidelines

#### Difficulty Levels
- **Beginner**: Simple string manipulation, basic algorithms
- **Intermediate**: File processing, data structures, regex
- **Advanced**: Complex algorithms, system programming, optimization

#### Best Practices
- **Clear Problem Statement**: Explain what the challenge does
- **Examples**: Provide input/output examples
- **Edge Cases**: Test empty input, special characters, large inputs
- **Hints**: Give helpful hints without spoiling the solution
- **Documentation**: Explain the solution approach

#### Example Challenge Template

```bash
#!/bin/bash
# Challenge: [Challenge Name]
# Description: [Brief description]
# Difficulty: [Beginner/Intermediate/Advanced]

# TODO: Implement your solution here
# Read input from stdin and write output to stdout

while IFS= read -r line; do
    # Your solution logic here
    echo "$result"
done
```

## 🔧 Development Guidelines

### Code Style

- **Python**: Follow PEP 8, use Black for formatting
- **Bash**: Use shellcheck for linting, follow best practices
- **Documentation**: Use clear, concise language

### Testing

1. **Test your challenge:**
   ```bash
   challengelab test your-challenge-name
   ```

2. **Test all challenges:**
   ```bash
   make test
   ```

3. **Run Docker tests:**
   ```bash
   make docker-test
   ```

### Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-challenge-name
   ```

2. **Make your changes:**
   - Add your challenge
   - Update documentation if needed
   - Test thoroughly

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add your-challenge-name challenge"
   ```

4. **Push and create PR:**
   ```bash
   git push origin feature/your-challenge-name
   ```

### PR Requirements

- **Working Challenge**: Must pass all tests
- **Documentation**: Clear README with examples
- **Test Coverage**: Comprehensive test cases
- **CI Passing**: All GitHub Actions checks must pass

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**: OS, Python version, Docker version
2. **Steps to Reproduce**: Clear reproduction steps
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Error Messages**: Full error output

## 💡 Feature Requests

For feature requests, please:

1. **Check Existing Issues**: Search for similar requests
2. **Describe the Feature**: Clear description of what you want
3. **Use Case**: Explain why this feature would be useful
4. **Implementation Ideas**: If you have ideas for implementation

## 📝 Documentation

### README Updates

When adding challenges, update:

1. **Challenge List**: Add to the "Available Challenges" section
2. **Examples**: Add example usage
3. **Installation**: Update if new dependencies are needed

### Code Documentation

- **Docstrings**: Document all functions and classes
- **Comments**: Explain complex logic
- **Type Hints**: Use type hints in Python code

## 🏗️ Architecture

### Core Components

1. **CLI Module** (`challenge_manager/cli.py`): Main command-line interface
2. **Challenge Manager**: Handles challenge operations
3. **Docker Integration**: Containerized execution
4. **Test Harness**: Automated testing system

### Adding New CLI Commands

1. **Add command function:**
   ```python
   @cli.command()
   @click.argument('name')
   def new_command(name: str):
       """Description of new command"""
       # Implementation
   ```

2. **Update help text and documentation**

## 🧪 Testing Strategy

### Test Types

1. **Unit Tests**: Test individual functions
2. **Integration Tests**: Test CLI commands
3. **Challenge Tests**: Test challenge implementations
4. **Docker Tests**: Test containerized execution

### Running Tests

```bash
# Run all tests
make test

# Run specific test
challengelab test challenge-name

# Run with Docker
make docker-test
```

## 📋 Checklist for Contributors

Before submitting a PR, ensure:

- [ ] Challenge passes all tests
- [ ] Documentation is complete and clear
- [ ] Code follows style guidelines
- [ ] No hardcoded paths or system-specific code
- [ ] Docker image builds successfully
- [ ] CI pipeline passes
- [ ] README is updated if needed

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the golden rule

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Email**: team@challengelab.dev for direct contact

## 📄 License

By contributing to ChallengeLab, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to ChallengeLab! 🎯
