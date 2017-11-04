# Python Object-Oriented Programming

#Method: a function that is associated with a class.

class Employee:
	pass

# Instance of Employee class
emp_1 = Employee()
# Another different instance of Employee class
emp_2 = Employee()

# Let's add few attributes to the class
emp_1.first = "Bablu"
emp_1.last = "Kumar"
emp_1.email = "hacback17@yahoo.com"
emp_1.pay = 50000

emp_2.first = "Amit"
emp_2.last = "Sharma"
emp_2.email = "amit17@yahoo.com"
emp_2.pay = 60000

print(emp_1.email)		# hacback17@yahoo.com
print(emp_2.email)		# amit17@yahoo.com

print(emp_1 == emp_2)  # False


