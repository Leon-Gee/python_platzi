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
	print('[C]reate client')
	print('[D]elete client')
	print('COMMAND: ')

if __name__ == '__main__':
	print_welcome()
	command = input().upper()

	if command == 'C':
		client_name = input('What is the client name: ')
		create_client(client_name = client_name)
		list_clients()
	if command == 'D':
		pass
	else:
		print('Invalid command')
