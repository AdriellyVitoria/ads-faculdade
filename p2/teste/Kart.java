package teste;

public class Kart {
    Personagem personagem;
    void setPersonagem(Personagem personagem){
        this.personagem = personagem;
    }
    void setAcelerar(int valor) {
        System.out.println("Acelerou"  + valor) ;
    }
}
