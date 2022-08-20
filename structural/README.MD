
# Problem

- program which uses object(s) with specified interface, become broken when we want to use another object, but with different interface
- when we use set of objects of subclasses and one of them missed specific method or property(this problem also could be solved by "Decorator" pattern)

# Solution

- create an adapter object which has the same methods as specified interface but under the hood this methods works with new incopatible object
