#!/usr/bin/env python3
"""
ChallengeLab CLI - Main command-line interface
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import List, Optional

import click
from click import echo, secho


class ChallengeManager:
    """Core challenge management functionality"""
    
    def __init__(self, base_path: Path = None):
        self.base_path = base_path or Path.cwd()
        self.challenges_path = self.base_path / "challenges"
        self.docker_path = self.base_path / "docker"
        
    def ensure_directories(self):
        """Ensure all required directories exist"""
        self.challenges_path.mkdir(exist_ok=True)
        self.docker_path.mkdir(exist_ok=True)
        
    def list_challenges(self) -> List[str]:
        """List all available challenges"""
        if not self.challenges_path.exists():
            return []
        
        challenges = []
        for item in self.challenges_path.iterdir():
            if item.is_dir() and (item / "challenge.sh").exists():
                challenges.append(item.name)
        return sorted(challenges)
    
    def create_challenge(self, name: str, description: str = "") -> bool:
        """Create a new challenge with boilerplate"""
        challenge_path = self.challenges_path / name
        
        if challenge_path.exists():
            secho(f"Challenge '{name}' already exists!", fg="red")
            return False
            
        try:
            # Create challenge directory
            challenge_path.mkdir(parents=True)
            tests_path = challenge_path / "tests"
            tests_path.mkdir()
            
            # Create challenge.sh
            challenge_script = f"""#!/bin/bash
# Challenge: {name}
# Description: {description or "No description provided"}

# TODO: Implement your solution here
# Read input from stdin and write output to stdout

# Example implementation (replace with your solution):
while IFS= read -r line; do
    echo "$line"
done
"""
            
            (challenge_path / "challenge.sh").write_text(challenge_script)
            (challenge_path / "challenge.sh").chmod(0o755)
            
            # Create test files
            (tests_path / "input.txt").write_text("test input\n")
            (tests_path / "expected.txt").write_text("test input\n")
            
            # Create README.md
            readme_content = f"""# {name}

## Description
{description or "No description provided"}

## Instructions
1. Edit `challenge.sh` to implement your solution
2. Your script should read from stdin and write to stdout
3. Run `challengelab test {name}` to test your solution

## Example
```bash
echo "input" | ./challenge.sh
```

## Test Cases
See `tests/` directory for input/output test cases.
"""
            
            (challenge_path / "README.md").write_text(readme_content)
            
            secho(f"Created challenge '{name}' successfully!", fg="green")
            return True
            
        except Exception as e:
            secho(f"Error creating challenge: {e}", fg="red")
            return False
    
    def run_challenge(self, name: str, input_data: str = None) -> bool:
        """Run a challenge in Docker container"""
        challenge_path = self.challenges_path / name
        
        if not challenge_path.exists():
            secho(f"Challenge '{name}' not found!", fg="red")
            return False
            
        try:
            # Build Docker image if needed
            self._build_docker_image(name)
            
            # Run the challenge
            cmd = [
                "docker", "run", "--rm", "-i",
                f"challengelab-{name}:latest"
            ]
            
            if input_data:
                result = subprocess.run(
                    cmd, 
                    input=input_data.encode(),
                    capture_output=True,
                    text=True
                )
            else:
                result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                echo(result.stdout)
                return True
            else:
                secho(f"Error running challenge: {result.stderr}", fg="red")
                return False
                
        except Exception as e:
            secho(f"Error running challenge: {e}", fg="red")
            return False
    
    def test_challenge(self, name: str) -> bool:
        """Run deterministic tests for a challenge"""
        challenge_path = self.challenges_path / name
        
        if not challenge_path.exists():
            secho(f"Challenge '{name}' not found!", fg="red")
            return False
            
        try:
            # Build Docker image if needed
            self._build_docker_image(name)
            
            # Run tests in Docker
            cmd = [
                "docker", "run", "--rm",
                f"challengelab-{name}:latest",
                "/app/run_tests.sh"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                secho(f"All tests passed for '{name}'!", fg="green")
                echo(result.stdout)
                return True
            else:
                secho(f"Tests failed for '{name}':", fg="red")
                echo(result.stderr)
                return False
                
        except Exception as e:
            secho(f"Error testing challenge: {e}", fg="red")
            return False
    
    def _build_docker_image(self, name: str):
        """Build Docker image for a challenge"""
        challenge_path = self.challenges_path / name
        dockerfile_path = self.docker_path / f"Dockerfile.{name}"
        
        # Create Dockerfile if it doesn't exist
        if not dockerfile_path.exists():
            self._create_dockerfile(name)
        
        # Build the image
        cmd = [
            "docker", "build",
            "-f", str(dockerfile_path),
            "-t", f"challengelab-{name}:latest",
            str(challenge_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Failed to build Docker image: {result.stderr}")
    
    def _create_dockerfile(self, name: str):
        """Create a Dockerfile for a challenge"""
        dockerfile_content = f"""FROM ubuntu:22.04

# Install basic tools
RUN apt-get update && apt-get install -y \\
    bash \\
    coreutils \\
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy challenge files
COPY challenge.sh /app/challenge.sh
COPY tests/ /app/tests/
COPY run_tests.sh /app/run_tests.sh

# Make scripts executable
RUN chmod +x /app/challenge.sh /app/run_tests.sh

# Default command
CMD ["/app/challenge.sh"]
"""
        
        dockerfile_path = self.docker_path / f"Dockerfile.{name}"
        dockerfile_path.write_text(dockerfile_content)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """ChallengeLab - Containerized CLI coding challenges"""
    pass


@cli.command()
@click.argument('name')
@click.option('--description', '-d', help='Challenge description')
def init(name: str, description: str):
    """Create a new challenge with boilerplate"""
    manager = ChallengeManager()
    manager.ensure_directories()
    manager.create_challenge(name, description)


@cli.command()
@click.argument('name')
@click.option('--input', '-i', help='Input data to pass to challenge')
def run(name: str, input: str):
    """Run challenge in Docker container"""
    manager = ChallengeManager()
    manager.run_challenge(name, input)


@cli.command()
@click.argument('name')
def test(name: str):
    """Execute deterministic tests inside container"""
    manager = ChallengeManager()
    manager.test_challenge(name)


@cli.command()
def list():
    """List all available challenges"""
    manager = ChallengeManager()
    challenges = manager.list_challenges()
    
    if not challenges:
        secho("No challenges found.", fg="yellow")
        return
    
    secho("Available challenges:", fg="green")
    for challenge in challenges:
        echo(f"  - {challenge}")


if __name__ == '__main__':
    cli()
