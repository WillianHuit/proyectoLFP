# Simple SQL - Manual de Usuario

SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su
propósito es facilitar al usuario la búsqueda de registros completos en archivos json, en los
que buscar registro por registro podría ser muy tedioso y cansado.

### Primeros Pasos 🚀
* Al iniciar el programa se le mostrara en pantalla un mensaje de bienvenida.
* Debera haber creado previamente un archivo .JSON dentro de la carpeta del programa
* El archivo JSON debe tener la siguiente estructura [Estructura JSON](https://drive.google.com/file/d/11P9Ms_1mJw5y6JSreRBsOOPOWhPQe3Yt/view)
* Cargue sus registros con el comando CARGAR.
* Listo! Ya puede utilizar el programa para realizar sus consultas.

### Consideraciones 📖
* Los comandos pueden ingresarse en mayusculas o minusculas en su totalidad.
* Los comandos pueden ingresarse en mayusculas o minusculas parcialmente.
* Debe deterner el programa una vez terminado de utilizar este mismo.
* Los reportes utilizan librerias online, por lo cual debera contar con acceso a internet.

### Comandos 📋

**Cargar** Este comando permite la carga de diferentes archivos a la memoria.
_Ejemplo de la sintaxis_
```
CARGAR archivo1.json, archivo2.json, archivo3.json, …… archivoN.json
```
_Importante: debe agregar el .json al nombre del archivo, de otro modo este marcara un herror_

**Seleccionar** Permite seleccionar uno o más registros y los muestra en pantalla.
_Ejemplo de la sintaxis_
```
SELECCIONAR [atributo], [atributo] DONDE [atributo] = [busqueda]
```
```
SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Francisco”
```
```
SELECCIONAR *
```
```
SELECCIONAR nombre, edad DONDE promedio = 14.45
```
_El comando seleccionar unicamente permite realizar busquedas mediante un atributo_

**Maximo** Muestra en pantalla el VALOR máximo de un atributo que se encuentre en los registros.
_Ejemplo de la sintaxis_
```
MAXIMO edad
```
_Unicamente se puede obtener el maximo de los atributos PROMEDIO y EDAD_

**Minimo** Muestra en pantalla el VALOR minimo de un atributo que se encuentre en los registros.
_Ejemplo de la sintaxis_
```
MINIMO edad
```
_Unicamente se puede obtener el minimo de los atributos PROMEDIO y EDAD_

**Suma** Muestra en pantalla la suma de todos los valores de un atributo que se encuentre registrados.
_Ejemplo de la sintaxis_
```
SUMA edad
```
_Unicamente se puede obtener la suma de los atributos PROMEDIO y EDAD_

**Cuenta** Muestra en pantalla los registros que se encuentran guardados en la memoria.
_Ejemplo de la sintaxis_
```
CUENTA
```
_El programa unicamente reconoce el comando cuenta si agrega algo mas a la instrucción esta la ignorara_

**Reportar** Muestra una pagina web con el número de registros deseados.
_Ejemplo de la sintaxis_
```
REPORTAR 25
```
```
REPORTAR 30
```
```
REPORTAR N
```
_N es un número que representa la cantidad de registros que se deben tener en el reporte. Evite ingresar letras este comando unicamente
reconoce números_

**Help** Muestra todos los comandos disponibles.
_Ejemplo de la sintaxis_
```
Help
```

**Close** Detiene el progra.
_Ejemplo de la sintaxis_
```
Close
```

### Bugs 📌
Evite realizar algunas de las siguientes acciones.

Realizar varias cargas
_Ejemplo_
```
Linea 1: CARGAR archivo1.json, archivo2.json
```
```
Linea 2: CARGAR archivo3.json, archivo4.json
```
_Al realizar esta acción podrian duplicarse registros, trate de cargar sus archivos en un solo comando_
_Ejemplo_
```
Linea 1: CARGAR archivo1.json, archivo2.json, archivo3.json, archivo4.json
```
## Versionado 📌

Se utilizo [GitHub](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/WillianHuit/proyectoLFP).

## Autores ✒️

_Proyecto realizado por:_

* **Willian Huit** - *Trabajo Total* - [WillianHuit](https://github.com/WillianHuit/)


## Licencia 📄

Este proyecto está bajo la Licencia - mira el archivo [LICENSE.md](LICENSE.md) para detalles

