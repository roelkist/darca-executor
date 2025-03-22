# tests/test_executor.py

import os

import pytest

from darca_executor import DarcaExecError


def test_successful_command(executor):
    """
    Test a basic command that should succeed.
    Works for both shell and non-shell modes.
    """
    command = (
        "echo Hello, Darca!"
        if executor.use_shell
        else ["echo", "Hello, Darca!"]
    )
    result = executor.run(command)
    assert result.returncode == 0
    assert "Hello, Darca!" in result.stdout


def test_failing_command(executor):
    """
    Ensure DarcaExecError is raised on command failure (non-zero exit code).
    """
    command = "exit 1" if executor.use_shell else ["sh", "-c", "exit 1"]

    with pytest.raises(DarcaExecError) as exc_info:
        executor.run(command)

    error = exc_info.value
    assert error.error_code == "DARCA_EXEC_ERROR"
    assert error.metadata["returncode"] == 1


def test_command_with_stderr_output(executor):
    """
    Test a command that writes to stderr but still exits with 0.
    """
    cmd = (
        "python -c 'import sys; sys.stderr.write(\"warning\\n\")'"
        if executor.use_shell
        else ["python", "-c", "import sys; sys.stderr.write('warning\\n')"]
    )

    result = executor.run(cmd)
    assert result.returncode == 0
    assert "warning" in result.stderr


def test_command_in_temp_dir(executor, temp_working_dir):
    """
    Test creating a file in a temporary working directory.
    """
    file_name = "test_output.txt"
    cmd = (
        f"echo DarcaRocks > {file_name}"
        if executor.use_shell
        else ["sh", "-c", f"echo DarcaRocks > {file_name}"]
    )

    executor.run(cmd)
    assert os.path.exists(file_name)

    with open(file_name) as f:
        content = f.read()
    assert "DarcaRocks" in content


def test_command_with_custom_env(executor, safe_env):
    """
    Verify environment variable overrides are passed to the subprocess.
    """
    cmd = (
        "python -c 'import os; print(os.getenv(\"LC_ALL\"))'"
        if executor.use_shell
        else ["python", "-c", "import os; print(os.getenv('LC_ALL'))"]
    )

    result = executor.run(cmd, env=safe_env)
    assert "C.UTF-8" in result.stdout
