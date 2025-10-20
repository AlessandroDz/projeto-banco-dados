import oracledb

# === CONFIGURAÇÃO DA CONEXÃO ===
# Altere conforme seu ambiente Oracle
conexao = oracledb.connect(
    user="SEU_USUARIO",
    password="SUA_SENHA",
    dsn="localhost/XEPDB1"  #  DSN Oracle XE
)

cursor = conexao.cursor()

# === FUNÇÕES  TABELA ===

# INSERIR REGISTROS
def inserir_aluno():
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    nome = input("Nome do aluno: ")
    telefone = input("Telefone: ")

    sql = """
    INSERT INTO aluno (id_aluno, cpf, data_nascimento, nome_aluno, telefone)
    VALUES (aluno_seq.NEXTVAL, :1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4)
    """
    cursor.execute(sql, (cpf, data_nascimento, nome, telefone))
    conexao.commit()
    print("Aluno inserido com sucesso!")

def inserir_instrutor():
    nome = input("Nome do instrutor: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    sql = """
    INSERT INTO instrutor (id_instrutor, nome_instrutor, especialidade, telefone, email)
    VALUES (instrutor_seq.NEXTVAL, :1, :2, :3, :4)
    """
    cursor.execute(sql, (nome, especialidade, telefone, email))
    conexao.commit()
    print("Instrutor inserido com sucesso!")

def inserir_treino():
    id_aluno = input("ID do aluno: ")
    id_instrutor = input("ID do instrutor: ")
    modalidade = input("Modalidade: ")
    horario = input("Horário (HH:MM): ")
    dia_semana = input("Dia da semana: ")
    frequencia = input("Frequência semanal: ")

    sql = """
    INSERT INTO treino (id_treino, id_aluno, modalidade, horario, dia_semana, frequencia, id_instrutor)
    VALUES (treino_seq.NEXTVAL, :1, :2, TO_DATE(:3, 'HH24:MI'), :4, :5, :6)
    """
    cursor.execute(sql, (id_aluno, modalidade, horario, dia_semana, frequencia, id_instrutor))
    conexao.commit()
    print("Treino inserido com sucesso!")

# === REMOVER REGISTROS ===
def remover_registro(tabela):
    id_nome = input(f"Digite o ID do registro que deseja remover da tabela {tabela.upper()}: ")
    id_campo = f"id_{tabela.lower()}"
    sql = f"DELETE FROM {tabela} WHERE {id_campo} = :1"
    cursor.execute(sql, (id_nome,))
    conexao.commit()
    print(f"Registro da tabela {tabela} removido com sucesso!")

# === ATUALIZAR REGISTROS ===
def atualizar_aluno():
    id_aluno = input("ID do aluno a atualizar: ")
    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone: ")

    sql = """
    UPDATE aluno
    SET nome_aluno = :1, telefone = :2
    WHERE id_aluno = :3
    """
    cursor.execute(sql, (novo_nome, novo_telefone, id_aluno))
    conexao.commit()
    print("Aluno atualizado com sucesso!")

# === RELATÓRIOS ===
def relatorio_treinos():
    sql = """
    SELECT t.id_treino, a.nome_aluno, i.nome_instrutor, t.modalidade, t.horario, t.dia_semana
    FROM treino t
    JOIN aluno a ON a.id_aluno = t.id_aluno
    JOIN instrutor i ON i.id_instrutor = t.id_instrutor
    ORDER BY a.nome_aluno
    """
    cursor.execute(sql)
    print("\n--- RELATÓRIO DE TREINOS ---")
    for linha in cursor:
        print(linha)

# === MENU PRINCIPAL ===
def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Inserir registros")
        print("2. Remover registros")
        print("3. Atualizar registros")
        print("4. Relatórios")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n1. Aluno\n2. Instrutor\n3. Treino")
            tipo = input("Inserir em qual tabela? ")
            if tipo == "1":
                inserir_aluno()
            elif tipo == "2":
                inserir_instrutor()
            elif tipo == "3":
                inserir_treino()

        elif opcao == "2":
            print("\n1. Aluno\n2. Instrutor\n3. Treino")
            tipo = input("Remover de qual tabela? ")
            if tipo == "1":
                remover_registro("aluno")
            elif tipo == "2":
                remover_registro("instrutor")
            elif tipo == "3":
                remover_registro("treino")

        elif opcao == "3":
            atualizar_aluno()

        elif opcao == "4":
            relatorio_treinos()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()
cursor.close()
conexao.close()