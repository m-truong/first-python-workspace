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

# General Python Syntax Rules:
# Indentation: Python uses indentation (spaces or tabs) to define blocks of code. For example, in loops or functions, the code inside the block must be indented.
# Case Sensitivity: Python is case-sensitive, so msg and Msg would be treated as different variables.
# No Semicolons: Unlike some other languages (e.g., C, Java), Python does not require semicolons (;) to terminate statements.

# My Notes:
# must always use a virtual environment through VSCode ~ either as venv or conda
# this prevents any issues of conflicting dependencies and what-the-who-ha.
# python syntax rules looks different from javascript
# it relies on indentations for IntelliSense to determine blocks of code
# semi-colons (;) are not needed to terminate statements
# also CASE-SENSITIVE variables

# What is Flask? => for Python backendfrom flask import Flask
# Microframework ~ used to build smaller REST APIs ~ smaller-scale web applications

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

# What is Django?
# Type: Full-stack framework
# Philosophy: Django is a "batteries-included" framework, meaning it comes with many built-in features like an ORM (Object-Relational Mapping), authentication, admin panel, and more. It emphasizes rapid development and clean, pragmatic design.

# Features:
# Built-in database support (via ORM).
# Authentication and user management out of the box.
# Scalable and secure.
# Ideal for large, complex projects.

# Use Cases:
# Enterprise-level applications.
# Content management systems (CMS).
# E-commerce platforms.

from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', home),
]