
# Problem

- we need to create the copy of the object, but have not access ot his own class
- we need to change the properties of the object, but have not access ot his own
  class
- prevent the creating tons of different classes which differs just by init values

# Solution

- implement "copy" method in class which can accept no parameters for copy process, or some params to replace values of the old obj
