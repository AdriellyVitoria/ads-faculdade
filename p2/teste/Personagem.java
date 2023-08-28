package teste;

public class Personagem {
    String nome;
    Kart car;

    public Kart getCar() {
        return car;
    }

    public void setCar(Kart car) {
        this.car = car;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    void Acelera(int valor) {
        car.setAcelerar(valor);
    }
}
