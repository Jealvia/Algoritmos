/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lcs;

import java.io.IOException;

/**
 *
 * @author Julio
 */
public class Main {

    public static void main(String[] args) throws IOException {
        LCS lcs = new LCS();
        String cadena1 = lcs.muestraContenido("HomoSapiens10.txt");
        String cadena2 = lcs.muestraContenido("MusMuscula10.txt");

        char[] X = cadena1.toCharArray();
        char[] Y = cadena2.toCharArray();
        int m = X.length;
        int n = Y.length;
        
        System.out.println("Tamaño de LCS es" + " "+ lcs.lcs(X, Y, m, n));
    }
}
