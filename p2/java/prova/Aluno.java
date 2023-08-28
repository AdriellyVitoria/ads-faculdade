import java.util.Scanner;

public class Aluno {
    private String nome;
    private int matricula;
    private String curso;
    private String displina1;
    private String displina2;
    private String displina3;
    private double nota1;
    private double nota2;
    private double nota3;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getMatricula() {
        return matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }
    public String getDisplina1() {
        return displina1;
    }
    public void setDisplina1(String displina1) {
        this.displina1 = displina1;
    }
    public String getDisplina2() {
        return displina2;
    }
    public void setDisplina2(String displina2) {
        this.displina2 = displina2;
    }
    public String getDisplina3() {
        return displina3;
    }
    public void setDisplina3(String displina3) {
        this.displina3 = displina3;
    }
    public double getNota1() {
        return nota1;
    }
    public void setNota1(int nota1) {
        this.nota1 = nota1;
    }
    public double getNota2() {
        return nota2;
    }
    public void setNota2(int nota2) {
        this.nota2 = nota2;
    }
    public double getNota3() {
        return nota3;
    }
    public void setNota3(int nota3) {
        this.nota3 = nota3;
    }

public void imformação(){

    Scanner entrada = new Scanner(System.in);
    System.out.println("Ola, gostaria de verificar qual historico de qual curso: ");
    String curso = entrada.nextLine();
   
    System.out.print("Nome do Aluno: ");
    String nome = entrada.nextLine();

    System.out.print("Numero da matricula: ");
    int matricula = entrada.nextInt();
    entrada.nextLine();
    dados(nome, curso, matricula);
}

public void dados(String nome, String curso, int matricula){
    System.out.println("*****************");
    System.out.println("Boletir do aluno " + nome);
    System.out.println("Do curso " + curso );
    System.out.println("Numero de matricula: " + matricula);
    System.out.println("*****************");
}

public void boletir(String displina1, String displina2, String displina3, double nota1, double nota2, double nota3){
    System.out.println("Suas notas da " + displina1);
    System.out.println(nota1);
    if (nota1 >= 7.0){
        System.out.println("aprovando");
    } else {
        System.out.println("vai fazer recuperação");
    }

    System.out.println("Suas notas da " + displina2);
    System.out.println(nota2);
    if (nota2 >= 7.0){
        System.out.println("aprovando");
    } else {
        System.out.println("vai fazer recuperação");
    }

    System.out.println("Suas notas da " + displina3);
    System.out.println(nota3);
    if (nota3 >= 7.0){
        System.out.println("aprovando");
    } else {
        System.out.println("vai fazer recuperação");
    }
   
}
}
