public class Instrutor {
    private Integer idInstrutor;
    private String nome;
    private String especialidade;
    private String telefone;
    private String email;

    public Instrutor() {}

    public Instrutor(Integer idInstrutor, String nome, String especialidade, String telefone, String email) {
        this.idInstrutor = idInstrutor;
        this.nome = nome;
        this.especialidade = especialidade;
        this.telefone = telefone;
        this.email = email;
    }

    public Integer getIdInstrutor() { return idInstrutor; }
    public void setIdInstrutor(Integer idInstrutor) { this.idInstrutor = idInstrutor; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEspecialidade() { return especialidade; }
    public void setEspecialidade(String especialidade) { this.especialidade = especialidade; }

    public String getTelefone() { return telefone; }
    public void setTelefone(String telefone) { this.telefone = telefone; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    @Override
    public String toString() {
        return String.format("Instrutor: %s | Nome: %s | Especialidade: %s | Telefone: %s | Email: %s",
                idInstrutor, nome, especialidade, telefone, email);
    }
}

