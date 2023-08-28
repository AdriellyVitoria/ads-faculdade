package aulaAnimal;

public class Domestico extends Animal{
    String nome;

    public Domestico(String especie, String nome) {
        super(especie);
        this.nome = nome;
    }

    public void som() {
        System.out.println("Animal não identificando");
    }
}
