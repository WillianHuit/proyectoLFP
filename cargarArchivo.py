import json
import re
archivo_retorno = []
def cargarArchivo(comando):
    #Guarda el nombre de los archivos
    temp = re.split("\s", comando, 1)
    nombreArchivo = re.split("\s", temp[1])
    valor = 0
    final = 0
    for x in nombreArchivo:
        valor += readJSON(x)
        final = final+1
    print("Archivos leidos:"+str(final)+" Completados:"+str(valor)+" Errores:"+str(final-valor))
    return archivo_retorno

def readJSON(nombreSucio):
    try:
        #cargar archivo.json, Practica1.json
        nombreArchivo = re.sub("\,","",nombreSucio)
        file = open(nombreArchivo,)
        data = json.load(file)
        #print(data)
        #print(type(data))
        for l in data:
            archivo_retorno.append(l)
        return 1
    except:
        return 0

