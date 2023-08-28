public class Veiculo {
    String marca;
    String modelo;
        
    public Veiculo(String marca, String modelo){
        this.marca = marca;
        this.modelo = modelo;
    }

    public void mostra(){
        System.out.println("marca: " +marca+ " Modelo: " +modelo);
    }
        
}
