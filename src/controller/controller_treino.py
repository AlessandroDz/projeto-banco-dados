from conexion import get_connection
from model.treino import Treino

class TreinoController:
    @staticmethod
    def listar_todos():
        treinos = []
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ID_TREINO, ID_ALUNO, ID_INSTRUTOR, TIPO, HORARIO, DIAS_SEMANA, FREQUENCIA
                    FROM TREINO
                """)
                for row in cur:
                    treinos.append(Treino(*row))
        except Exception as e:
            print(f"Erro ao listar treinos: {e}")
        finally:
            if conn:
                conn.close()
        return treinos

    @staticmethod
    def inserir(id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO TREINO 
                    (ID_TREINO, ID_ALUNO, ID_INSTRUTOR, TIPO, HORARIO, DIAS_SEMANA, FREQUENCIA)
                    VALUES (TREINO_ID_SEQ.NEXTVAL, :1, :2, :3, :4, :5, :6)
                """, (id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia))
                conn.commit()
            print("Treino inserido com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")
            return False
        finally:
            if conn:
                conn.close()
