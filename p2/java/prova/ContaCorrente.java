public class ContaCorrente {
    private int numero;
    private double saldo;
    private String status;
    private int limite;
    
    public ContaCorrente(int numero, double saldo, String status, int limite) {
        this.numero = numero;
        this.saldo = saldo;
        this.status = status;
        this.limite = limite;
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
    public int getLimite() {
        return limite;
    }
    public void setLimite(int limite) {
        this.limite = limite;
    }

    public void saque(double saque){
        if (saldo > saque) {
            System.out.println("Foi retirando da conta: "+ saque);
            saldo -= saque;
        } else {
            System.out.println("limite insuficiente");
        }
    } 

    public void despositar(double despositor) {
        System.out.println("Seu depositor foi realizando com sucesso. teve um aumento de " + despositor );
        saldo += despositor;
    }

    public void consultar(){
        System.out.println("Seu saldo é: " + saldo);
        if (status == "especial"){
            System.out.println("Voce é cliente especial");
        } else {
            System.out.println("vc não é clinte especial");
        }
    }
}
