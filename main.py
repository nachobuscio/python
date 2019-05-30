import sys
clientes = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',

    },
    {
        'name': 'Ricardo',
        'company': 'Oracle',
        'email': 'pablo@Oracle.com',
        'position': 'Data engineer',

    },
    {
        'name': 'Jose',
        'company': 'Facebok',
        'email': 'pablo@Facebok.com',
        'position': 'Software engineer',

    },
]

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


def delete_cliente(client):
    global clientes
    print(client)
    print(clientes['name'])
    if client in clientes['name']:
        clientes = clientes.remove(client)
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
        print('{uid}| {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = cliente['name'],
            company = cliente['company'],
            email = cliente['email'],
            position = cliente['position']
        ))


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field


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
    print('[L]List')
    print('[S]erch')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_cliente(client)
        list_cliente()
    elif command == 'D':
            client = {
                'name': _get_client_field('name'),
            }
            delete_cliente(client)
            list_cliente()
    elif command == 'U':
            cliente_name = get_cliente_name()
            update_client_name = get_cliente_name()
            update_client(cliente_name, update_client_name)
            list_cliente()
    elif command == 'L':
            list_cliente()
    elif command == 'S':
            cliente_name = get_cliente_name()
            found = search_client(cliente_name)
            if found:
                print('The client: {} is in cliente\'s list'.format(cliente_name))
            else:
                print('The client: {} is not in our client\'s list'.format(cliente_name) )

    else:
        Print('Error')
