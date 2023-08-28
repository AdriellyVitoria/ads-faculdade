import javax.swing.*;
public class Teste extends JFrame {
    
        public MyFrame() {
            super("My JFrame");
            setSize(500, 500);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            getContentPane().setBackground(Color.BLUE); // Set the background color to blue
            setVisible(true);
        }
    
        public static void main(String[] args) {
            new MyFrame();
        }
    }
     
