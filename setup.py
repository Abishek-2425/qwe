from setuptools import setup, find_packages
from pathlib import Path

# Read README.md for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="gensh",
    version="0.1.0",
    description="Natural-language to shell command converter CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ABISHEK S",
    packages=find_packages(include=["core", "core.*", "cli", "cli.*"]),
    python_requires=">=3.10",
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "google-generativeai",  # Adjust if a specific version is required
    ],
    entry_points={
        "console_scripts": [
            "gensh=cli.main:main",  # CLI entry point
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
