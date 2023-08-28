package questão2;

public class Local {
    public String nome;
    public int endereço;
    public int capacidade;
    
    public void verificarDisponibilidade(int capacidade){
        if( capacidade < 100){
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}
