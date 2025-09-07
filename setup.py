#!/usr/bin/env python3
"""
Setup script for ChallengeLab
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="challengelab",
    version="1.0.0",
    author="ChallengeLab Team",
    author_email="team@challengelab.dev",
    description="A platform for containerized CLI coding challenges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/challengelab/challengelab",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "challengelab=challenge_manager.cli:cli",
        ],
    },
    include_package_data=True,
    package_data={
        "challenge_manager": ["*.sh", "*.md"],
    },
)
