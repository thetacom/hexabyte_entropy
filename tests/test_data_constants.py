"""Test Files Module."""
from enum import Enum
from pathlib import Path


class Files(Enum):
    """Test file paths for use within test cases."""

    DATA_1K = Path("tests/data/1K.data")
    AARCH64 = Path("tests/data/hello_world_aarch64")
    X86_64 = Path("tests/data/hello_world_x86-64")
    UTF8 = Path("tests/data/hello_world.c")
    MISSING = Path("tests/data/missing")
    TEST = Path("tests/data/test.data")
