public class Funcionario {
    private String nome;
    private double salario;
    private int dataDeAdmissao;

    public Funcionario(String nome, double salario, int dataDeAdmissao) {
        this.nome = nome;
        this.salario = salario;
        this.dataDeAdmissao = dataDeAdmissao;
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
    public int getDataDeAdmissao() {
        return dataDeAdmissao;
    }
    public void setDataDeAdmissao(int dataDeAdmissao) {
        this.dataDeAdmissao = dataDeAdmissao;
    }
}
