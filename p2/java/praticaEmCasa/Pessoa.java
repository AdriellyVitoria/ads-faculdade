//Crie uma classe Pessoa com os atributos nome, idade e sexo. Crie um método para imprimir as informações da pessoa.
// Crie uma classe Pessoa com os atributos nome, idade e sexo. Crie classes filhas para representar homem e mulher, adicionando atributos específicos para cada uma das classes filhas e criando um método para imprimir as informações da pessoa

public class Pessoa {
    protected String nome;
    protected int idade;
    protected String sexo;
     
    // Contrutor 
    public Pessoa (String nome, int idade, String sexo) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
    }
    //Metodo para imprimir as imforçoes de pessoa 
    public void imprimirImformaçâo(){
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Sexo: " + sexo);
    }

        
}
