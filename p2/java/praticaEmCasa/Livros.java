//Crie uma classe Livro com os atributos título, autor e número de páginas. Crie um método para imprimir as informações do livro.
public class Livros {
    protected String titulo;
    protected String autor;
    protected int numeroDePaginas;

    public Livros (String titulo, String autor, int numeroDePaginas){
        this.titulo = titulo;
        this.autor = autor;
        this.numeroDePaginas = numeroDePaginas;
    }

    public void imprimir(){
        System.out.println("Titulo: " + titulo);
        System.out.println("autor: " + autor);
        System.out.println("numero De pag: " + numeroDePaginas);
    }
}
