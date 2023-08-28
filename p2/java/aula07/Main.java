package aula07;

public class Main {
    public static void main(String[] args) {
      SuperHerois p1 = new SuperHerois(
        "Batma",
        "Ser rico",
        "ter um passa tempo ",
        "Bruce");
        p1.apresentar();

        Vilao v1 = new Vilao("Coringa",
        "Ser doido",
        "ver o cirgo pegar fogo",
        "Qualquer coisa");
        v1.apresentar();
        v1.lutar();
    }


  
}
