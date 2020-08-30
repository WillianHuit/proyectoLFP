import re
import cargarArchivo
import seleccionarArchivo
import maximoArchivo
import minimoArchivo
import sumaArchivo
import cuentaArchivo
import generadorReporte
import json

#simula la base de datos

datos =[]
def cargar(comandoInicial):
    temp = cargarArchivo.cargarArchivo(comandoInicial)
    for l in temp:
        datos.append(l)
    ingresarComando()

def baseCargada():
    if datos == []:
        return False
    else:
        return True

def seleccionar(comandoInicial):

    if baseCargada():
        seleccionarArchivo.mostrarSeleccion(comandoInicial,datos)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
    ingresarComando()

def maximo(comandoInicial):
    if baseCargada():
        maximoArchivo.maximoValor(comandoInicial,datos)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
    ingresarComando()

def minimo(comandoInicial):
    if baseCargada():
        minimoArchivo.minimoValor(comandoInicial,datos)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
    ingresarComando()

def suma(comandoInicial):
    if baseCargada():
        sumaArchivo.sumaValor(comandoInicial,datos)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
    ingresarComando()

def cuenta():
    if baseCargada():
        cuentaArchivo.cuentaDatos(datos)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
    ingresarComando()
def mostrarTodo():
    print(datos)
    ingresarComando()

def reportar(comandoInicial):
    if baseCargada():
        generadorReporte.generar(datos,comandoInicial)
    else:
        print("Aun no hay registros, utiliza el comando CARGAR")
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
    print("Ingresa un comando:")
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
        maximo(comandoInicial)
    elif comando.lower() == "minimo":
        minimo(comandoInicial)
    elif comando.lower() == "suma":
        suma(comandoInicial)
    elif comando.lower() == "cuenta":
        cuenta()
    elif comando.lower() == "reportar":
        reportar(comandoInicial)
    elif comando.lower() == "reportar":
        reportar(comandoInicial)
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



