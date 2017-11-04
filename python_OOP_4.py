## Python Object-Oriented Programming - 2

#Method: a function that is associated with a class.

# Class variable: class variables are the variables that are shared among all instances of a class.
# In Java, we use static keyword to show a class variable. 
# It does not belong to an instance of a class.

class Employee:

	raise_amount = 1.04		# class variable

	# constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


# Instance of Employee class
emp_1 = Employee("Bablu", "Kumar", 50000)
emp_2 = Employee("Amit", "Sharma", 60000)


# Let's look at what is contained inside a class
print(Employee.__dict__) 

# Now look at what is contained inside an instance
print(emp_1.__dict__)

print(emp_2.__dict__)




