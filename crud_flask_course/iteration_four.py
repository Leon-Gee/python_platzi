clients = [
	{
		'name' : 'pablo',
		'company' : 'Google',
		'email' : 'pablo@google.com',
		'position': 'Software Engineer',
	},
	{
		'name': 'Ricardo',
		'company': 'Facebook',
		'email': 'ricardo@facebook.com',
		'position':'Data engineer',
	}
]


def create_client(client):
	""" creates and saves a client
	param
	"""
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('The client is already in the agenda!')


def update_client(client_name, updated_client_name):
	"""updates a client
	"""
	global clients

	if _verify_client(client_name = client_name):
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else:
		_client_not_found


def delete_client(client_name):
	"""deletes a client
	"""
	global clients
	if _check_client_name(client_name = client_name):
		for idx, client in enumerate(clients):
			if client_name == client['name']:
				clients.pop(idx)
				break

def _check_client_name(client_name):
	for client in clients:
		if client_name == client['name']:
			return True

	return False


def search_client(client_name):

	for client in clients:
		if client != client_name:
			continue
		else:
			print(f'The client {client_name} is in the list')
	print(f'The client {client_name} is not in the list')


def list_clients():
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
		uid = idx,
		name = client['name'],
		company = client['company'],
		email = client['email'],
		position = client['position']))


def _get_client_field(field_name):
	field = None

	while not field:
		field = input(f'What is the {field_name} of the client? ')
	return field


def _get_client_name():
	client_name = None
	while not client_name:
		client_name = input('What is the client name: ')
	return client_name


def _client_not_found():
	print("The client its not in the agenda")


def _verify_client(client_name):
	"""verifies that a client its in the agenda
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
			client = {
				'name': _get_client_field(field_name = 'name'),
				'company': _get_client_field(field_name = 'company'),
				'email': _get_client_field(field_name = 'email'),
				'position': _get_client_field(field_name = 'position')
			}
			create_client(client)
			list_clients()

		elif command == 'D':
			delete_client(client_name = _get_client_name())
			list_clients()
		elif command == 'U':
			client = {
				'name': _get_client_field(field_name = 'name'),
				'company': _get_client_field(field_name = 'company'),
				'email': _get_client_field(field_name = 'email'),
				'position': _get_client_field(field_name = 'position')
			}
			list_clients()
		elif command == 'S':
			search_client(client_name = _get_client_name())
		elif command == 'E':
			break
		else:
			print('Invalid command')
