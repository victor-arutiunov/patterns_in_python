
# Problem

- class should create only one instance
- have a global access to instance(don't know what it means)

# Solution

- do what you want
- if really...
  - add an exception to __init__ method that will block the recreating of instances
  - create a method that will return an instance if it exists or create if not
