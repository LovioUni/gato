from persistence.db import get_connection
from security.crypto import encrypt, decrypt

class Card:
    def __init__(self, id: int, numero: str, cvc: str, tipo: str, banco: str):
        self.id = id
        self.numero = numero
        self.cvc = cvc
        self.tipo = tipo
        self.banco = banco

        
    def insert_tarjeta(numero, cvc, tipo, banco):
        connection = get_connection()
        cursor = connection.cursor()

        numero_encrypt = encrypt(numero)

        sql = "INSERT INTO card (numero, cvc, tipo, banco) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (numero_encrypt, cvc, tipo, banco))
        connection.commit()

        cursor.close()
        connection.close()

    def get_cards():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        sql = "SELECT id, numero, cvc, tipo, banco FROM card"
        cursor.execute(sql)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        cards = []

        for row in rows:
            cards.append(
                Card(
                    id=row["id"],
                    numero=decrypt(row["numero"]),
                    cvc=row["cvc"],
                    tipo=row["tipo"],
                    banco=row["banco"]
                )
            )

        return cards