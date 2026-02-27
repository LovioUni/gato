from entities.user import User
from entities.card import Card
from getpass import getpass
from security.crypto import generate_key

def register_card():
    numero = input("Numero de tarjeta: ")
    cvc = input("CVC: ")
    print("Seleccione si es credito o debito.")
    tipo = input("Tipo: ")
    banco = input("Banco: ")

    Card.insert_tarjeta(numero, cvc, tipo, banco)
    print("Tarjeta registrada.")

def register_user():
    name = input("Nombre: ")
    curp = input("CURP: ")
    account = input("Cuenta: ")

    if User.verify_account(account):
        print("La cuenta ya existe.")
        return

    password = getpass("Contraseña: ")
    
    User.insert(name, curp, account, password)
    print("Listo, registrado.")

def view_users():
    users = User.get_users()
    for user in users:
        print(f"ID: {user.id} | Nombre: {user.name} | Cuenta: {user.account} | CURP: {user.curp}")

def view_card():
    cards = Card.get_cards()
    for card in cards:
        print(f"ID: {card.id} | Numero: {card.numero} | CVC: {card.cvc} | Tipo: {card.tipo} | Banco: {card.banco}")

def login():
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")

    user = User.get_user_by_account(account)
    if user and user.password == password:
        return True
    else:
        return False
    
    #return user and user.password == password   <--- esto es lo mismo que lo de arriba

if __name__ == "__main__":
    generate_key()
    print("Inicio de sesion")
    if login():
        print("Seleccione una opción del menú")
        print("1.- Registrar un usuario")
        print("2.- Consultar usuarios")
        print("3.- Registrar tarjeta")
        print("4.- Consultar tarjeta")
        option = int(input())
        if option == 1:
            register_user()
        if option == 2:
            view_users()
        if option == 3:
            register_card()
        if option == 4:
            view_card()
    else:
        print("Credenciales invalidas")
