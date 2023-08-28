import java.util.Scanner;

public class Departamento {
    private String nome;
    Funcionario funcionario;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public Funcionario getFuncionario() {
        return funcionario;
    }
    public void setFuncionario(Funcionario funcionario) {
        this.funcionario = funcionario;
    }

    public void organizacao(){
        Scanner entrada = new Scanner(System.in);

        System.out.print("nome do funcionario: ");
        String nome = entrada.nextLine();

        System.out.println("O funcionario " + nome + " E de qual derparamento é o funcionario");

        System.out.println("Financeiro [F] marketing [M] Servoço ao cliente[S]");
        String derpatamento = entrada.nextLine();
        System.out.println(derpatamento);

        if (derpatamento == "F"){
            System.out.println("teve uma aumento de 10%");
        } else {
            System.out.println("Sem aumento");
        }
    }

    public void Funcionario(Funcionario funcionario ){
        System.out.println(nome);
    }
}
