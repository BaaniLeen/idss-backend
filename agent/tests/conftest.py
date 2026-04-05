"""
Shared pytest fixtures for agent unit tests.
Sets a dummy OPENAI_API_KEY so UniversalAgent can be instantiated
without a real key (tests that actually call the LLM are skipped or mocked).
"""
import os
import sys
from pathlib import Path

import pytest

# Repo root + mcp-server on path so `from agent...` and `from app...` resolve
# when running `pytest agent/tests` without setting PYTHONPATH manually.
_root = Path(__file__).resolve().parents[2]
for _p in (_root, _root / "mcp-server"):
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

# Set before any imports so OpenAI client doesn't raise on init
os.environ.setdefault("OPENAI_API_KEY", "test-dummy-key-for-unit-tests")
