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

def create_client(cliente_name):
    global clientes
    if cliente_name not in clientes:
        clientes.append(cliente_name)
    else:
        print('Client already is in client\'s list')



def update_client(client_name, update_client_name):
    global clientes, esta
    esta = 'N'
    for idx, client in enumerate(clientes):
        if client['name'] == client_name['name']:
            client['name'] =  update_client_name['name']
            esta = 'S'
            break

    if esta == 'N':
        print('Client is not in clientes list')



def delete_client(client_name):
    global clientes, esta

    esta = 'N'
    for idx, client in enumerate(clientes):
        if client['name'] == client_name['name']:
            del clientes[idx]
            esta = 'S'
            break

    if esta == 'N':
        print('Client is not in clientes list')


def search_client(client_name):
    global clientes, esta
    esta = 'N'
    for idx, client in enumerate(clientes):
        if client['name'] == client_name['name']:
            print('{uid}| {name} | {company} | {email} | {position}'.format(
                uid = idx,
                name = client['name'],
                company = client['company'],
                email = client['email'],
                position = client['position']
            ))
            esta = 'S'
            break

    if esta == 'N':
        print('Client is not in clientes list')


def list_client():
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
        create_client(client)
        list_client()
    elif command == 'D':
            client = {
                'name': _get_client_field('name'),
            }
            delete_client(client)
            list_client()
    elif command == 'U':
            esta = 'N'
            client_name = {
                'name': _get_client_field('name'),
            }
            update_client_name = {
                'name': _get_client_field('name'),
            }

            for idx, client in enumerate(clientes):
                if client['name'] == client_name['name']:
                    client['name'] =  update_client_name['name']
                    esta = 'S'
                    break

            if esta == 'N':
                print('Client is not in clientes list')
            else:
                list_client()
    elif command == 'L':
            list_client()
    elif command == 'S':
            client = {
                'name': _get_client_field('name'),
            }
            search_client(client)

    else:
        Print('Error')
