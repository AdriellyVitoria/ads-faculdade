package questão2;
import java.util.ArrayList;
import java.util.List;
public class Evento {
    public String nome;
    public int data;
    public int hora;
    public Local organizador;
    public String local;
    public List<Participante> participante = new ArrayList<Participante>();


    public void adicionarDisponibilidade(Participante participante){
        participante.add(participante);
    }

    public void imprimirDeParticipante(){
        Participante par1 = new Participante("Adrielly ", "hott");
        par1.Participante();
    }
}
