public class Filho extends Personagem{
    public String pai;
    public String mae;

    public Filho(String nome, int idade,  Familia familia){
        super(nome, idade, familia);
    }

    public Filho(String nome, int idade, Familia familia, String pai, String mae) {
        super(nome, idade, familia);
        this.pai = pai;
        this.mae = mae;
    }

    public void imprimirDetalhes() {
        super.imprimirDetalhes();
        System.out.println("Pai: " + pai);
        System.out.println("Mãe: " + mae);
    }

    public void imprimirDetalhes(String pai, String mae){
        this.pai = pai;
        this.mae = mae;
        super.imprimirDetalhes();
        System.out.println("pai: " + pai);
        System.out.println("mae: " + mae);
        
    }
}
