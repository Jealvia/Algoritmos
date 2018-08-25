def estudiantes_egresados(archivo1, archivo2):
    dic={}
    lista_info=archivo1.readlines()
    lista_estudiantes=archivo2.readlines()
    for i in lista_info:
        c = i.split("|")
        d = c[1][1:-2].split(",")
        matr = c[0]
        for esto in range(len(d)):
            var = d[esto].split(":")

            if var[0] == "PERIODO DE EGRESO":
                p_egre = var[1].split("-")
                a_egre = int(p_egre[0])
                if p_egre[1][0]=="1":
                    t_egre = 1
                elif p_egre[1][0]=="2":
                    t_egre = 2
                elif p_egre[1][0]=="3":
                    t_egre = 3
                else:
                    t_egre=3

            elif var[0] == "FECHA DE GRADUACION":
                if var[1] != " " and var[1].strip() != "NO GRADUADO":
                    f_graduac = var[1]
                else:
                    f_graduac = "-"
            elif var[0] == "CARRERA":
                if var[1] != " ":
                    carre = var[1]
                else:
                    carre = "-"
            elif var[0] == "TITULO OBTENIDO":
                if var[1] != " ":
                    tit = var[1]
                else:
                    tit = "-"
            elif var[0] == "NIVEL DE ESTUDIO":
                if var[1] != " ":
                    nivel = var[1]
                else:
                    nivel = "-"
            elif var[0] == "TESIS O PROYECTO":
                if var[1] != " ":
                    tesi = var[1]
                else:
                    tesi = "-"
        for linea2 in lista_estudiantes:
            d = linea2.split(";")
            matri = str(d[0])
            e = d[1].split(" ")

            if matr == matri and len(e) == 4:
                dic[int(matr)] = {"apellidos": str(e[0]) + " " + str(e[1]), "nombres": str(e[2]) + " " + str(e[3][:-1]),
                                  "a_ingreso": int(matri[:4]), "a_egreso": a_egre,
                                  "t_egreso": t_egre, "fecha_graduacion": f_graduac, "carrera": carre,
                                  "titulo": tit, "tesis_proyecto": tesi}
            elif matr == matri and len(e) == 3:

                dic[int(matr)] = {"apellidos": str(e[0]) + " " + str(e[1]), "nombres": str(e[2][:-1]),
                                  "a_ingreso": int(matri[:4]), "a_egreso": a_egre,
                                  "t_egreso": t_egre, "fecha_graduacion": f_graduac, "carrera": carre,
                                  "titulo": tit, "tesis_proyecto": tesi}
            elif matr == matri and len(e) == 2:
                print(matr)
                dic[int(matr)] = {"apellidos": str(e[0]), "nombres": str(e[1]),
                                  "a_ingreso": int(matri[:4]), "a_egreso": a_egre,
                                  "t_egreso": t_egre, "fecha_graduacion": f_graduac, "carrera": carre,
                                  "titulo": tit, "tesis_proyecto": tesi}
    return dic
"""def funcion_nueva():
    φ1 = this.lat.toRadians(), λ1 = this.lon.toRadians()
    φ2 = point.lat.toRadians(), λ2 = point.lon.toRadians()
    sinφ1 = Math.sin(φ1), cosφ1 = Math.cos(φ1), sinλ1 = Math.sin(λ1), cosλ1 = Math.cos(λ1)
    sinφ2 = Math.sin(φ2), cosφ2 = Math.cos(φ2), sinλ2 = Math.sin(λ2), cosλ2 = Math.cos(λ2)
    // distance
    between
    points
    Δφ = φ2 - φ1;
    Δλ = λ2 - λ1;
    a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2)
    + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2)
    δ = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
    A = Math.sin((1 - fraction) * δ) / Math.sin(δ)
    B = Math.sin(fraction * δ) / Math.sin(δ)
    x = A * cosφ1 * cosλ1 + B * cosφ2 * cosλ2
    y = A * cosφ1 * sinλ1 + B * cosφ2 * sinλ2
    z = A * sinφ1 + B * sinφ2
    φ3 = Math.atan2(z, Math.sqrt(x * x + y * y))
    λ3 = Math.atan2(y, x)"""""
def estudiantesPorCarrera( diccionario):
    dic = {}
    for k in diccionario.keys():
        if diccionario[k]["carrera"] not in dic:
            ya=diccionario[k]["carrera"]
            dic[diccionario[k]["carrera"]]= 1
        else:
            dic[ya] += 1
    return dic

def guardarEstudiantesPorCarrera (diccionario, archivo):
    nuevo=open((archivo+".txt"),"w")
    for k,v in diccionario.items():
        nuevo.write(str(k)+";"+str(v)+"\n")

info=open("info.txt","r",encoding='utf-8')
estudiantes=open("estudiantes.txt","r")

termino=estudiantesPorCarrera(estudiantes_egresados(info,estudiantes))
print(termino)
texto="n_estudiantes_x_carrera"
guardarEstudiantesPorCarrera(termino,texto)

def totalEmpresasPais():
    archivo = open("accionistas_nuevo2.csv", 'r', encoding="utf8")
    dic = {}
    for linea in archivo.readlines():
        linea = linea.split(";")
        if linea[1] not in dic:
            dic[linea[1]] = {linea[3].strip(): [linea[2].strip()]}
        else:
            if linea[3] not in dic[linea[1]]:
                dic[linea[1]]={linea[3].strip : [linea[2].strip()]}
            else:
                dic[linea[1]][linea[3].strip()].append(linea[2].strip())
    archivo.close()
    return dic

#def empresasAccionistasParaisosFisales(diccionario):


def listaParaisos():
    lista=[]
    archivo = open("accionistas_nuevo2.csv", 'r', encoding="utf8")
    for linea in archivo.readlines():
        linea=linea.split(";")
        lista.append(linea[1].strip())
    archivo.close()
