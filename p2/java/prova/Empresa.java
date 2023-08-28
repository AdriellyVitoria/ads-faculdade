public class Empresa {
    private String nome;
    private int cnpj;
    Departamento departamento;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getCnpj() {
        return cnpj;
    }
    public void setCnpj(int cnpj) {
        this.cnpj = cnpj;
    }
    public Departamento getDepartamento() {
        return departamento;
    }
    public void setDepartamento(Departamento departamento) {
        this.departamento = departamento;
    }

    public void nomeDaempresa(String nome){
        System.out.println("A empresa: " + nome );
       
    }
}
