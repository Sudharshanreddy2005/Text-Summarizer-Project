import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger

# ✅ FIX: 'ensure' package breaks in Python 3.12+
try:
    from ensure import ensure_annotations
except Exception:
    # fallback: simple no-op decorator
    def ensure_annotations(func):
        return func

from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object"""
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as box_exception:
        raise box_exception
    except Exception as e:
        logger.exception(f"Error reading the YAML file: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """Creates directories if they don't exist"""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file"""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f" ~ {size_in_kb} KB"
