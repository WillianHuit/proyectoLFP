import re
import json
def mostrarSeleccion(comandoInicial, datos):
    temp = re.split("\s", comandoInicial, 1)
    if temp[1] == "*":
        imprimirTodo(datos)
    else:
        imprimirSeleccion(temp[1],datos)

    #print("+------------+------------+------------+------------+")
    #print("|   Nombre   |"+"    Edad    |"+"   Activo   |"+"  Promedio  |")
    #print("+------------+------------+------------+------------+")
    #print("|Juan Perez  |"+"45          |"+"true        |"+"56.456      |")
    #print("+------------+------------+------------+------------+")

def imprimirTodo(datos):
    division = "+------------------+------------------+------------------+------------------+"
    print(division)
    print("|      Nombre      |"+"       Edad       |"+"      Activo      |"+"     Promedio     |")
    print(division)
    data_string = json.dumps(datos)
    decoded = json.loads(data_string)
    #Juegos de 18
    nombre = "|"
    edad = ""
    activo = ""
    promedio = ""
    contador = 0
    espacio = 0
    actual = 0
    for x in datos:
        tempEspacio = ""
        #----------------Toma el nombre------------------------
        nombre = nombre + decoded[contador]["nombre"]
        actual = len(nombre)
        espacio = 19-actual
        for y in range(espacio):
            tempEspacio = tempEspacio + " "
        nombre = nombre + tempEspacio+"|"
        # ----------------Toma el edad------------------------
        tempEspacio = ""
        edad = edad + str(decoded[contador]["edad"])
        actual = len(edad)
        espacio = 18 - actual
        for y in range(espacio):
            tempEspacio = tempEspacio + " "
        edad = edad + tempEspacio + "|"
        # ----------------Toma el activo------------------------
        tempEspacio = ""
        activo = activo + str(decoded[contador]["activo"])
        actual = len(activo)
        espacio = 18 - actual
        for y in range(espacio):
            tempEspacio = tempEspacio + " "
        activo = activo + tempEspacio + "|"
        # ----------------Toma el promedio------------------------
        tempEspacio = ""
        promedio = promedio + str(decoded[contador]["promedio"])
        actual = len(promedio)
        espacio = 18 - actual
        for y in range(espacio):
            tempEspacio = tempEspacio + " "
        promedio = promedio + tempEspacio + "|"

        print(nombre+edad+activo+promedio)
        edad = activo = promedio = ""
        nombre = "|"
        print(division)
        contador = contador + 1


def imprimirSeleccion(comando, datos):
    #cargar archivo.json, Practica1.json
    #SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Francisco”
    temp = re.split("\s", comando)
    contador = 0
    for x in temp:
        if x.lower() == "donde":
            break
        else:
            contador = contador + 1
    for x in range(contador):
        print(temp[x])
    print("Esta en: "+ str(contador))
    print("Especifico")