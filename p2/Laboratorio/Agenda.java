package Laboratorio;

import java.util.Scanner;

public class Agenda {
    private Encontro lista[];

    public void SetEncontro(Encontro lista[]) {
        this.lista = lista;
    }

    public void exibiLista() {
        
    }
    // private int contador;

    // public Agenda(int tamanho) {
    //     encontros = new Encontro[tamanho];
    //     contador = 0;
    // }

    // public void adicionarEncontro() {
    //     if (contador < encontros.length) {
    //         Encontro encontro = new Encontro();
    //         encontros[contador] = encontro;
    //         contador++;
    //     } else {
    //         throw new IllegalArgumentException("A agenda está cheia.");
    //     }
    // }

    // public Encontro[] getEncontros() {
    //     return encontros;
    // }
}