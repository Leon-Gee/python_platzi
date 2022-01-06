clients = 'leon, oswaldo,'

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_coma()
	else:
		print('The client is already in the agenda!')
def _add_coma():
	global clients
	clients += ','


def list_clients():
	global clients
	print(clients)


def print_welcome():
	print('welcome to our client agenda')
	print('*'*50)
	print('What would you want to do today?:)')
	print('[C]reate client \n [D]elete client \n [U]pdate client')
	print('COMMAND: ')


def get_client_name():
	return input('What is the client name: ')

def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',',updated_client_name + ',')
	else:
		print('Client its not in the agenda')


if __name__ == '__main__':
	print_welcome()
	command = input().upper()

	if command == 'C':
		create_client(client_name = get_client_name())
		list_clients()

	elif command == 'D':
		pass

	elif command == 'U':
		new_client_name = input('Whats the new name of the client: ')
		update_client(client_name = get_client_name(), updated_client_name = new_client_name)
		list_clients()
	else:
		print('Invalid command')
