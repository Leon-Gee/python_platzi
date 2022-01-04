def is_prime(number):
	if number == 1:
		return False
	count = 0

	for i in range(1, number + 1):
		if i == 1 or i == number:
			continue
		if number % i == 0:
			count += 1

	if count == 0:
		return True
	else:
		return False


def run(test_number):
	if is_prime(number = test_number):
		print(str(test_number) + " is a prime number ")
	else:
		print(str(test_number) + " is not a a prime number")


def is_prime_but_useful(number):
	if number == 1:
		return False
	for i in range(2,number+1):
		if number == i:
			continue
		if number % i == 0:
			return False
	return True

if __name__ == "__main__":
	test_number = int(input("Welcome to prime number test, write a number: "))
	run(test_number=test_number)
	print(is_prime_but_useful(number=test_number))
