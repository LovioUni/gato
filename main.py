from entities.user import User
from getpass import getpass

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
    print("Inicio de sesion")
    if login():
        print("Seleccione una opción del menú")
        print("1.- Registrar un usuario")
        print("2.- Consultar usuarios")
        option = int(input())
        if option == 1:
            register_user()
        if option == 2:
            view_users()
    else:
        print("Credenciales invalidas")
