from conexion import get_connection
from model.aluno import Alunos

class AlunoController:

    @staticmethod
    def listar_todos():
        alunos = []
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ID_ALUNO, NOME, CPF, DATA_NASCIMENTO, TELEFONE
                    FROM LABDATABASE.ALUNO
                    ORDER BY ID_ALUNO
                """)
                for row in cur:
                    aluno = Alunos(*row)
                    alunos.append(aluno)
        except Exception as e:
            print(f"Erro ao listar alunos: {e}")
        finally:
            if conn:
                conn.close()
        return alunos


    @staticmethod
    def buscar_por_id(id_aluno):
        aluno = None
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT ID_ALUNO, NOME, CPF, DATA_NASCIMENTO, TELEFONE
                    FROM LABDATABASE.ALUNO
                    WHERE ID_ALUNO = :1
                """, (id_aluno,))
                row = cur.fetchone()
                if row:
                    aluno = Alunos(*row)
        except Exception as e:
            print(f"Erro ao buscar aluno por ID: {e}")
        finally:
            if conn:
                conn.close()
        return aluno


    @staticmethod
    def inserir(nome, cpf, data_nascimento, telefone):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO LABDATABASE.ALUNO
                    (ID_ALUNO, NOME, CPF, DATA_NASCIMENTO, TELEFONE)
                    VALUES (LABDATABASE.ALUNO_ID_SEQ.NEXTVAL, :1, :2, :3, :4)
                """, (nome, cpf, data_nascimento, telefone))
                conn.commit()
            print("Aluno inserido com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao inserir aluno: {e}")
            return False
        finally:
            if conn:
                conn.close()


    @staticmethod
    def atualizar(id_aluno, nome=None, cpf=None, data_nascimento=None, telefone=None):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE LABDATABASE.ALUNO
                    SET NOME = :1,
                        CPF = :2,
                        DATA_NASCIMENTO = :3,
                        TELEFONE = :4
                    WHERE ID_ALUNO = :5
                """, (nome, cpf, data_nascimento, telefone, id_aluno))
                conn.commit()
            print(" Aluno atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao atualizar aluno: {e}")
            return False
        finally:
            if conn:
                conn.close()


    @staticmethod
    def deletar(id_aluno):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM LABDATABASE.ALUNO
                    WHERE ID_ALUNO = :1
                """, (id_aluno,))
                conn.commit()
            print(" Aluno deletado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao deletar aluno: {e}")
            return False
        finally:
            if conn:
                conn.close()