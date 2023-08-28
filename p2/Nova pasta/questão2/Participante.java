package questão2;

public class Participante {
  public String nome;
  public String email;
  public int idade;

  public Participante(String nome, String email){
    System.out.println("Seu nome: " + nome);
    System.out.println("Seu email é: " + email);
    
  }

  public void add(Participante participante) {
      
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getEmail() {
    return email;
  }

  }
  
