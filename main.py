import re
import cargarArchivo
import seleccionarArchivo
import json

#simula la base de datos

datos =[]

def cargar(comandoInicial):
    temp = cargarArchivo.cargarArchivo(comandoInicial)
    for l in temp:
        datos.append(l)
    #print(datos)
    # encoded
    #data_string = json.dumps(datos)
    #print(data_string)
    # Decoded
    #decoded = json.loads(data_string)
    #print(decoded)-- el siguiente codigo muestra el registro 2
    #print("Tenemos " + str(decoded[1]["nombre"]) + " Lechugas.")
    ingresarComando()

def seleccionar(comandoInicial):
    seleccionarArchivo.mostrarSeleccion(comandoInicial,datos)
    ingresarComando()

def maximo():
    print("maximo")
    ingresarComando()

def minimo():
    print("minimo")
    ingresarComando()

def suma():
    print("suma")
    ingresarComando()

def cuenta():
    print("cuenta")
    ingresarComando()
def mostrarTodo():
    print(datos)
def reportar():
    print("reportar")
    ingresarComando()
def error():
    print("No se pudo reconocer el comando intenta de nuevo (ingresa help para ver los comandos aceptados)")
    ingresarComando()
def close():
    print("Se ha finalizado el programa")

def help():
    print("Comandos aceptados:")
    print("cargar, seleccionar, maximo, minimo, suma, cuenta, reportar, close")
    ingresarComando()


def inicio():
    # print("¿Cómo se llama? ", end="")
    # nombre = input()
    print("--------------Simple SQL----------------")
    print("Ahora esta en uso, ingresa un comando (help para ver los comandos)")
    ingresarComando()

def ingresarComando():
    comandoInicial = input()
    reconocer = re.split("\s", comandoInicial, 1)
    activarComando(reconocer[0], comandoInicial)

def activarComando(comando, comandoInicial):
    #Lower convierte a minusculas, upper a mayusculas
    if comando.lower() == "cargar":
        cargar(comandoInicial)
    elif comando.lower() == "seleccionar":
        seleccionar(comandoInicial)
    elif comando.lower() == "maximo":
        maximo()
    elif comando.lower() == "minimo":
        minimo()
    elif comando.lower() == "suma":
        suma()
    elif comando.lower() == "cuenta":
        cuenta()
    elif comando.lower() == "reportar":
        reportar()
    elif comando.lower() == "reportar":
        reportar()
    elif comando.lower() == "mostrar":
        mostrarTodo()
    elif comando.lower() == "help":
        help()
    elif comando.lower() == "close":
        close()
    else:
        error()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    inicio()



