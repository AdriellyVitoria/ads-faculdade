
package aula03;
import java.util.Scanner; //para importa entrada 
public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
    
            SeriesFavoritas s1 = new SeriesFavoritas();

            s1.setNome("Sur");
            Personagem p1 = new Personagem();

            p1.setNome("Deus");

            s1.setPersognagem(p1);
            p1.setSerie(s1);


            System.out.println(s1.getPersonagem().getNome());
            System.out.println(p1.getPersonagem().getNome());
    
    
        }
        // Scanner entrada = new Scanner(System.in);



        // #PEGAR STRING 
        // String nome;
        // System.out.println("Di");
        // nome = entrada.nextLine();

        // System.out.println("nome: " + nome);


        // #PARA COLOCAR A AS CASAS DECIMAS 
            // float a = 5;
            // System.out.printf("%.5f %n" , a);


        // #ENTRADA COM INT
        //  int a;
        //  int b;
        //  System.out.print("Digite o valor de a: ");
        //  a=entrada.nextInt();

        //  System.out.print("Digite o valor de b: ");
        //  b=entrada.nextInt();

        //  System.out.println("valor de a: " + "Valor de b: " + "Soma dos valores a e b: " + (a+b));
        
        
        // #vertores
         // int numeros[] = new int[2];
        // numeros [0] = 2;
        // numeros [1] = 7;

        // for (int i=0; i<=2; i++) {
        //     System.out.println(numeros [i]);
        // }
    }
