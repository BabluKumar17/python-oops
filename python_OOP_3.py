# Python Object-Oriented Programming

#Method: a function that is associated with a class.

class Employee:
	# constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


# Instance of Employee class
emp_1 = Employee("Bablu", "Kumar", 50000)
# Another different instance of Employee class
emp_2 = Employee("Amit", "Sharma", 60000)

print(emp_1.email)		# hacback17@yahoo.com
print(emp_2.email)		# amit17@yahoo.com
print(emp_1 == emp_2)   # False


######################################
print(emp_1.fullname())	# Bablu Kumar

print(emp_2.fullname())	# Amit Sharma

print(Employee.fullname(emp_1))   # Bablu Kumar

print(Employee.fullname(emp_2))	  # Amit Sharma
######################################