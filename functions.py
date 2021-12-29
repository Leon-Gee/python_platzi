

#def print_special_message():
#	print("Special message: ")
#	print("Im learning about functions!")

#if __name__ == "__main__":
#	print_special_message()
def hi_message(message):
	print("hi")
	print("how are u")
	print(message)
	print("adios")

option = int(input("Choose an option (1,2,3) : "))

if option == 1:
	hi_message("You choosed option 1")

elif option == 2:
	hi_message("You choosed option 2")

elif option == 3:
	hi_message("You choosed option 3")

else:
	print("Choose a proper option")
