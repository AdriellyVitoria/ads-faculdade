public class Disciplinas {
    private String nome;
    static Aluna aluna;
    Prof prof;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNomeAlunaString() {
        return aluna.getNome();
    }

    public void setAluna(Aluna aluna) {
        this.aluna = aluna;
    }

    public Prof getProf() {
        return prof;
    }

    public void setProf(Prof prof) {
        this.prof = prof;
    }

    public void mostra(String nome, String disciplina, String prof){
        System.out.println("O aluno: " + nome + " Da materias: " + disciplina + " O proff é: "  + prof);
    }
    
}
