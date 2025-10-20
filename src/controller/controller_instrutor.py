from conexion.queries import OracleQueries
from conexion import get_connection
from model.instrutor import Instrutor

class InstrutorController:

    @staticmethod
    def listar_todos():
        instrutores = []
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT ID_INSTRUTOR, NOME, ESPECIALIDADE, TELEFONE, EMAIL
                FROM LABDATABASE.INSTRUTOR
                ORDER BY ID_INSTRUTOR
            """)
            for row in cur:
                instrutor = Instrutor(*row)
                instrutores.append(instrutor)
        except Exception as e:
            print(f"Erro ao listar instrutores: {e}")
        finally:
            if cur:
                try:
                    cur.close()
                except Exception:
                    pass
            if conn:
                conn.close()
        return instrutores


    @staticmethod
    def buscar_por_id(id_instrutor):
        instrutor = None
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT ID_INSTRUTOR, NOME, ESPECIALIDADE, TELEFONE, EMAIL
                FROM LABDATABASE.INSTRUTOR
                WHERE ID_INSTRUTOR = :1
            """, (id_instrutor,))
            row = cur.fetchone()
            if row:
                instrutor = Instrutor(*row)
        except Exception as e:
            print(f"Erro ao buscar instrutor por ID: {e}")
        finally:
            if cur:
                try:
                    cur.close()
                except Exception:
                    pass
            if conn:
                conn.close()
        return instrutor


    @staticmethod
    def inserir(nome, especialidade, telefone, email):
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO LABDATABASE.INSTRUTOR
                (ID_INSTRUTOR, NOME, ESPECIALIDADE, TELEFONE, EMAIL)
                VALUES (LABDATABASE.INSTRUTOR_ID_SEQ.NEXTVAL, :1, :2, :3, :4)
            """, (nome, especialidade, telefone, email))
            conn.commit()
            print("Instrutor inserido com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao inserir instrutor: {e}")
            return False
        finally:
            if cur:
                try:
                    cur.close()
                except Exception:
                    pass
            if conn:
                conn.close()


    @staticmethod
    def atualizar(id_instrutor, nome=None, especialidade=None, telefone=None, email=None):
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE LABDATABASE.INSTRUTOR
                SET NOME = :1,
                    ESPECIALIDADE = :2,
                    TELEFONE = :3,
                    EMAIL = :4
                WHERE ID_INSTRUTOR = :5
            """, (nome, especialidade, telefone, email, id_instrutor))
            conn.commit()
            print("Instrutor atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao atualizar instrutor: {e}")
            return False
        finally:
            if cur:
                try:
                    cur.close()
                except Exception:
                    pass
            if conn:
                conn.close()


    @staticmethod
    def deletar(id_instrutor):
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM LABDATABASE.INSTRUTOR
                WHERE ID_INSTRUTOR = :1
            """, (id_instrutor,))
            conn.commit()
            print("Instrutor deletado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao deletar instrutor: {e}")
            return False
        finally:
            if cur:
                try:
                    cur.close()
                except Exception:
                    pass
            if conn:
                conn.close()