def is_palindrome(word):
	return word[::-1].replace(" ","") == word.replace(" ","")

print(is_palindrome("anita lava la tina".lower()))


