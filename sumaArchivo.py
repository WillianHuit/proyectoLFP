import re
import json

def sumaValor(comando,datos):
    temp = re.split("\s", comando)
    if temp[1].lower() == "edad":
        sumaEdad(datos)
    elif temp[1].lower() == "promedio":
        sumaPromedio(datos)
    else:
        print("Error: Suma ?/ no pudo realizar la busqueda")
        print("Solo puedes hacer una consulta de los siguientes atributos:")
        print("[edad, promedio]")

def sumaEdad(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorSuma = 0
    for x in datos:

        valorSuma = valorSuma + base[contador]["edad"]
        contador = contador + 1
    print("La suma de las EDADES es:"+str(valorSuma))

def sumaPromedio(datos):
    data_string = json.dumps(datos)
    base = json.loads(data_string)
    contador = 0
    valorSuma = 0
    for x in datos:
        valorSuma = valorSuma+ base[contador]["promedio"]
        contador = contador + 1
    print("la Suma del PROMEDIO es:"+str(valorSuma))

#cargar archivo.json, Practica1.json