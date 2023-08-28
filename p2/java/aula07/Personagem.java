package aula07;

public class Personagem {
   private String nome;
   private String poder;
   private String objetivo;
   private String nomeReal;

   public Personagem(String nome, String poder, String objetivo, String nomeReal) {
      this.nome = nome;
      this.poder = poder;
      this.objetivo = objetivo;
      this.nomeReal = nomeReal;
   }

   public String getNome() {
      return nome;
   }

   public String getPoder() {
      return poder;
   }

   public String getObjetivo() {
      return objetivo;
   }

   public String getNomeReal() {
      return nomeReal;
   }

   public void apresentar(){
      System.out.println("Eu sou o " + getNome() + " Meu objetivo é: " + getObjetivo() + " O meu super poder é: " + getPoder() + "Mas meu nome real é " + getNomeReal());
   }

  
}
