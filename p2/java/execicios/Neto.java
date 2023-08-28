public class Neto extends Filho {
    public String avôPaterno;
    public String avóPaterna;
    public String avôMaterno;
    public String avóMaterna;
    public String mãe;

    public Neto(String nome, int idade, Familia familia) {
        super(nome, idade, familia);
    }

    public void imprimirDetalhes() {
        super.imprimirDetalhes();
        System.out.println("Avô paterno: " + avôPaterno);
        System.out.println("Avó paterna: " + avóPaterna);
        System.out.println("Avô materno: " + avôMaterno);
        System.out.println("Avó materna: " + avóMaterna);
    }
}
