# Programa-de-gesti-n-de-cobros

---> A continuacion los requerimientos del trabajo realizado...

Una empresa dedicada a la gestión de peajes en rutas requiere un programa para gestionar los movimientos de cobro
en cada una de sus ventanillas. Por cada ticket cobrado se tienen los siguientes datos: número de ticket (un entero),
nombre de puesto de peaje (una cadena de caracteres), un número entre 1 y 10 para indicar la ventanilla o carril que
hizo el cobro en ese puesto, una cadena para la patente del automóvil al que se le hizo el cobro, y finalmente un
número entero para indicar el monto que se cobró.
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos [Máximo 4 puntos
por este requerimiento, incluyendo también convenciones de estilo y otros aspectos del programa general]:
• En uno de ellos, definir la clase Ticket que represente al registro a usar en el programa, y las funciones básicas
para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de
datos, aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones
para desarrollar las siguientes tareas:

[1]. Generar un arreglo de n registros de tipo Ticket que contenga los datos de los cobros realizados (cargue el valor de
n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
generando los datos en forma aleatoria. El arreglo debe permanecer en todo momento ordenado por el número
de ticket durante la carga. Cada vez que se seleccione esta opción, el arreglo debe ser generado nuevamente
desde cero. Será considerada la eficiencia de la estrategia de carga y los algoritmos que aplique. [Máximo 4 puntos
entre los ítems 1 y 2 juntos].

[2]. Mostrar todos los datos del arreglo generado en el punto 1, a razón de un registro por renglón. Al final del listado,
muestre una línea adicional con el monto total recaudado por todos los tickets que se mostraron. [Máximo 4
puntos entre los ítems 1 y 2 juntos].

[3]. En base al arreglo generado en el punto 1 determinar si existe un ticket cuyo número sea num (cargar num por
teclado). Si existe, informe solo el nombre del puesto de peaje y el número de ventanilla o carril de ese registro. Si
no existe, informe con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que cumpla el
criterio de busqueda pedido. [Máximo 4 puntos].

[4]. En base al arreglo generado en el punto 1, determinar cuántos tickets se cobraron en cada una de las 10 posibles
ventanillas o carriles posibles. Mostrar solo los contadores diferentes de cero. [Máximo 4 puntos].

[5]. En base al arreglo generado en el punto 1 determinar cuántas veces se le cobró peaje al automóvil cuya patente es
pat (cargue la cadena pat por teclado). Note que esa patente podría estar varias veces en el vector, y ahora sí se
pide contar todas sus apariciones. Si no existe ningún ticket emitido para esa patente, informe con un mensaje.
[Máximo 4 puntos].

[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
tickets emitidos por ventanillas con número menor a 6. [Máximo 4 puntos].

[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando la cantidad de registros
mostrados. [Máximo 4 puntos].
