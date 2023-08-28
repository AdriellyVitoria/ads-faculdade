package aula03;
import java.util.Scanner;
public class Series {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Gostaria: ");
        int quantidade = entrada.nextLine();

        SeriesFavoritas series[] = new SeriesFavoritas[2];
        for (int i = 0; i < 2; i++) {
                series[i] = new SeriesFavoritas();
                SeriesFavoritas series = new SeriesFavoritas();
                System.out.println("Diga me sua series favorita: ");
                series.nome = entrada.nextLine();

                System.out.print("Qual o genero da serie " + series.nome + ": ");
                series.genero = entrada.nextLine();
        
                System.out.print("Quantas tempora a serie " + series.nome + " tem: ");
                series.temp = entrada.nextInt();
        
                System.out.println("Sua serie favorita é: " + series.nome + "\nO genero é " + series.genero + "\nE são " + series.temp);
        }
        // SeriesFavoritas series = new SeriesFavoritas();

        // int perguntar;
        // System.out.println("Quantas series vc deseja add? ");
        // perguntar = entrada.nextInt();

        // int i = 1;
        // for (i = 1; i < perguntar; i++ ) {

        //     System.out.println("Diga me sua series favorita: ");
        //     series.nome = entrada.nextLine();

        //     System.out.print("Qual o genero da serie " + series.nome + ": ");
        //     series.genero = entrada.nextLine();
    
        //     System.out.print("Quantas tempora a serie " + series.nome + " tem: ");
        //     series.temp = entrada.nextInt();
    
        //     System.out.println("Sua serie favorita é: " + series.nome + "\nO genero é " + series.genero + "\nE são " + series.temp);

        // }

        // SeriesFavoritas Series;
        // Series = new SeriesFavoritas();

        // Series.nome = "Big bang";
        // Series.genero = "humor";
        // Series.temp = 8;

        // SeriesFavoritas Series1 = new SeriesFavoritas();

        // Series1.nome = "Bridgerton";
        // Series1.genero = "romance";
        // Series1.temp = 2;

        //System.out.println(Series1.nome + "..." + Series.nome);


    }
}
