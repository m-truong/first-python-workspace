# A best practice among Python developers is to use a project-specific virtual environment.
# Once you activate that environment, any packages you then install are isolated from other environments, including the global interpreter environment.
# ... ^^^ this reduces many complications that can arise from conflicting package versions.
# use Venv or Anaconda with Python: Create Environment.
# Note: By using the .py file extension, you tell VS Code to interpret this file as a Python program, so that it evaluates the contents with the Python extension and the selected interpreter.

# msg is a variable that stores the value "Roll a dice!".
# The (=) operator is used to assign the value on the right-hand side ("Roll a dice!") to the variable on the left-hand side (msg).
# In Python, you don't need to declare the type of the variable explicitly (e.g., string, int). Python infers the type automatically based on the value.
msg = "Roll a dice!"

# print() is a built-in Python function used to display output to the console.
# When you start typing print, notice how IntelliSense presents auto-completion options.
print(msg)

# Lines starting with # are comments.
# Comments are ignored by the Python interpreter and are used to explain the code or provide additional context for developers.