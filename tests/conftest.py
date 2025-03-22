# tests/conftest.py

import os
import tempfile

import pytest

from darca_executor import DarcaExecutor


@pytest.fixture(params=[True, False], ids=["shell", "no-shell"])
def executor(request):
    """
    Creates a DarcaExecutor instance with both shell=True and shell=False,
    to ensure coverage across both modes.
    """
    return DarcaExecutor(use_shell=request.param)


@pytest.fixture
def temp_working_dir():
    """
    Creates a temporary working directory for tests that
    interact with the filesystem.
    Automatically cleans up after use.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        orig = os.getcwd()
        os.chdir(tmpdir)
        try:
            yield tmpdir
        finally:
            os.chdir(orig)


@pytest.fixture
def safe_env(monkeypatch):
    """
    Provides a sanitized environment for command execution,
    e.g., removing dangerous or noisy env vars for tests.
    """
    monkeypatch.delenv("DEBUG", raising=False)
    monkeypatch.setenv("LC_ALL", "C.UTF-8")
    monkeypatch.setenv("LANG", "C.UTF-8")
    return dict(os.environ)
