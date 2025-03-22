Contributing to darca-executor
==============================

Thank you for considering contributing to **darca-executor**!

We welcome:
-----------

- 🛠 Bug fixes
- 🚀 New feature requests
- 📚 Improvements to documentation
- ✅ Additional test coverage
- 🧪 Enhancements to CI/CD workflows

How to Contribute
-----------------

1. **Fork the repository**
2. **Create a new branch** for your work:
   
   .. code-block:: bash

       git checkout -b feature/my-awesome-feature

3. **Write your code**, making sure to include appropriate tests.
4. **Run all checks before committing:**

   .. code-block:: bash

       make check

   This will:
   - Format your code
   - Run pre-commit hooks
   - Run tests and ensure 100% coverage

5. **Commit and push** your changes.
6. **Open a Pull Request** on GitHub targeting the `main` branch.

Reporting Bugs or Suggesting Features
-------------------------------------

If you’ve found a bug or have a feature request:

- Open an issue on GitHub with a clear description.
- Include reproduction steps or example use cases if possible.

CI/CD
-----

All pull requests are validated by the GitHub Actions CI pipeline which runs:

.. code-block:: bash

    make ci

This includes formatting checks, pre-commit hooks, tests, and documentation builds.

Individual Commands
-------------------

You can also run commands separately if needed:

- `make format` – Apply code formatters
- `make precommit` – Run pre-commit hooks manually
- `make test` – Run all tests with coverage report
- `make docs` – Build the Sphinx documentation

Questions?
----------

Feel free to open a discussion or reach out by opening an issue. We’re happy to help!

Happy hacking! 💻✨
