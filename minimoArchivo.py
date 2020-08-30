import re
import json

def minimoValor(comando,datos):
    temp = re.split("\s", comando)
    if temp[1].lower() == "edad":
        minimoEdad(datos)
    elif temp[1].lower() == "promedio":
        minimoPromedio(datos)
    else:
        print("Error: Minimo ?/ no pudo realizar la busqueda")
        print("Solo puedes hacer una consulta de los siguientes atributos:")
        print("[edad, promedio]")

def minimoEdad(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorminimo = 99999
    for x in datos:
        if valorminimo > base[contador]["edad"]:
            valorminimo = base[contador]["edad"]
        contador = contador + 1
    print("La EDAD minima es:"+str(valorminimo))

def minimoPromedio(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorminimo = 9999
    for x in datos:
        if valorminimo > base[contador]["promedio"]:
            valorminimo = base[contador]["promedio"]
        contador = contador + 1
    print("El PROMEDIO minimo es:"+str(valorminimo))

#cargar archivo.json, Practica1.json