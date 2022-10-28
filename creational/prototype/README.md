
# Problem

- we want to create the copy of the object, but have no access to his own class
- we want to change the properties of the object, but have not access to his own
  class
- prevent the creating tons of different classes which differs just by init values

# Solution

- implement "copy" method in class which can accept no parameters just for copy process, or some params to replace values of the old obj
