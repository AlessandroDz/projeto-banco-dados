import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class InstrutorController {

    public static List<Instrutor> listarTodos() {
        List<Instrutor> lista = new ArrayList<>();
        String sql = "SELECT id_instrutor, nome, especialidade, telefone, email FROM instrutor ORDER BY id_instrutor";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Instrutor i = new Instrutor(
                        rs.getInt("id_instrutor"),
                        rs.getString("nome"),
                        rs.getString("especialidade"),
                        rs.getString("telefone"),
                        rs.getString("email")
                );
                lista.add(i);
            }
        } catch (SQLException e) {
            System.err.println("Erro ao listar instrutores: " + e.getMessage());
        }
        return lista;
    }

    public static Instrutor buscarPorId(int id) {
        Instrutor instrutor = null;
        String sql = "SELECT id_instrutor, nome, especialidade, telefone, email FROM instrutor WHERE id_instrutor = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    instrutor = new Instrutor(
                            rs.getInt("id_instrutor"),
                            rs.getString("nome"),
                            rs.getString("especialidade"),
                            rs.getString("telefone"),
                            rs.getString("email")
                    );
                }
            }
        } catch (SQLException e) {
            System.err.println("Erro ao buscar instrutor por ID: " + e.getMessage());
        }
        return instrutor;
    }

    public static boolean inserir(String nome, String especialidade, String telefone, String email) {
        String sql = "INSERT INTO instrutor (nome, especialidade, telefone, email) VALUES (?, ?, ?, ?)";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, nome);
            ps.setString(2, especialidade);
            ps.setString(3, telefone);
            ps.setString(4, email);
            int rows = ps.executeUpdate();
            System.out.println("✅ Instrutor inserido com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao inserir instrutor: " + e.getMessage());
            return false;
        }
    }

    public static boolean atualizar(int id, String nome, String especialidade, String telefone, String email) {
        String sql = "UPDATE instrutor SET nome = ?, especialidade = ?, telefone = ?, email = ? WHERE id_instrutor = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, nome);
            ps.setString(2, especialidade);
            ps.setString(3, telefone);
            ps.setString(4, email);
            ps.setInt(5, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Instrutor atualizado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao atualizar instrutor: " + e.getMessage());
            return false;
        }
    }

    public static boolean deletar(int id) {
        String sql = "DELETE FROM instrutor WHERE id_instrutor = ?";
        try (Connection conn = ConnectionFactory.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            int rows = ps.executeUpdate();
            System.out.println("✅ Instrutor deletado com sucesso!");
            return rows > 0;
        } catch (SQLException e) {
            System.err.println("Erro ao deletar instrutor: " + e.getMessage());
            return false;
        }
    }
}
