public class Main {
    public static void main(String[] args) { 

    Pessoa pessoa1 = new Pessoa("Adrielly", 20, "feminina");
    pessoa1.imprimirImformaçâo();

    System.out.println();

    Livros livros1 = new Livros("Amor gelado", "Adrielly", 150);
    livros1.imprimir();

    System.out.println();

    Aluno aluno1 = new Aluno("Adrielly", 10, 80);
    Aluno aluno2 = new Aluno("Arielly", 18, 6.2);

    aluno1.calcularmedia();
    aluno2.calcularmedia();

   Funcionario funcionario = new Funcionario("Mateus", "G", 1000);
   Funcionario funcionario1 = new Funcionario("Bruno", "S", 1000);
   Funcionario funcionario3 = new Funcionario("Castiel", "F", 1000);

   funcionario.CalcularAumento();
   funcionario1.CalcularAumento();
   funcionario3.CalcularAumento();

   Gerente gerente = new Gerente("Adrielly", "gerente", 1000, 100);
   gerente.calcularSalario();
    Mulher mulher = new Mulher("Josa", 65, "feminino", "bela");
    mulher.imprimir();
}
}
