
# Problem & desire

- we create a class with complex logic and this class realize abstract and implementation logic at once. That means if you change code in absctract level you also have to change it at implementation level. It leads to creating of huge ierarchy of subclasses for each case.
Examples:
  - web development. We have stable business logic and want use it in different web frameworks.
  - API. The same.

# Solution

- separate abstract logic and implementation in different classes
- pass the implementation object as parameter to the absctract class \_\_init__ method

# Benefits

- implementation logic becomes isolated from client
- easier scaling of program code:
  - extension of absctract code does not affect on implementation code and vise versa
