import json
import webbrowser
import re

def generar(datos,comandoInicial):
    temp = re.split("\s", comandoInicial)
    veces = int(temp[1])
    print("Cargando...")
    try:
        file = open("reporte.html", "w")
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>Reporte</title>\n")
        file.write("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css\" integrity=\"sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z\" crossorigin=\"anonymous\">\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<center><h1>Reporte</h1></center>\n")
        file.write("<table class=\"table\">\n")
        file.write("<thead class=\"thead-dark\">\n")
        file.write("<tr>\n")
        file.write("<th scope=\"col\">#</th>\n")
        file.write("<th scope=\"col\">Nombre</th>\n<th scope=\"col\">Edad</th>\n<th scope=\"col\">Activo</th>\n<th scope=\"col\">Promedio</th>")
        file.write("</tr>\n")
        file.write("</thead>\n")
        file.write("<tbody>\n")
        # Crea la fila -----------------------------------------------------------------
        data_string = json.dumps(datos)
        baseDatos = json.loads(data_string)
        contador = 0
        for x in range(veces):
            file.write("<tr>\n")
            file.write("<th scope=\"row\">"+str(contador+1)+"</th>\n")
            file.write("<td>"+baseDatos[contador]["nombre"]+"</td>\n")
            file.write("<td>" + str(baseDatos[contador]["edad"]) + "</td>\n")
            file.write("<td>" + str(baseDatos[contador]["activo"]) + "</td>\n")
            file.write("<td>" + str(baseDatos[contador]["promedio"]) + "</td>\n")
            file.write("</tr>\n")
            contador = contador + 1
        file.write("</tbody>\n")
        file.write("</table>\n")
        file.write("</body>\n")
        file.write("</html>\n")
        #Finaliza ---------------------------------------------------------------------
        file.close()
        webbrowser.open_new_tab("reporte.html")
        print("Operación Exitosa")
    except:
        print("El comando contiene expresiones erroneas")

    #cargar archivo.json, Practica1.json
    #SELECCIONAR nombre, nombre DONDe nombre = "Registro 1"