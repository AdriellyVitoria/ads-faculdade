public class Funcionario {
    private String nome;
    private double salario;
    private int data;

    public Funcionario(double salario, int data) {
        this.salario = salario;
        this.data = data;
    }
    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }
    public int getData() {
        return data;
    }
    public void setData(int data) {
        this.data = data;
    }
}
