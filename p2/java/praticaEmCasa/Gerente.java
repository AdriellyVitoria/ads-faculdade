// Crie uma classe Funcionario com os atributos nome, cargo e salário. Crie uma classe filha para representar o gerente, adicionando um atributo para o bônus anual do gerente. Crie um método para calcular o salário anual do gerente.

public class Gerente extends Funcionario {

    public double bonusAnual;

    public Gerente(String nome, String cargo, int salario, double bonusAnual) {
        super(nome, cargo, salario);
        this.bonusAnual = bonusAnual;
    }

    public double getBonusAnual() {
        return bonusAnual;
    } 

    public void calcularSalario() {
        System.out.println("O gerente " + nome +" Vai receber "+ (salario+bonusAnual));
    }
}
