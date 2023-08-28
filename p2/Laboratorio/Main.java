package Laboratorio;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        Agenda a1 = new Agenda();
        Encontro encontro[] = new Encontro[2];

        int dia, mes;
        String descricao;

        for (int i = 0; i < 2; i++) {
            System.out.println("Digete o dia, mes e descrição do evento");
            
            dia = tec.nextInt();
            mes = tec.nextInt();
            tec.nextLine();
            descricao = tec.nextLine();
            
            encontro[i] = new Encontro(dia, mes, descricao);
        }
        //Encontro e1 = new Encontro();

        System.out.println("Encontro 1: Dia " + e1.getDia() + ", Mês " + e1.getMes() + ", Descrição " + e1.getDescricao());
      
}
}