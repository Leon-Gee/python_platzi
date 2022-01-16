
class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def _say_hello(self):
		print('Hello, my name is {} and i am {} years old'.format(self.name, self.age))


if __name__ == '__main__':

	person = Person('David', 34)

	person._say_hello()
