import random


def binary_search(data, target, low, high):
	if low > high:
		return False

	mid = (low + high) // 2

	if data[mid] == target:
		return True
	elif target < data[mid]:
		return binary_search(data, target, low, high = mid -1)
	else:
		return binary_search(data, target, low = mid +1 , high = high)



if __name__ == '__main__':
	data = [random.randint(0,100) for i in range(10)]

	sorted_data = sorted(data)
	print(sorted_data)

	target = int(input('what number would you want to find? '))
	found = binary_search(data = sorted_data, target = target, low = 0, high = len(sorted_data))
	print(found)
