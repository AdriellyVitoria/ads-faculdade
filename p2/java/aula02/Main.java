// new vai falar que é um objeto e vai atribuir um novo metodo
package aula02;

public class Main {
    public static void main(String[] args) {
        Carro carro1;
        carro1 = new Carro();

        carro1.cor = "vermelho";
        carro1.ano = 2021;

        System.out.println("Cor: " + carro1.cor);
        System.out.println("Ano: " + carro1.ano);

        Carro carro2 = new Carro();
        carro2.cor = "Azul";
        carro2.ano = 2020;

        System.out.println("Cor: " + carro2.cor);
        System.out.println("Ano: " + carro2.ano);

        Pessoa pessoa1;
        pessoa1 = new Pessoa();

        pessoa1.nome = "Adrielly";
        pessoa1.idade = 20;
        pessoa1.peso = 50.2;

        System.out.println("nome: " + pessoa1.nome);
        
    }
}
