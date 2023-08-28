public class Viajante {
    private Personagem personagem;

    public Viajante(Personagem personagem) {
        this.personagem = personagem;
    }

    public void setPersonagem(Personagem personagem) {
        this.personagem = personagem;
    }

    public void imprimirDetalhes() {
        personagem.imprimirDetalhes();
    }
}
