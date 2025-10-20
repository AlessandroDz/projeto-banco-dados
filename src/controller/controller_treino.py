from connection import get_connection
from models.treino import Treino

class TreinoController:
    @staticmethod
    def listar_todos():
        conn = get_connection()
        treinos = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM LABDATABASE.TREINO")
            for row in cur:
                treinos.append(Treino(*row))
            cur.close()
            conn.close()
        return treinos

    @staticmethod
    def inserir(id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia):
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO LABDATABASE.TREINO 
                (ID_TREINO, ID_ALUNO, ID_INSTRUTOR, TIPO, HORARIO, DIAS_SEMANA, FREQUENCIA)
                VALUES (LABDATABASE.TREINO_ID_SEQ.NEXTVAL, :1, :2, :3, :4, :5, :6)
            """, (id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia))
            conn.commit()
            cur.close()
            conn.close()
            print("Treino inserido com sucesso!")
