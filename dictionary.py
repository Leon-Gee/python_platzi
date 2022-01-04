def run():
	my_dict = {
		"key1":"value",
		"key2":"value2"
	}
	#print(my_dict["key1"])
	#print(my_dict["key2"])

	country_population = {
		'Argetina': 1241241,
		'Mexico' : 23234123412,
		'Brazil' : 1231231231231231
	}
	#for country in country_population.keys():
	#	print(country_population[country])

	for key in country_population.keys():
		print(key)
	for value in country_population.values():
		print(value)
	for key, value in country_population.items():
		print(key, value)


if __name__ == "__main__":
	run()
