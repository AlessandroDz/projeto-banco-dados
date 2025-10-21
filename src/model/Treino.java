public class Treino {
    private Integer idTreino;
    private Integer idAluno;
    private Integer idInstrutor;
    private String tipo;
    private String horario;
    private String diasSemana;
    private Integer frequencia;

    public Treino() {}

    public Treino(Integer idTreino, Integer idAluno, Integer idInstrutor, String tipo, String horario, String diasSemana, Integer frequencia) {
        this.idTreino = idTreino;
        this.idAluno = idAluno;
        this.idInstrutor = idInstrutor;
        this.tipo = tipo;
        this.horario = horario;
        this.diasSemana = diasSemana;
        this.frequencia = frequencia;
    }

    public Integer getIdTreino() { return idTreino; }
    public void setIdTreino(Integer idTreino) { this.idTreino = idTreino; }

    public Integer getIdAluno() { return idAluno; }
    public void setIdAluno(Integer idAluno) { this.idAluno = idAluno; }

    public Integer getIdInstrutor() { return idInstrutor; }
    public void setIdInstrutor(Integer idInstrutor) { this.idInstrutor = idInstrutor; }

    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }

    public String getHorario() { return horario; }
    public void setHorario(String horario) { this.horario = horario; }

    public String getDiasSemana() { return diasSemana; }
    public void setDiasSemana(String diasSemana) { this.diasSemana = diasSemana; }

    public Integer getFrequencia() { return frequencia; }
    public void setFrequencia(Integer frequencia) { this.frequencia = frequencia; }

    @Override
    public String toString() {
        return String.format("Treino: %s | Aluno: %s | Instrutor: %s | Tipo: %s | Horário: %s | Dias: %s | Frequência: %s",
                idTreino, idAluno, idInstrutor, tipo, horario, diasSemana, frequencia);
    }
}
