
//import java.util.Scanner;
class Personagem {
   private String nome;
   private Kart car;
   private int pontos = 0;
   
   public Kart getCar() {
      return car;
   }

   public void setCar (Kart car) {
      this.car = car;
   }

   public String getNome() {
      return nome;
   }
   public void setNome(String nome) {
      this.nome = nome;
   }
   public void acelera(int valor){
      car.acelerado(valor);
   }

   void perderPontos() {
      pontos = pontos - 100;
   }

   void ganharPontos(){
      pontos = pontos + 100;
   }

   void frea(){
      car.freado();
   }
   void pontos(){

   }
}
