public class Dark {
    public static void main(String[] args) {

        //familia.recebePersonagem(jonas);

        // Neto neto = new Neto();
        // neto.nome = "Jonas Kahnwald";
        // neto.idade = 17;

        // neto.familia = new Familia("Kahnwald");
        // neto.pai = "Michael Kahnwald";
        // neto.mae = "Hannah Kahnwald";

        // neto.imprimirDetalhes();

        // Familia kahnwald = new Familia("Kahnwald");
        // kahnwald.nome = "kahnwald";

        Neto jonas = new Neto(null, 0, null);
        jonas.nome = "Jonas Kahnwald";
        jonas.idade = 17;
        jonas.familia = new Familia("Kahnwald");
        jonas.pai = "Michael Kahnwald";
        jonas.mãe = "Hannah Kahnwald";
        jonas.avôPaterno = "Ines Kahnwald";
        jonas.avóPaterna = "Unknown";
        jonas.avôMaterno = "Daniel Doppler";
        jonas.avóMaterna = "Ines Kahnwald";

        Viajante viajante = new Viajante(jonas);
        viajante.imprimirDetalhes();
        //kahnwald.membros = new String[] {"Jonas", "Michael"};

        // Personagem jonas = new Personagem(null, 0, kahnwald);
        // jonas.nome = "Jonas Kahnwald";
        // jonas.idade = 17;
        // jonas.familia = "Familia Kahnwald";

        //kahnwald.imprimirDetalhes();
        //jonas.imprimirDetalhes();

    }
}
