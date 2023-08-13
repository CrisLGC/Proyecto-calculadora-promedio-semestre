Documentación del proyecto de la calculadora de promedio de un semestre

Primero definí las funciones que utilizaré durante el código
prom2: siendo una función para sacar el promedio entre dos dígitos
prom5: siendo una función para sacar el promedio entre cinco dígitos
prom4: siendo una función para sacar el promedio entre cuatro dígitos

En la línea número 13 empieza la codificación del programa utilizando un print para pedirle al usuario que ingrese la nota que obtuvo en su primer parcial de matemática
luego uso un if para programar la condición de que si el número que ingreso no está en el rango del 1 al 20 (ya que esta es la calificación que se utiliza en Venezuela)
entonces imprima un mensaje diciéndole al usuario que hubo un error y que ingrese por favor una nota válida.
Repetimos este proceso con los 4 parciales de la materia.
Y almacenamos en una variable a la función prom4 usando como elementos a las cuatro notas de los parciales
Si todas las notas que ingreso son válidas, pasará a repetirse el mismo proceso anterior con cada materia.
Una vez el usuario ingreso todas sus notas de cada uno de los parciales que presento en cada materia se sacara su promedio total del semestre.
En la línea número 108 usamos un print para imprimir el resultado de llamar a una función anidada entre la función prom5 y las funciones prom4 que almacenamos en cada una de las cinco materias, de esta manera la función prom5 saca el promedio entre el promedio de cada una de las 5 materias e imprime el resultado para que el usuario lo obtenga.
