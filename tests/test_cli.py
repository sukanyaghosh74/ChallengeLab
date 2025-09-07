#!/usr/bin/env python3
"""
Unit tests for ChallengeLab CLI
"""

import pytest
import subprocess
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from challenge_manager.cli import ChallengeManager


class TestChallengeManager:
    """Test cases for ChallengeManager class"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.base_path = Path(self.temp_dir)
        self.manager = ChallengeManager(self.base_path)
        self.manager.ensure_directories()
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_ensure_directories(self):
        """Test directory creation"""
        assert self.manager.challenges_path.exists()
        assert self.manager.docker_path.exists()
    
    def test_list_challenges_empty(self):
        """Test listing challenges when none exist"""
        challenges = self.manager.list_challenges()
        assert challenges == []
    
    def test_create_challenge(self):
        """Test challenge creation"""
        name = "test-challenge"
        description = "A test challenge"
        
        success = self.manager.create_challenge(name, description)
        assert success is True
        
        challenge_path = self.manager.challenges_path / name
        assert challenge_path.exists()
        assert (challenge_path / "challenge.sh").exists()
        assert (challenge_path / "tests" / "input.txt").exists()
        assert (challenge_path / "tests" / "expected.txt").exists()
        assert (challenge_path / "README.md").exists()
    
    def test_create_challenge_already_exists(self):
        """Test creating challenge that already exists"""
        name = "existing-challenge"
        self.manager.create_challenge(name)
        
        success = self.manager.create_challenge(name)
        assert success is False
    
    def test_list_challenges_with_content(self):
        """Test listing challenges when they exist"""
        # Create a test challenge
        self.manager.create_challenge("challenge1")
        self.manager.create_challenge("challenge2")
        
        challenges = self.manager.list_challenges()
        assert "challenge1" in challenges
        assert "challenge2" in challenges
        assert len(challenges) == 2


class TestCLICommands:
    """Test cases for CLI commands"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = Path.cwd()
        os.chdir(self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir)
    
    def test_cli_help(self):
        """Test CLI help command"""
        result = subprocess.run(
            ["python", "-m", "challenge_manager.cli", "--help"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert "ChallengeLab" in result.stdout
    
    def test_list_command_empty(self):
        """Test list command with no challenges"""
        result = subprocess.run(
            ["python", "-m", "challenge_manager.cli", "list"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert "No challenges found" in result.stdout


if __name__ == "__main__":
    pytest.main([__file__])
