import numpy
def programaPrincipal(esfuerzo, puntaje, M):
    columna=M + 1
    fila=len(esfuerzo) + 1
    tabla = numpy.zeros((fila,columna), float)
    for i in range (0, fila):
        tabla[i][0] = float("inf")
    for j in range (0, columna):
        tabla[0][j] = float("inf")
    for k in range(1, fila):
        for l in range(1, columna):
            if sum(puntaje[:k]) < l:
                tabla[k][l] = float("inf")
            else:
                tmp = 0
                if l - puntaje[k - 1] >= 0:
                    tmp = tabla[k - 1, l - puntaje[k - 1]]
                if tmp + esfuerzo[k - 1] < tabla[k - 1, l]:
                    tabla[k, l] = tmp + esfuerzo[k - 1]
                else:
                    tabla[k, l] = tabla[k - 1, l]
    return presentarSolucion(tabla, fila - 1, columna - 1, puntaje)

def presentarSolucion(matriz, m, n, puntajes):
    tareas =[]
    while n>0 and m>0:
        if matriz[m,n] == matriz[m-1,n]:
            m -= 1
        else:
            tareas.append(m-1)
            n -= puntajes[m-1]
            m -= 1
    return tareas

def main():
    minimaNota = 60
    esfuerzos = [9, 2, 8, 4, 1, 2, 15, 6, 8, 3, 7]
    puntajes = [9, 5, 14, 2, 8, 30, 13, 8, 7, 5,10]
    print "*****Datos iniciales*****"
    print "Nota minima: ",minimaNota
    for i in range(0,len(esfuerzos)):
        print("Esfuerzo: "+str(esfuerzos[i])+" \t"+" Puntaje: "+str(puntajes[i]))
    tareas = programaPrincipal(esfuerzos, puntajes, minimaNota)
    tareas.sort()
    print "*****Tareas a realizar para aprobar y su esfuerzo*****"
    for i in tareas[::]:
        print("Tarea: "+ str(i + 1)+"\t"+"Puntaje: "+ str(puntajes[i])+"\t"+"Esfuerzo: "+str(esfuerzos[i]))

main()