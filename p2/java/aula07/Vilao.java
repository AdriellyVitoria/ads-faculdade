package aula07;

public class Vilao extends SuperHerois {

   public Vilao(String nome, String poder, String objetivo, String nomeReal) {
        super(nome, poder, objetivo, nomeReal);  
    }

    public void lutar(Vilao vilao) {
        System.out.println(getNome() + " Está lutando contra " + vilao.getNome() );
     }

}
