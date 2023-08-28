//Crie classes filhas para representar homem e mulher, adicionando atributos específicos para cada uma das classes filhas e criando um método para imprimir as informações da pessoa
public class Mulher extends Pessoa {
    public String beleza;

    public Mulher(String nome, int idade, String sexo, String beleza) {
        super(nome, idade, sexo);
        this.beleza = beleza;
    }

    public void imprimir(){
        System.out.println("nome "+ nome+ " idade: "+idade+ " Sexo: " +sexo+ " beleza: " + beleza);
    }
}
