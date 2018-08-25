/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectofinal;

import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 *
 * @author Julio
 */
public class Tarea {

    int nota, esfuerzo;

    public Tarea(int nota, int esfuerzo) {
        this.nota = nota;
        this.esfuerzo = esfuerzo;
    }

    public int getNota() {
        return nota;
    }

    public int getEsfuerzo() {
        return esfuerzo;
    }
    
    public static String OptimizarTareas(int notaMin,List<Integer> deberes,List<Integer> esfuerzos)
   {
       int esfuerzo=0, contador=0, nota=0;
       String respuesta="Lista de deberes\n";
       Comparator<Tarea> c = (Tarea o1, Tarea o2) -> o1.getEsfuerzo()-o2.getEsfuerzo();
       Queue<Tarea> colaDeberes=new PriorityQueue<>(c);
       if(deberes.size()!=esfuerzos.size())
           return "Listas no válidas, deber ser del mismo tamaño";
       else{
           for(int i=0;i<deberes.size();i++)
           {
               colaDeberes.add(new Tarea(deberes.get(i),esfuerzos.get(i)));
           }
           while(nota<notaMin && !colaDeberes.isEmpty())
           {
               Tarea tmp=colaDeberes.remove();
               esfuerzo=esfuerzo+tmp.getEsfuerzo();
               nota=nota+tmp.getNota();
               respuesta=respuesta+"Nota de Tarea: "+tmp.getNota()+" con el esfuerzo de "+tmp.getEsfuerzo()+"\n";
               contador=contador+1;
           }
       }
       if(nota>=notaMin)
        return respuesta+"Total de deberes: "+contador+" con el esfuerzo de "+esfuerzo+" y con una nota total para pasar de "+nota;
       else
           return"No es posible pasar ni realizando todas las tareas, le faltó "+(notaMin-nota)+" puntos para pasar." ;
   }

    
}
