def currency_to_dollars(currency,dollar_value):
	quantity_pesos= float(input("How many " + currency +" pesos are you holding: "))
	dollars = quantity_pesos / dollar_value
	dollars = round(dollars,2)

	print("You have $ " + str(dollars) + " dollars")



if __name__ == "__main__":
	menu =  """
	Welcome to our currency convertor
	
	1.- Colombian Pesos
	2.- Argetinian Pesos
	3.- Mexican Pesos

	Please, choose an option: 
	"""
	option = int(input(menu))

	if option == 1:
		currency_to_dollars("Colombian",3875)
	elif option == 2:
		currency_to_dollars("Argentinian",65)
	elif option == 3:
		currency_to_dollars("Mexican", 20)
	else:
		print("Please, choose a proper option")
