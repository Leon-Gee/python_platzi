import sys

class Student():
	name = ""
	age = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age


school_students = {}



def add_student(name, age):
	global school_students
	student = Student(name, age)
	school_students[len(school_students)+1] = student



def delete_student(name):
	for i in school_students.values():
		if name == i.name:
			


def _print_welcome():
	print("*" * 50)
	print("Welcome to my dictionary student test")
	print(" 1.Add a student \n 2.Delete a student")
	print(" 3.List all students \n 4.Update a student")
	print(" 5.Search an stundent by his control number \n 6.Search an student by his name")
	print(" [Input anything to exit]")
	print("*" * 50)


def _get_command():
	command = None
	while not command:
		command = int(input("What would you want to do?: "))
	return command


def exit():
	sys.exit()


def _agenda_run():
	while (True):
		_print_welcome()
		command = _get_command()

		if command == 1:
			name = input("Write the name of the student: ")
			age = int(input("Write the age of the student: "))
			add_student(name = name, age = age)
		elif command == 2:
			name = input("Write the name of the student: ")
			delete_student(name = name)
		elif command == 3:
			list_students()
		elif command == 4:
			update_student()
		elif command == 5:
			search_student()
		elif command == 6:
			search_student()
		elif command == 7:
			exit()


if __name__ == "__main__":
	_agenda_run()
