# Changelog

All notable changes to ChallengeLab will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Core CLI functionality with Click framework
- Docker containerization support
- Deterministic test harness
- GitHub Actions CI/CD pipeline
- Example reverse-string challenge

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [1.0.0] - 2024-01-01

### Added
- Initial release of ChallengeLab
- CLI tool with commands: `init`, `run`, `test`, `list`
- Docker-based challenge execution
- Automated test harness with input/output verification
- GitHub Actions workflow for CI/CD
- Comprehensive documentation
- Example challenge: reverse-string
- Support for custom Dockerfiles
- Docker Compose integration
- Python packaging with setup.py and pyproject.toml
- MIT License

### Features
- **Challenge Management**: Create, run, and test challenges
- **Containerized Execution**: Isolated Docker environments
- **Deterministic Testing**: Automated input/output verification
- **CLI Interface**: Easy-to-use command-line tool
- **CI/CD Integration**: Automated testing with GitHub Actions
- **Extensible Architecture**: Easy to add new challenges
- **Documentation**: Comprehensive guides and examples

### Technical Details
- Python 3.8+ support
- Click framework for CLI
- Docker and Docker Compose
- Ubuntu 22.04 base images
- Bash-based test runners
- Pytest for Python testing
- GitHub Actions for automation

---

## Version History

- **1.0.0**: Initial release with core functionality
- **Unreleased**: Future features and improvements

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to ChallengeLab.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
