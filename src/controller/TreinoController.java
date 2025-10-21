import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class TreinoController {

    public static List<Treino> listarTodos() {
        List<Treino> lista = new ArrayList<>();
        String sql = "SELECT id_treino, id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia FROM treino ORDER BY id_treino";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Treino t = new Treino(
                        rs.getInt("id_treino"),
                        rs.getInt("id_aluno"),
                        rs.getInt("id_instrutor"),
                        rs.getString("tipo"),
                        rs.getString("horario"),
                        rs.getString("dias_semana"),
                        rs.getInt("frequencia")
                );
                lista.add(t);
            }
        } catch (SQLException e) {
            System.err.println("Erro ao listar treinos: " + e.getMessage());
        }
        return lista;
    }

    public static boolean inserir(int idAluno, int idInstrutor, String tipo, String horario, String diasSemana, int frequencia) {
        String sql = "INSERT INTO treino (id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia) VALUES (?, ?, ?, ?, ?, ?)";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, idAluno);
            ps.setInt(2, idInstrutor);
            ps.setString(3, tipo);
            ps.setString(4, horario);
            ps.setString(5, diasSemana);
            ps.setInt(6, frequencia);
            int rows = ps.executeUpdate();
            System.out.println("✅ Treino inserido com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao inserir treino: " + e.getMessage());
            return false;
        }
    }

    public static boolean deletar(int id) {
        String sql = "DELETE FROM treino WHERE id_treino = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Treino deletado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao deletar treino: " + e.getMessage());
            return false;
        }
    }

    public static boolean atualizar(int id, int idAluno, int idInstrutor, String tipo, String horario, String diasSemana, int frequencia) {
        String sql = "UPDATE treino SET id_aluno = ?, id_instrutor = ?, tipo = ?, horario = ?, dias_semana = ?, frequencia = ? WHERE id_treino = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, idAluno);
            ps.setInt(2, idInstrutor);
            ps.setString(3, tipo);
            ps.setString(4, horario);
            ps.setString(5, diasSemana);
            ps.setInt(6, frequencia);
            ps.setInt(7, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Treino atualizado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao atualizar treino: " + e.getMessage());
            return false;
        }
    }
}

