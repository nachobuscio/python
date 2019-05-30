import sys
clientes = ['Pablo', 'Ricardo', 'José', 'Ignacio']

def create_cliente(cliente_name):
    global clientes
    if cliente_name not in clientes:
        clientes.append(cliente_name)
    else:
        print('Client already is in client\'s list')


def update_client(cliente_name, update_client_name):
    global clientes
    if cliente_name in clientes:
        index = clientes.index(cliente_name)
        clientes[index] = update_client_name
    else:
        print('Client is not in clientes list')


def delete_cliente(delete_cliente_name):
    global clientes
    if delete_cliente_name in clientes:
        clientes = clientes.remove(delete_cliente_name)
    else:
        print('Client is not in clientes list')

def search_client(cliente_name):
    global clientes
    for client in clientes:
        if cliente_name != clientes:
            continue
        else:
            return True



def list_cliente():
    for idx, cliente in enumerate(clientes):
        print('{}:{}'.format(idx, cliente))

def get_cliente_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('Whats would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[P]Prueba')
    print('[S]erch')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        cliente_name = get_cliente_name()
        create_cliente(cliente_name)
        list_cliente()
    elif command == 'D':
            delete_cliente_name = get_cliente_name()
            delete_cliente(delete_cliente_name)
            list_cliente()
    elif command == 'U':
            cliente_name = get_cliente_name()
            update_client_name = get_cliente_name()
            update_client(cliente_name, update_client_name)
            list_cliente()
    elif command == 'P':
            var = 'Hola como estas?'
            var2 = var[::-1]
            print(var2)
    elif command == 'S':
            cliente_name = get_cliente_name()
            found = search_client(cliente_name)
            if found:
                print('The client: {} is in cliente\'s list'.format(cliente_name))
            else:
                print('The client: {} is not in our client\'s list'.format(cliente_name) )

    else:
        Print('Error')
