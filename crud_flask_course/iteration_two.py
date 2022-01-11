clients = 'leon, oswaldo,'


def create_client(client_name):
	""" creates and saves a client
	param str client_name
	"""
	global clients
	if _verify_client(client_name = client_name):
		print('The client is already in the agenda!')
	else:
		clients += client_name
		_add_coma()



def update_client(client_name, updated_client_name):
	"""updates a client
	param str client_name name of the client wich is updated
	param str updated_client_name the new name of the client
	"""
	global clients

	if _verify_client(client_name = client_name):
		clients = clients.replace(client_name + ',',updated_client_name + ',')
	else:
		_client_not_found


def delete_client(client_name):
	"""deletes a client
	param str client_name the name of the client wich is beign deleted
	"""
	global clients
	if _verify_client(client_name = client_name):
		clients = clients.replace(client_name + ',' , '')
		clients.strip()
	else:
		_client_not_found()


def search_client(client_name):
	clients_list = clients.split(',')

	for client in clients_list:
		if client != client_name:
			continue
		else:
			print(f'The client {client_name} is in the list')
	print(f'The client {client_name} is not in the list')

def list_clients():
	global clients
	print(clients)


def _add_coma():
	global clients
	clients += ','



def _get_client_name():
	client_name = None
	while not client_name:
		client_name = input('What is the client name: ')
	return client_name


def _client_not_found():
	print("The client its not in the agenda")


def _verify_client(client_name):
	"""verifies that a client its in the agenda
	param str client_name
	returns bool true if the client its in the list
	"""

	global clients

	if client_name in clients:
		return True
	else:
		return False


def print_welcome():
	print('welcome to our client agenda')
	print('*'*50)
	print('What would you want to do today?:)')
	print(' [C]reate client \n [D]elete client \n [U]pdate client \n [S]earch Client \n [E]xit')
	print('COMMAND: ')


if __name__ == '__main__':
	while(True):
		print_welcome()
		command = input().upper()
		if command == 'C':
			create_client(client_name = _get_client_name())
			list_clients()

		elif command == 'D':
			delete_client(client_name = _get_client_name())
			list_clients()
		elif command == 'U':
			new_client_name = input('Whats the new name of the client: ')
			update_client(client_name = _get_client_name(), updated_client_name = new_client_name)
			list_clients()
		elif command == 'S':
			search_client(client_name = _get_client_name())
		elif command == 'E':
			break
		else:
			print('Invalid command')
