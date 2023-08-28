package Laboratorio;


public class Encontro {
    private int dia;
    private int mes;
    private String descricao;

    public Encontro () {
        // Scanner sc = new Scanner(System.in);

        // System.out.print("Digite o mes do encontro: ");
        // int dia = sc.nextInt();

        // System.out.print("Digite o dia do encontro: ");
        // int mes = sc.nextInt();

        // sc.nextLine();

        // System.out.print("Digite a descrição do encontro: ");
        // String descricao = sc.nextLine();

        if (validaData(dia, mes)) {
            this.dia = dia;
            this.mes = mes;
        } else {
            throw new IllegalArgumentException("Data inválida.");
        }
        this.descricao = descricao;
    }

    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        if (validaData (dia, this.mes)) {
            this.dia = dia;
        } else {
            throw new IllegalArgumentException("Data inválida.");
        }
    }

    public int getMes() {
        return mes;
    }

    public void setMes(int mes) {
        if (validaData (this.dia, mes)) {
            this.mes = mes;
        } else {
            throw new IllegalArgumentException("Data inválida.");
        }
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public boolean validaData(int dia, int mes) {
        if (dia < 1 || dia > 31 || mes < 1 || mes > 12) {
            return false;
        } 
        if ((dia == 31) && (mes == 4 || mes == 6 || mes == 9 || mes == 11)) {
            return false;
        }
        if (mes == 2) {
            if (dia > 29) {
                return false;
            }
        }
        // if (dia == 29 && !(((ano % 4 == 0) && (ano % 100 != 0)) || (ano % 400 == 0))) {
        //     return false;
        // }
       return true; 
    }
}
