import random

def run():
	random_number = random.randint(1,100)

	number_guess = int(input("Guess the number!: "))

	while number_guess != random_number:
		if number_guess > random_number:
			print("Try a smaller number")
		else:
			print("Try a bigger number")

		number_guess = int(input("Try again: "))
	print("You won!")

if __name__ == "__main__":
	run()
