public class Escola {
    public static void main(String[] args) {       
        Aluno escola = new Aluno();
       escola.imformação();
       escola.boletir("portugues", "matematica", "historia", 7.0, 9.0, 5.0);

       Aluno escola2 = new Aluno();
       escola2.imformação();
       escola2.boletir("matematica", "geografia", "artes", 8.0, 5.0, 7.0);
    }
}