
# Problem

- excessive using of class inheritance(telescoping construcor) which cause:
  - large amount of parameters in __init__ method
  - large amount of classes

# Solution

- separate the construction(builder) of the object and it's representation(state) in different classes
- create the class(director) with methods which agregates the methods from builder and return specific product
