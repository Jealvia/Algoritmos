/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lcs;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author Julio
 */
public class LCS {

    public int lcs(char[] X, char[] Y, int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        }
        if (X[m - 1] == Y[n - 1]) {
            return 1 + lcs(X, Y, m - 1, n - 1);
        } else {
            return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));
        }
    }


    public int max(int a, int b) {
        return (a > b) ? a : b;
    }

    public String muestraContenido(String archivo) throws FileNotFoundException,
            IOException {
        String cadena;
        String resultado="";
        FileReader f = new FileReader(archivo);
        BufferedReader b = new BufferedReader(f);
        while ((cadena = b.readLine()) != null) {
            resultado+=cadena;
        }
        b.close();
        System.out.println(resultado);
        return resultado;
    }

}
 

