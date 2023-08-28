package teste;

public class Main {
    public static void main(String[] args) {
        Personagem mario = new Personagem();
        Kart car = new Kart();
        mario.setCar(car);
        mario.Acelera(100);
    }
    
}
