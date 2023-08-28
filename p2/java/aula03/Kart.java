public class Kart {
    Personagem personagem;
    String cor;

    //void setCor(String ){

    //}

    void setPersonagem(Personagem personagem) {
        this.personagem = personagem;
    }

    void setAcelerar(int valor) {
        System.out.println("Acelerar" + valor);
    }

    public void acelerado(int valor) { 
        System.out.println("Acelerou" + valor);
    }

    void freado(){
        System.out.println("Carro parou!");
    }

    void bateu() {
        System.out.println("Bateu!");
        personagem.perderPontos();
    }

    void pegarMoedas(){
        System.out.println("Pegou moeda!");
        personagem.ganharPontos();
    }
}
