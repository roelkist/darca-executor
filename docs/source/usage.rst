Usage Guide
===========

.. code-block:: python

   from darca_executor import DarcaExecutor, DarcaExecError

   executor = DarcaExecutor(use_shell=True)

   try:
       result = executor.run("echo 'Hello from DarcaExecutor'")
       print(result.stdout)
   except DarcaExecError as e:
       print("Command failed:", e)
