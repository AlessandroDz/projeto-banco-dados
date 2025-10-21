import java.sql.Date;

public class Aluno {
    private Integer idAluno;
    private String nome;
    private String cpf;
    private Date dataNascimento;
    private String telefone;

    public Aluno() {}

    public Aluno(Integer idAluno, String nome, String cpf, Date dataNascimento, String telefone) {
        this.idAluno = idAluno;
        this.nome = nome;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
        this.telefone = telefone;
    }

    public Integer getIdAluno() { return idAluno; }
    public void setIdAluno(Integer idAluno) { this.idAluno = idAluno; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getCpf() { return cpf; }
    public void setCpf(String cpf) { this.cpf = cpf; }

    public Date getDataNascimento() { return dataNascimento; }
    public void setDataNascimento(Date dataNascimento) { this.dataNascimento = dataNascimento; }

    public String getTelefone() { return telefone; }
    public void setTelefone(String telefone) { this.telefone = telefone; }

    @Override
    public String toString() {
        return String.format("ID: %s | CPF: %s | Nome: %s | Data Nasc: %s | Telefone: %s",
                idAluno, cpf, nome, dataNascimento, telefone);
    }
}


