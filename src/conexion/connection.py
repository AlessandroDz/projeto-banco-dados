"""import cx_Oracle

def get_connection():
    try:
        connection = cx_Oracle.connect(
            user="LABDATABASE",
            password="senha123",
            dsn="localhost:1521/XEPDB1"
        )
        return connection
    except cx_Oracle.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return None
"""