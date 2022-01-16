PASSWORD = '12345'


def password_required(func):

	def wrapper():
		password = input('write your password: ')

		if password == PASSWORD:
			return func()
		else:
			print('incorrect password')
	return wrapper


@password_required
def needs_password():
	print('The password is correct')


def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)

		return result.upper()

	return wrapper


@upper
def say_my_name(name):
	return 'Hello, {}'.format(name)


if __name__ == '__main__':
	print(say_my_name('leon'))
