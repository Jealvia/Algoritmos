/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package voraces;

import java.util.*;

/**
 *
 * @author Julio
 */
public class Cuerdas {

    static int costoMinimo(int arr[], int n) {
        PriorityQueue<Integer> pq
                = new PriorityQueue<Integer>();
        for (int i = 0; i < n; i++) {
            pq.add(arr[i]);
        }
        int res = 0;
        while (pq.size() > 1) {
            int first = pq.poll();
            int second = pq.poll();
            res += first + second;
            pq.add(first + second);
        }

        return res;
    }
    public static void main(String args[]) {
        int len[] = {4, 3, 2, 6};
        int size = len.length;
        System.out.println("Costo total de conectar"
                + " cuerdas es " + costoMinimo(len, size));

    }
}
