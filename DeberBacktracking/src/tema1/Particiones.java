package tema1;

import java.util.ArrayList;

public class Particiones {
    // Devuelve true si palabra es palindrome, caso contrario falso

    public static boolean esPalindromo(String palabra) {
        int tam = palabra.length();
        tam--;
        for (int i = 0; i < tam; i++) {
            if (palabra.charAt(i) != palabra.charAt(tam)) {
                return false;
            }
            tam--;
        }
        return true;
    }

    // Genera todas las particiones palindrómicas de 's' y almacena el resultado en 'v'.
    public static void particion(String s, ArrayList<ArrayList<String>> v) {
        // ArrayList temporal para almacenar cada cadena palindrómica
        ArrayList<String> temp = new ArrayList<>();
        // llama al método String agrega todo las particiones palindrómicas a v
        v = addStrings(v, s, temp, 0);
        // imprime la solucion
        presentarSolucion(v);
    }

    // Pasa por todos los índices y agrega recursivamente el resto particiones si la cadena actual es palindrome.
    public static ArrayList<ArrayList<String>> addStrings(ArrayList<ArrayList<String>> v, String palabra, ArrayList<String> tmp, int indice) {
        int len = palabra.length();
        String str = "";
        ArrayList<String> current = new ArrayList<>(tmp);
        if (indice == 0) {
            tmp.clear();
        }
        // Iterar sobre la cadena
        for (int i = indice; i < len; ++i) {
            str = str + palabra.charAt(i);
            // verifica si la subcadena es palindrómico o no
            if (esPalindromo(str)) {
                // si es palindrome lo agrega a la lista temporal
                tmp.add(str);
                if (i + 1 < len) {
                    // recurre para obtener todas las particiones palindrómicas para las subcadenas
                    v = addStrings(v, palabra, tmp, i + 1);
                } else {
                    // si se llega al final de la cadena, agregue temp a v
                    v.add(tmp);
                }
                // temp se inicializa con el i actual.
                tmp = new ArrayList<>(current);
            }
        }
        return v;
    }

    // Imprime la lista de particiones
    public static void presentarSolucion(ArrayList<ArrayList<String>> particiones) {
        for (ArrayList<String> i : particiones) {
            for (String j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {
        System.out.println("Primera prueba:");
        String s = "geeks";
        ArrayList<ArrayList<String>> partitions = new ArrayList<>();
        particion(s, partitions);
        System.out.println("Segunda prueba:");
        String s2 = "hola";
        ArrayList<ArrayList<String>> partitions1 = new ArrayList<>();
        particion(s2, partitions1);
    }
}
