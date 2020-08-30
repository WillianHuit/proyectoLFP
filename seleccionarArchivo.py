import re
import json
def mostrarSeleccion(comandoInicial, datos):
    temp = re.split("\s", comandoInicial, 1)
    if temp[1] == "*":
        imprimirTodo(datos)
    else:
        imprimirSeleccion(temp[1],datos)



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
    temp = re.split("\s", comando)
    contador = 0
    for x in temp:
        if x.lower() == "donde":
            break
        else:
            contador = contador + 1
    continuar = 0
    a = b = c = d = 0
    for x in range(contador):
        tempIgualdad = re.sub("\,","",temp[x])
        if tempIgualdad == "nombre" or tempIgualdad == "edad" or tempIgualdad == "activo" or tempIgualdad == "promedio":
            continuar = continuar +1
    if contador == continuar and notRepet(temp,contador) and formatoBusqueda(temp, contador):
        division = crearEncabezado(temp, contador)
        try:
            busqueda = temp[contador + 3] + " " + temp[contador + 4]
        except:
            busqueda = temp[contador + 3]
        imprimirDato(temp[contador + 1], busqueda, datos, division, temp, contador)
    else:
        print("El comando contiene atributos erroneos o atributos duplicados")

    #for x in range(contador):
        #print(temp[x])
def formatoBusqueda(temp, contador):
    valor = len(temp)-(contador + 3)
    if valor>1:
        txt = temp[contador+3]
        x =re.findall("\"", txt)
        if x:
            return True
    else:
        txt = temp[contador+3]
        if txt.isdigit():
            return True
        else:
            x = re.search("\"", txt)
            if x:
                return True

    return False
def notRepet(atributos, contador):
    repetir = 0
    atributoTemp = ""
    for x in range(contador):
        atributoTemp = re.sub("\,","",atributos[x])
        if atributoTemp == "nombre":
            repetir = repetir + 1
        if repetir > 1:
            return False
    repetir = 0
    for x in range(contador):
        atributoTemp = re.sub("\,", "", atributos[x])
        if atributoTemp == "edad":
            repetir = repetir + 1
        if repetir > 1:
            return False
    repetir = 0
    for x in range(contador):
        atributoTemp = re.sub("\,", "", atributos[x])
        if atributoTemp == "promedio":
            repetir = repetir + 1
        if repetir > 1:
            return False
    repetir = 0
    for x in range(contador):
        atributoTemp = re.sub("\,", "", atributos[x])
        if atributoTemp == "activo":
            repetir = repetir + 1
        if repetir > 1:
            return False
    return True

def crearEncabezado(temp, tam):
    try:
        division = "+"
        encabezado = "|"
        contador = 0
        actual = 0
        faltante = 0
        for x in range(tam):
            nombreTemp = ""
            espacio = ""
            division = division + "------------------+"
            nombreTemp = re.sub("\,", "", temp[contador])
            actual = len(nombreTemp)
            faltante = 18 - actual
            for y in range(faltante):
                espacio = espacio + " "
            nombreTemp = nombreTemp + espacio + "|"
            encabezado = encabezado + nombreTemp
            contador = contador + 1
        print(division)
        print(encabezado)
        print(division)
        return division
    except:
        print("El comando tiene campos inexistentes")
        return ""


def imprimirDato(atributo, busquedaSucia, datos, division,temp,tam):
    try:
        data_string = json.dumps(datos)
        decoded = json.loads(data_string)
        # print(str(decoded[1]["nombre"]))
        contador = 0
        encontrado = False
        busquedaPreventiva = re.sub("\“","",busquedaSucia)
        busquedaA = re.sub("\"","",busquedaPreventiva)
        busqueda = str(re.sub("\”","",busquedaA))
        for x in datos:
            registro = str(decoded[contador][atributo])
            if registro.lower() == busqueda.lower():
                encabezado = "|"
                fila = "|"
                for x in range(tam):
                    nombreTemp = ""
                    espacio = ""
                    atributoSimple = re.sub("\,","",temp[x])
                    nombreTemp = decoded[contador][atributoSimple]
                    actual = len(str(nombreTemp))
                    faltante = 18 - actual
                    for y in range(faltante):
                        espacio = espacio + " "
                    nombreTemp = str(nombreTemp) + espacio + "|"
                    fila = fila + nombreTemp
                print(fila)
                print(division)
            contador = contador + 1
    except:
        print("error")

#cargar archivo.json, Practica1.json
#SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Registro 1”
#SELECCIONAR nombre, edad, promedio, activo DONDE activo = "True"