def mochila(peso, valor, capacidad, R):
    for c in range(capacidad + 1):
        R[0][c] = 0
    for j in range(1, len(peso) + 1):
        for c in range(capacidad + 1):
            if c >= peso[j - 1]:
                R[j][c] = max(R[j - 1][c], R[j - 1][c - peso[j - 1]] + valor[j - 1])
            else:
                R[j][c] = R[j - 1][c]
    for i in range(len(peso) + 1):
        print(R[i])


valor = [25,20,15,40,50]
peso = [3, 2, 1, 4, 5]
capacidad = 6

R = []
for i in range(len(peso) + 1):
    ea_row = []
    for j in range(capacidad + 1):
        ea_row.append(0)
    R.append(ea_row)
    
mochila(peso, valor, capacidad, R)