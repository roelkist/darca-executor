Darca Executor
==============

**Darca Executor** is a Python module designed for secure and structured command execution.  
It integrates tightly with the `darca-log-facility` and `darca-exception` ecosystem, ensuring consistent logging, structured error reporting, and clean extensibility.

.. image:: coverage.svg
   :target: coverage.svg
   :alt: Test coverage badge

---

Features
--------

- 🛠  Execute system commands with subprocess safely and consistently.
- 🧾  Structured error handling via `DarcaExecError` (based on `DarcaException`)
- 📜  Rich logging integration with `DarcaLogger`
- 🧪  Pytest-based test suite with coverage and formatting checks
- 📚  Sphinx-ready documentation setup
- 🧰  Built-in Makefile for all major development workflows

---

Installation
------------

To get started with local development:

.. code-block:: bash

    make install

This installs all dependencies into a self-contained virtual environment in `/tmp/darca-executor-venv`.

To install additional packages:

.. code-block:: bash

    make add-deps group=dev deps="some-package"
    make add-prod-deps deps="some-runtime-package"

---

Usage
-----

Example usage of the executor:

.. code-block:: python

    from darca_executor import DarcaExecutor, DarcaExecError

    executor = DarcaExecutor(use_shell=True)

    try:
        result = executor.run("echo Hello, Darca!")
        print(result.stdout)
    except DarcaExecError as e:
        print(f"Command failed: {e}")

---

Testing & Quality
-----------------

Run all checks (formatting, tests, coverage, precommit):

.. code-block:: bash

    make check

Run tests with coverage output:

.. code-block:: bash

    make test

Run pre-commit hooks:

.. code-block:: bash

    make precommit

Apply auto-formatting:

.. code-block:: bash

    make format

---

Documentation
-------------

To build the docs:

.. code-block:: bash

    make docs

Docs will be available at: `docs/build/html/index.html`

---

Continuous Integration
----------------------

The `make ci` command is used as the default entrypoint in GitHub Actions:

.. code-block:: bash

    make ci

This will install dependencies, run precommit, test the codebase, and build the documentation.

---

Contributing
------------

We welcome your contributions!

Please see `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ for details on how to get involved.

You can:

- 💡 Open feature requests or ideas via GitHub Issues
- 🐛 Report bugs
- 🔧 Submit Pull Requests for fixes, enhancements, or tests

---

License
-------

This project is maintained by the Darca collective. License details TBD.
