import java.util.Scanner;
public class Main {

    public static void main(String[] args) {

        Pessoa p1 = new Pessoa();
        Enderenço e1 = new Enderenço();
        ContatoTelefone c1 = new ContatoTelefone();

        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite um nome: ");
        p1.setNome(entrada.nextLine());
        System.out.print("Qual o seu enderenço: ");
        e1.setBairro(entrada.nextLine());
        System.out.println("Digite o contado: ");
        c1.setGmail(entrada.nextLine());
        
        System.out.println(p1.getNome());
        System.out.println(e1.getBairro());
        System.out.println(c1.getGmail());
       
         // Personagem p1 = new Personagem();
        // Kart car = new Kart();

        // p1.setNome("Mario");
        // p1.setCar(car);
        // //car.setCor("vermelho");
        // car.setPersonagem(p1);
        // p1.acelera(100);   
        // p1.acelera(80);
        // car.bateu();


             
    
        }

    }
