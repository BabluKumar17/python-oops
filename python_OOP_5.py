# Python OOP

# Difference b/w regular methods, class methods and static methods


class Employee:

	num_of_emps = 0
	raise_amount = 1.04		# class variable

	# constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1
	
	# a regular method
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	# a regular method
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# a class method
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)


##########################################################
# print(Employee.num_of_emps)

# Instance of Employee class
emp_1 = Employee("Bablu", "Kumar", 50000)
emp_2 = Employee("Amit", "Sharma", 60000)

# set another amout to raise_amt
Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
###########################################################

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Mohan-Das-60000'
emp_str_3 = 'Bablu-Kumar-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# total number of employee
print(Employee.num_of_emps)  # 3
