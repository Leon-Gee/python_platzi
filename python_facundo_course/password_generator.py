import random

def password_generate():

	CAPITALS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P',
	 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

	SMALLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
	, 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q'
	, 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

	NUMBERS = [0, 1, 2, 3, 4, 5, 6 ,7 ,8, 9]

	CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
	'{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~'
	, '°', '^', '&', '$', '#', '"']

	CHARACTERS = CAPITALS + SMALLS + NUMBERS + CHARS

	SUPER_SECRET_STUFF = []

	for i in range(15):
		random_char = str(random.choice(CHARACTERS))
		SUPER_SECRET_STUFF.append(random_char)

	SUPER_SECRET_STUFF = "".join(SUPER_SECRET_STUFF)

	return SUPER_SECRET_STUFF

def run():
	password = password_generate()
	print("your new password is: " + password)
	print("funny, a password is beign printed")


if __name__ == "__main__":
	run()


