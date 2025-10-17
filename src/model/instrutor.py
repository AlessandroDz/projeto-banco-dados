class Instrutor:
    def __init__(self,
                 id_instrutor: int = None,
                 nome: str = None,
                 especialidade: str = None,
                 telefone: str = None,
                 email: str = None):
        self.set_id_instrutor(id_instrutor)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_telefone(telefone)
        self.set_email(email)

    # Setters
    def set_id_instrutor(self, id_instrutor: int):
        self.id_instrutor = id_instrutor

    def set_nome(self, nome: str):
        self.nome = nome

    def set_especialidade(self, especialidade: str):
        self.especialidade = especialidade

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def set_email(self, email: str):
        self.email = email

    # Getters
    def get_id_instrutor(self) -> int:
        return self.id_instrutor

    def get_nome(self) -> str:
        return self.nome

    def get_especialidade(self) -> str:
        return self.especialidade

    def get_telefone(self) -> str:
        return self.telefone

    def get_email(self) -> str:
        return self.email

    # Representação
    def to_string(self):
        return (f"Instrutor: {self.get_id_instrutor()} | Nome: {self.get_nome()} | "
                f"Especialidade: {self.get_especialidade()} | Telefone: {self.get_telefone()} | "
                f"Email: {self.get_email()}")