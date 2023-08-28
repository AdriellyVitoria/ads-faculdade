import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Senha senha = new Senha();
        senha.setValor(2311);

        System.out.println("Digite a sua senha (entre 1000 e 9999): ");
        int tentativa = scanner.nextInt();

        if (tentativa == senha.getValor()) {
            System.out.println("Acesso permitido");
        } else {
            System.out.println("Acesso negado");
        }    
    }
}
