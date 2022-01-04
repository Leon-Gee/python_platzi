clients = 'leon, oswaldo,'

def create_client(client_name):
	global clients
	clients += client_name
	_add_coma()

def _add_coma():
	global clients
	clients += ','


def list_clients():
	global clients
	print(clients)


if __name__ == '__main__':
	list_clients()
	create_client(client_name = 'oscar')
	list_clients()
