// Crie uma classe Funcionario com os atributos nome, cargo e salário. Crie um método para calcular o aumento salarial de acordo com o cargo (gerente = 10%, supervisor = 5%, funcionário = 2%).
// Crie uma classe Funcionario com os atributos nome, cargo e salário. Crie uma classe filha para representar o gerente, adicionando um atributo para o bônus anual do gerente. Crie um método para calcular o salário anual do gerente.

public class Funcionario {
    protected String nome;
    protected String cargo;
    protected int  salario;

    public Funcionario(String nome, String cargo, int salario){
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }
    public String getCargo() {
        return cargo;
    }
    public int getSalario() {
        return salario;
    }

    public void CalcularAumento(){
        if(cargo == "G"){
            System.out.println("O seu salario "+nome +" Teve um aumento, e vc vai receber: " + salario + 10/100 );
        } else if (cargo == "S"){
            System.out.println("O seu salario "+nome +" Teve um aumento, e vc vai receber: " + salario + 5/100 );
        } else {
            System.out.println("O seu salario "+nome +" Teve um aumento, e vc vai receber: " + salario + 2/100 );
        }
}    
}
