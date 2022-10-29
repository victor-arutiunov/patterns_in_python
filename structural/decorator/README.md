
# Problem & desire

	- adding a new abilities to your **object** with no changes of this object

# Solution

	- create a **decorator** object which have a parameter with **object**
	- add **decorator** methods which delegates all work to **object** methods
		with the same names
	- extend **decorator** by new classes which instead of pure translation of
		work to **object** do some some work before or after **object** method
		executes
