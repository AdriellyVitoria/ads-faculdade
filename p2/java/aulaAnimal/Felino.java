package aulaAnimal;

public class Felino extends Domestico {
    String dono;

    public Felino(String especie, String nome, String dono){
        super(especie, nome);
        this.dono = dono;
    }

    public void som() {
        System.out.println("miao");
    }
}
