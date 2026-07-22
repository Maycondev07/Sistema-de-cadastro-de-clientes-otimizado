import os
import sqlite3
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_int(prompt, min_value=0, max_value=None):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            number = int(value)
            if number >= min_value and (max_value is None or number <= max_value):
                return number
        print('Entrada invalida. Tente novamente.')


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('Valor obrigatorio.')


def confirm(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in {'s', 'sim'}:
            return True
        if response in {'n', 'nao', 'nao', 'nao'}:
            return False
        print('Resposta invalida. Use s ou n.')


def only_digits(value):
    return bool(value) and value.isdigit()


def validate_cpf(cpf):
    if not only_digits(cpf) or len(cpf) != 11:
        return False

    def calc_digit(digits, weights):
        total = sum(int(d) * w for d, w in zip(digits, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    digits = cpf[:-2]
    digit1 = calc_digit(digits, range(len(digits) + 1, 1, -1))
    digit2 = calc_digit(digits + str(digit1), range(len(digits) + 2, 1, -1))
    return cpf[-2:] == f'{digit1}{digit2}'


def validate_cnpj(cnpj):
    if not only_digits(cnpj) or len(cnpj) != 14:
        return False

    def calc_digit(digits, weights):
        total = sum(int(d) * w for d, w in zip(digits, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    digits = cnpj[:-2]
    digit1 = calc_digit(digits, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    digit2 = calc_digit(digits + str(digit1), [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    return cnpj[-2:] == f'{digit1}{digit2}'


class ClientDB:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                cpf TEXT UNIQUE,
                cnpj TEXT UNIQUE
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def insert_client(self, name, cpf=None, cnpj=None):
        self.conn.execute(
            'INSERT INTO clients (name, cpf, cnpj) VALUES (?, ?, ?)',
            (name, cpf, cnpj)
        )
        self.conn.commit()

    def get_by_id(self, client_id):
        return self.conn.execute('SELECT * FROM clients WHERE id = ?', (client_id,)).fetchone()

    def get_by_cpf(self, cpf):
        return self.conn.execute('SELECT * FROM clients WHERE cpf = ?', (cpf,)).fetchone()

    def get_by_cnpj(self, cnpj):
        return self.conn.execute('SELECT * FROM clients WHERE cnpj = ?', (cnpj,)).fetchone()

    def list_all(self):
        return self.conn.execute('SELECT * FROM clients ORDER BY id').fetchall()


def register_client(db):
    while True:
        clear_screen()
        print('Cadastro de cliente')
        option = read_int('Tipo:\n1 - PF\n2 - PJ\n0 - Voltar\nOpcao: ', 0, 2)
        if option == 0:
            return

        name = read_text('Nome: ')

        if option == 1:
            cpf = read_text('CPF (11 digitos): ')
            if not validate_cpf(cpf):
                print('CPF invalido.')
                time.sleep(1)
                continue
            print(f'\nNome: {name}\nCPF: {cpf}')
            if not confirm('Confirmar cadastro? (s/n): '):
                continue
            try:
                db.insert_client(name=name, cpf=cpf)
                print('Cliente cadastrado com sucesso.')
                time.sleep(1)
                return
            except sqlite3.IntegrityError:
                print('CPF ja cadastrado.')
                time.sleep(1)
        else:
            cnpj = read_text('CNPJ (14 digitos): ')
            if not validate_cnpj(cnpj):
                print('CNPJ invalido.')
                time.sleep(1)
                continue
            print(f'\nNome: {name}\nCNPJ: {cnpj}')
            if not confirm('Confirmar cadastro? (s/n): '):
                continue
            try:
                db.insert_client(name=name, cnpj=cnpj)
                print('Cliente cadastrado com sucesso.')
                time.sleep(1)
                return
            except sqlite3.IntegrityError:
                print('CNPJ ja cadastrado.')
                time.sleep(1)


def search_client(db):
    while True:
        clear_screen()
        print('Buscar cliente')
        option = read_int('Buscar por:\n1 - ID\n2 - CPF\n3 - CNPJ\n0 - Voltar\nOpcao: ', 0, 3)
        if option == 0:
            return

        if option == 1:
            client = db.get_by_id(read_int('Digite o ID: '))
        elif option == 2:
            client = db.get_by_cpf(read_text('Digite o CPF: '))
        else:
            client = db.get_by_cnpj(read_text('Digite o CNPJ: '))

        if client is None:
            print('Cliente nao encontrado.')
        else:
            print(f"ID: {client['id']}")
            print(f"Nome: {client['name']}")
            print(f"CPF: {client['cpf'] or '-'}")
            print(f"CNPJ: {client['cnpj'] or '-'}")

        input('\nPressione Enter para continuar...')


def list_clients(db):
    clear_screen()
    clients = db.list_all()
    if not clients:
        print('Nenhum cliente cadastrado.')
    else:
        print('Lista de clientes')
        for client in clients:
            print(f"ID {client['id']} | Nome: {client['name']} | CPF: {client['cpf'] or '-'} | CNPJ: {client['cnpj'] or '-'}")
    input('\nPressione Enter para continuar...')


def main():
    db = ClientDB()
    try:
        while True:
            clear_screen()
            print('=' * 30)
            print('Base de clientes')
            print('=' * 30)
            option = read_int('1 - Cadastrar\n2 - Buscar\n3 - Listar\n0 - Sair\nOpcao: ', 0, 3)
            if option == 1:
                register_client(db)
            elif option == 2:
                search_client(db)
            elif option == 3:
                list_clients(db)
            else:
                clear_screen()
                print('Encerrando...')
                break
    finally:
        db.close()


if __name__ == '__main__':
    main()
