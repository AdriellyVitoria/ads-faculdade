//Crie uma classe Aluno com os atributos nome, idade e média. Crie um método para calcular a situação do aluno (se a média é maior ou igual a 7, o aluno está aprovado; caso contrário, está reprovado).

public class Aluno {
    protected String nome;
    protected int idade;
    protected double media;

    public Aluno(String nome, int idade, double media){
        this.nome = nome;
        this.idade = idade;
        this.media = media;
    }

    public void calcularmedia(){
        if(media >= 7.0) {
            System.out.println("O " + nome + " Foi aprovado");
        } else{
            System.out.println("O " + nome + " Foi reprovado");
        }
    }

}
