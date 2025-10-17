class Treino:
    def __init__(self,
                 id_treino: int = None,
                 id_aluno: int = None,
                 id_instrutor: int = None,
                 tipo: str = None,
                 horario: str = None,
                 dias_semana: str = None,
                 frequencia: int = 0):
        self.set_id_treino(id_treino)
        self.set_id_aluno(id_aluno)
        self.set_id_instrutor(id_instrutor)
        self.set_tipo(tipo)
        self.set_horario(horario)
        self.set_dias_semana(dias_semana)
        self.set_frequencia(frequencia)

    # Setters
    def set_id_treino(self, id_treino: int):
        self.id_treino = id_treino

    def set_id_aluno(self, id_aluno: int):
        self.id_aluno = id_aluno

    def set_id_instrutor(self, id_instrutor: int):
        self.id_instrutor = id_instrutor

    def set_tipo(self, tipo: str):
        self.tipo = tipo

    def set_horario(self, horario: str):
        self.horario = horario

    def set_dias_semana(self, dias_semana: str):
        self.dias_semana = dias_semana

    def set_frequencia(self, frequencia: int):
        self.frequencia = frequencia

    # Getters
    def get_id_treino(self) -> int:
        return self.id_treino

    def get_id_aluno(self) -> int:
        return self.id_aluno

    def get_id_instrutor(self) -> int:
        return self.id_instrutor

    def get_tipo(self) -> str:
        return self.tipo

    def get_horario(self) -> str:
        return self.horario

    def get_dias_semana(self) -> str:
        return self.dias_semana

    def get_frequencia(self) -> int:
        return self.frequencia

    # Representação
    def to_string(self):
        return (f"Treino: {self.get_id_treino()} | Aluno: {self.get_id_aluno()} | "
                f"Instrutor: {self.get_id_instrutor()} | Tipo: {self.get_tipo()} | "
                f"Horário: {self.get_horario()} | Dias: {self.get_dias_semana()} | "
                f"Frequência: {self.get_frequencia()}")
