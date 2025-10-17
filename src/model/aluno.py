from datetime import date
class Alunos:
    def __init__(self,
                 ID_ALUNO: int = None,
                 nome: str = None,
                 cpf: str=None,
                 data_nascimento: date=None,
                 telefone: str=None):
        
        self.set_ID_ALUNO = (ID_ALUNO)
        self.set_nome= (nome)
        self.set_cpf=(cpf)
        self.set_data_nascimento(data_nascimento)
        self.set_telefone(telefone)


    def set_ID_ALUNO(self,ID_ALUNO:int):
        self.ID_ALUNO = ID_ALUNO

    def set_nome(self,nome:str):
        self.nome = nome

    def set_cpf(self,cpf:str):
        self.cpf=cpf

    def set_data_nascimento(self,data_nascimento:date):
        self.data_nascimento =data_nascimento

    def set_telefone(self,telefone:str):
        self.telefone= telefone




    def get_ID_ALUNO(self) ->int:
        return self.ID_ALUNO

    def get_nome(self)->str:
        return self.nome

    def get_cpf(self)->str:
        return self.cpf

    def get_data_nascimento(self)-> date:
        return self.data_nascimento

    def get_telefone(self)-> str:
        return self.telefone
    




    def to_String(self) ->str:
        return f"ID: {self.get_ID_ALUNO()} | CPF: {self.get_cpf()} | Nome: {self.get_nome()} Data Nascimento: {self.get_data_nascimento()} | Telefone: {self.get_telefone()}"