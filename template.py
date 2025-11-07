import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # ✅ Do NOT overwrite NON-empty files
    if filepath.exists() and filepath.stat().st_size > 0:
        logging.info(f"File already exists: {filepath}, skipping creation.")
        continue

    # ✅ Create setup.py with proper content
    if filename == "setup.py":
        with open(filepath, "w") as f:
            f.write(
"""from setuptools import setup, find_packages

setup(
    name="textSummarizer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
"""
            )
        logging.info("Created setup.py with default configuration")
        continue  # ✅ prevents overwriting setup.py

    # ✅ Create empty files for all others
    with open(filepath, "w") as f:
        pass
    logging.info(f"Creating empty file: {filepath}")
