import java.util.ArrayList;

public class Familia {
    public String nome;
    public ArrayList<Personagem> membros = new ArrayList<Personagem>();
   // public Personagem membros;

    public void recebePersonagem(Personagem personagem){
        personagem.imprimirDetalhes();
    }

    public Familia(String nome) {
        this.nome = nome;
    }

    public void imprimirDetalhes() {
        System.out.println("Nome da familia: " + nome);
        System.out.println("Membros: " );
        for (Personagem pessoa : membros) {
            System.out.println(pessoa.getNome());
        }
    }
}
