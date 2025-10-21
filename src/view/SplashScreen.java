import java.awt.*;
import javax.swing.*;

public class SplashScreen extends JWindow {
    public SplashScreen(int millis) {
        JPanel content = (JPanel) getContentPane();
        content.setBackground(Color.white);

        int width = 400;
        int height = 160;
        Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (screen.width - width) / 2;
        int y = (screen.height - height) / 2;
        setBounds(x, y, width, height);

        JLabel label = new JLabel("Academia - Carregando..."); 
        label.setFont(new Font("SansSerif", Font.BOLD, 18));
        label.setHorizontalAlignment(SwingConstants.CENTER);

        JLabel subtitle = new JLabel("Sistema LabFit"); 
        subtitle.setFont(new Font("SansSerif", Font.PLAIN, 12));
        subtitle.setHorizontalAlignment(SwingConstants.CENTER);

        JProgressBar progressBar = new JProgressBar();
        progressBar.setIndeterminate(false);
        progressBar.setStringPainted(true);

        content.setLayout(new BorderLayout());
        content.add(label, BorderLayout.NORTH);
        content.add(subtitle, BorderLayout.CENTER);
        content.add(progressBar, BorderLayout.SOUTH);

        setVisible(true);

        try {
            int steps = 80;
            for (int i = 0; i <= steps; i++) {
                progressBar.setValue(i);
                Thread.sleep(millis / steps);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        setVisible(false);
        dispose();
    }
}

