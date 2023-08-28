 public class Teste {

    public static void main(String[] args) {
        Conta c = new Conta();

        c.saldo = 300;
        c.depositar = 500;

        try {
            c.sacar(400);
            c.deposiatar(500);

        } catch (Excessos e){
            System.out.println("Error")
        }   
    }
}