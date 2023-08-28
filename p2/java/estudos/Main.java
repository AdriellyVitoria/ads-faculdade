public class Main {
    public static void main(String[] args) {
        Empresa framework = new Empresa("Adri Techon", 14825);
        Departamento infra = new Departamento("suporte");
        Funcionario adrielly = new Funcionario();

        framework.setDepartamento(infra);

        framework.getDepartamento().setFuncionario(adrielly);
        framework.getDepartamento().getFuncionario().
    }

}
