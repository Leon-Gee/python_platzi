import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode = 'r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name, mode = 'w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)

		writer.writerows(clients)

		os.remove(CLIENT_TABLE)
		os.rename(tmp_table_name, CLIENT_TABLE)



def create_client(client):
	""" creates and saves a client
	param
	"""
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('The client is already in the agenda!')


def update_client(client_name):
	"""updates a client
	"""
	global clients

	if _check_client_name(client_name = client_name):
		for idx, client in enumerate(clients):
			if client_name == client['name']:
				clients[idx] = client_input()


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


def client_input():
	client = {
		'name': _get_client_field(field_name = 'name'),
		'company': _get_client_field(field_name = 'company'),
		'email': _get_client_field(field_name = 'email'),
		'position': _get_client_field(field_name = 'position')
		}
	return client



def search_client(client_name):
	if _check_client_name(client_name = client_name):
		for idx, client in enumerate(clients):
			if client_name == client['name']:
				print('{uid} | {name} | {company} | {email} | {position}'.format(
				uid = idx,
				name = client['name'],
				company = client['company'],
				email = client['email'],
				position = client['position']))
	else:
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
	print(' [C]reate client \n [D]elete client \n [U]pdate client')
	print(' [S]earch Client \n [L]ist clients \n [E]xit')
	print('COMMAND: ')


if __name__ == '__main__':

	_initialize_clients_from_storage()

	while(True):
		print_welcome()
		command = input().upper()
		if command == 'C':
			client = client_input()
			create_client(client)

		elif command == 'D':
			delete_client(client_name = _get_client_name())

		elif command == 'U':
			update_client(_get_client_name())

		elif command == 'S':
			search_client(_get_client_name())

		elif command == 'L':
			list_clients()

		elif command == 'E':
			break
		else:
			print('Invalid command')


	_save_clients_to_storage()
