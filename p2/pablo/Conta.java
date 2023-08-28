class Conta {
    int saldo;

    public sacar(int valor) throws Excessos {
        if (saldo < valor){
            throw new Excessos()
        }
    }

    public void deposiatar(int valor) {
       saldo += depositar
       System.out.println("Depositor feito com sucesso ")
    }

    public retirar(int valor) {
        saldo -= retirar
        System.out.println('Retirqndo feita com sucesso ')
        
    }
    public String verificar() {
        System.out.println(saldo)
    }

} 