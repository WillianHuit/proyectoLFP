import re
import json

def maximoValor(comando,datos):
    temp = re.split("\s", comando)
    if temp[1].lower() == "edad":
        maximoEdad(datos)
    elif temp[1].lower() == "promedio":
        maximoPromedio(datos)
    else:
        print("Error: Maximo ?/ no pudo realizar la busqueda")
        print("Solo puedes hacer una consulta de los siguientes atributos:")
        print("[edad, promedio]")

def maximoEdad(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorMaximo = 0
    for x in datos:
        if valorMaximo < base[contador]["edad"]:
            valorMaximo = base[contador]["edad"]
        contador = contador + 1
    print("La EDAD maxima es:"+str(valorMaximo))

def maximoPromedio(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorMaximo = 0
    for x in datos:
        if valorMaximo < base[contador]["promedio"]:
            valorMaximo = base[contador]["promedio"]
        contador = contador + 1
    print("El PROMEDIO maximo es:"+str(valorMaximo))

#cargar archivo.json, Practica1.json