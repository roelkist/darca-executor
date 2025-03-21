=============================================
Darca Exception - Advanced Exception Handling
=============================================

Darca Exception is a powerful and feature-rich Python exception base class designed to enhance error handling in your projects. 
It integrates seamlessly with `darca-log-facility` for structured logging, making debugging and error tracking effortless.

🚀 **Key Features**
--------------------
- **Generic & Reusable** - Works across various projects without modification.
- **Structured Logging** - Uses `DarcaLogger` for clean and consistent logs.
- **Exception Chaining** - Captures underlying causes (`cause`).
- **Metadata Support** - Add extra details (`metadata`).
- **JSON Serialization** - Easily convert exceptions to structured JSON.
- **100% Test Coverage** - Ensured via `pytest` and `pytest-cov`.

---

📦 **Installation**
--------------------
Darca Exception uses `Poetry` for dependency management. To install dependencies, use:

.. code-block:: bash

    make install

This will:
- Create a virtual environment (`venv`) if needed.
- Install `Poetry` and project dependencies.

---

🚀 **Usage**
--------------------
### **Raising an Exception**
You can raise an exception using `DarcaException`:

.. code-block:: python

    from darca_exception import DarcaException

    raise DarcaException("Something went wrong", error_code="GENERIC_ERROR")

### **Exception Chaining**
You can chain exceptions using `cause`:

.. code-block:: python

    try:
        1 / 0
    except ZeroDivisionError as e:
        raise DarcaException("Math error", error_code="MATH_001", cause=e)

### **Structured JSON Output**
Converting an exception to JSON is simple:

.. code-block:: python

    try:
        raise DarcaException("Database failure", error_code="DB_FAIL")
    except DarcaException as e:
        print(e.to_dict())

---

🛠 **Development & Testing**
----------------------------
### **Running Tests**
To run the test suite and check coverage:

.. code-block:: bash

    make test

This will:
- Run `pytest` with coverage enabled.
- Generate a test coverage report.

### **Formatting & Linting**
To automatically format and check code consistency:

.. code-block:: bash

    make format

### **Checking Before Pushing**
Before pushing code, always run:

.. code-block:: bash

    make check

This will:
- Format the code.
- Run pre-commit hooks.
- Execute tests.

---

📖 **Building Documentation**
-----------------------------
To generate documentation using Sphinx:

.. code-block:: bash

    make docs

This will:
- Build the documentation in `docs/build/html/`.

---

🚀 **Pre-Commit Hooks**
-----------------------
To run pre-commit checks before committing code:

.. code-block:: bash

    make precommit

This will:
- Run linting, formatting, and static analysis.
- Prevent common mistakes before pushing code.

---

🔧 **Adding Dependencies**
--------------------------
You can dynamically add dependencies using `make`:

- **Development dependencies** (`dev` group):

  .. code-block:: bash

      make add-deps group=dev deps="pytest black isort"

- **Production dependencies**:

  .. code-block:: bash

      make add-prod-deps deps="requests pydantic"

---

🗑 **Cleaning Up**
-----------------
To remove the virtual environment and reset dependencies:

.. code-block:: bash

    make clean

This will:
- Remove the Poetry environment.
- Delete cache files.

---

💡 **Contributing**
-------------------
Contributions are welcome! You can contribute by:

- **Submitting feature requests**  
- **Reporting issues**  
- **Creating pull requests for fixes and enhancements**  

Before submitting a pull request, make sure to:

1. Run `make check` to ensure all checks pass.
2. Follow code style and formatting guidelines.

---

📜 **License**
---------------
This project is licensed under the MIT License. See `LICENSE` for details.

---

🎉 **Final Notes**
-------------------
This project is production-ready and **fully tested**. 🚀  
If you find any issues, feel free to submit a bug report!

---

