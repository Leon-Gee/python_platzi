def run():
	#for i in range(0,999):
	#	if i % 2 != 0:
	#		continue
	#	print(i)

	#for i in range(0,100):
	#	print(i)
	#	if i == 78:
	#		break

	text = input("write something: ")
	for letter in text:
		if letter == 'o':
			break
		print(letter)


if __name__ == "__main__":
	run()
