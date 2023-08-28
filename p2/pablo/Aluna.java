public class Aluna {
    private String nome;
    private int matricula;
    
    public String getNome(String string) {
        return nome;
    }

    public Aluna(String nome) {
        this.nome = nome;
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public void NomeDoAluno(String aluno, int matricula){
        System.out.println("O aluno: " + aluno + " Com a matricula " + matricula);
    }

    public String getNome() {
        return null;
    }
}
