public class Personagem {
    // encapsulamento private
    private String nome;
    private int idade;
    private String familia;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {  
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getFamilia() {
        return familia;
    }

    public void setFamilia(String familia) {
        this.familia = familia;
    }

    public void imprimirDetalhes() {  //metodo
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Arvore Genealogica: " + familia);
    }
}