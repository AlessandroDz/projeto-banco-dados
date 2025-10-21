import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class AlunoController {

    public static List<Aluno> listarTodos() {
        List<Aluno> alunos = new ArrayList<>();
        String sql = "SELECT id_aluno, nome, cpf, data_nascimento, telefone FROM aluno ORDER BY id_aluno";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Aluno a = new Aluno(
                        rs.getInt("id_aluno"),
                        rs.getString("nome"),
                        rs.getString("cpf"),
                        rs.getDate("data_nascimento"),
                        rs.getString("telefone")
                );
                alunos.add(a);
            }
        } catch (SQLException e) {
            System.err.println("Erro ao listar alunos: " + e.getMessage());
        }
        return alunos;
    }

    public static Aluno buscarPorId(int id) {
        Aluno aluno = null;
        String sql = "SELECT id_aluno, nome, cpf, data_nascimento, telefone FROM aluno WHERE id_aluno = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    aluno = new Aluno(
                            rs.getInt("id_aluno"),
                            rs.getString("nome"),
                            rs.getString("cpf"),
                            rs.getDate("data_nascimento"),
                            rs.getString("telefone")
                    );
                }
            }
        } catch (SQLException e) {
            System.err.println("Erro ao buscar aluno por ID: " + e.getMessage());
        }
        return aluno;
    }

    public static boolean inserir(String nome, String cpf, Date dataNascimento, String telefone) {
        String sql = "INSERT INTO aluno (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, nome);
            ps.setString(2, cpf);
            ps.setDate(3, dataNascimento);
            ps.setString(4, telefone);
            int rows = ps.executeUpdate();
            System.out.println("✅ Aluno inserido com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao inserir aluno: " + e.getMessage());
            return false;
        }
    }

    public static boolean atualizar(int id, String nome, String cpf, Date dataNascimento, String telefone) {
        String sql = "UPDATE aluno SET nome = ?, cpf = ?, data_nascimento = ?, telefone = ? WHERE id_aluno = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, nome);
            ps.setString(2, cpf);
            ps.setDate(3, dataNascimento);
            ps.setString(4, telefone);
            ps.setInt(5, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Aluno atualizado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao atualizar aluno: " + e.getMessage());
            return false;
        }
    }

    public static boolean deletar(int id) {
        String sql = "DELETE FROM aluno WHERE id_aluno = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Aluno deletado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao deletar aluno: " + e.getMessage());
            return false;
        }
    }
}
