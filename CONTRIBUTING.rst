Contributing to Darca Executor
==============================

First off, thank you for considering contributing to **Darca Executor**.  
Your ideas, suggestions, code, and feedback are what make this project better.

---

Getting Started
---------------

To get started with local development:

.. code-block:: bash

    make install

This sets up a Poetry environment in `/tmp/darca-executor-venv` and installs all dependencies.

---

Pre-Commit Checklist
--------------------

Before pushing your code or opening a Pull Request, run the following:

.. code-block:: bash

    make check

This will:

- Auto-format your code (via Black + isort)
- Run pre-commit hooks (linting, checks)
- Run the full test suite with coverage
- Build the documentation to ensure it's error-free

---

How to Contribute
-----------------

We welcome:

- 🐞 **Bug Reports** — Submit an issue with a clear reproduction.
- 💡 **Feature Requests** — Have a cool idea? Open an issue and describe it.
- 🛠  **Pull Requests** — Fix a bug, improve tests, or add functionality.

---

Pull Request Guidelines
-----------------------

1. Fork the repository
2. Create a new branch: `git checkout -b feat/your-feature-name`
3. Make your changes
4. Ensure `make check` passes
5. Push to your fork and submit a Pull Request

---

Best Practices
--------------

- Keep your code Pythonic and consistent with existing patterns.
- Use `DarcaExecutor` and `DarcaExecError` consistently for command execution and error handling.
- Add or update tests for any new functionality.
- Keep docstrings and logging clear and helpful.

---

Communication
-------------

We encourage open communication via GitHub Issues and Pull Requests.

Whether it's a suggestion, bug, or a "hey this is cool" — we want to hear from you!

---

Thank you again for helping make Darca Executor awesome! 🚀
