public class Prof {
    private String nome;
    private int cpf;
   
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCpf() {
        return cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public void mostraDados(String nome, int cpf){
        System.out.println("O prof: " + nome + " Com o numero de cpf " + cpf );
    }
}
