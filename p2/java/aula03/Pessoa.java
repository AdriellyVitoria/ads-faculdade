public class Pessoa {

    String nome;
    ContatoTelefone telefone;
    Enderenço enderenço;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public ContatoTelefone getTelefone() {
        return telefone;
    }
    public void setTelefone(ContatoTelefone telefone) {
        this.telefone = telefone;
    }
    public Enderenço getEnderenço() {
        return enderenço;
    }
    public void setEnderenço(Enderenço enderenço) {
        this.enderenço = enderenço;
    }
}
