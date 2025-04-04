Desde los ejercicios 1 hasta el 15 considero que es bastante simple comprender las lineas de codigo, son cosas supremamnete bascias como operaciones simples y bucles

![Image_Alt](https://github.com/SANPEREZAL/TareaN1/blob/037659a2998e6fd6628b267dde37de35700b56e4/1-8.jpg)

En el ejercicio 16 lo que hacemos con el bucle for es repetir un proceso, y con la funcion range es tomamos los 20 primeros numeros anturales (1-20), para despues multiplicarlos entre ellos cada vez que se complete un ciclo

En el ejercicio 17 evidenciamos un proceso parecido, solo que esta vez los numeros del 1 al 100, entonces el ciclo for toma cada uno de estos numeros y los eleva al cuadrado, para luego sumarlos una vez recorridos los 100

En el ejercicio 18 el usuario introduce un numero entero, y el ciclo for recorre el rango comprendido entre el numero que se digito y sus 100 numeros siguientes, para luego imprimir la suma de todos los numeros que fueron recorridos

En el ejercicio 19, asignamos a la variable valor la equivalencia euros = dolar (1 euro = 1.09 dolares), para luego por medio de un input, hacer que el usuario introduzca la cantidad de euros que quiere transformar, y luego que la variable dolar este determinada por la multiplicacion de la cantidad de euros por el valor de la equivalencia

En el ejercicio 20 simplemente conociendo la formula del area de un rectangulo (base x altura) hacemos que el usuario ingrese ambos valores, para luego hacer una operacion sencilla como la de los primeros puntos

En el ejercicio 21 usamos la condicion if, donde luego de haber introducido nos numeros enteros, esta condicion if evalua cual de los dos es mayor e imprime si el primero es mayor que el segundo, o si el segundo es mayor que el primero, y en caso de que sean iguales, tambien el programa imprime que ambos valores son iguales

En el ejercicio 22, luego de que el usuario haya introducido un numero, el ciclo while recorrera todos los numeros menores al que fue introducido (empezando desde el 1) y simplemente les sumara 2 unidades a cada uno para asi obtener todos los impares menor al valor de entrada

En el ejercicio 23, definimos la funcion algoritmo, el la cual el ciclo while seguira funcionando siempre y cuando b no sea 0, y en el a tomara el valor de b y b el resto de la divison entre a y b (a % b), asi cuando b alcance el valor de 0, el ciclo retornara el valor de a, el cual seria el gcd (MCD)

Para resolver el ejercicio 24 debemos recordar que para hayar las soluciones de una ecuacion cuadratica, se debe cumplir la condicion de que el primer coeficiente no puede ser 0, por lo que luego de que el usuario digitara sus 3 numeros, lo primero que hace el condicional es verificar esto, y en caso de que a = 0, el programa imprimira inmediatamente que la ecuacion no es cuadratica, en caso de no ser asi, pasamos a hayar el discriminante, que es el que nos permite determinar las posibles soluciones, en donde se pueden presentar 3 casos: a- el discriminante es mayor a 0, por ende la ecuacion tiene dos soluciones reales, b- el discriminante es 0, por lo que tendria una solucion real, y c- el discriminante es menor a 0, por lo que para solucionar la ecuacion tendriamos que recurrir a los numeros complejos

En el ejercicio 26, luego de haber introducido los 3 numeros a evaluar, el ciclo if verifica en primera instancia que se cumpla el requerimiento de que los 3 numeros deben ser enteros naturales, por ende si alguno es menor que 0, el programa simplemente imprimira que los numeros deben ser positivos, en caso de haber introducido valores validos, el programa simplemente mediante las funciones min y max determina el valor mayor y menor del conjunto de 3 numeros dimos de entrada, e imprime cual es el mayor y cual es el menor

En el ejercicio 27, definimos la funcion conversions, en la que digitamos la conversion respectiva de fahrenheit a celsius, y por medio del input el usuario podra introducir el valor que quiera convertir de fahrenheit a celsius, y el programa por medio del while True, se seguira ejecutando hasta que el usuario digite como temperatura 999, y se imprimira el valor convertido a celsius en caso de no haber intentado con 999

En el ejercicio 28, se nos pide que implementemos una sentencia switch, pero al no existir en python, recurri al uso de concidionales if,elif,else, en donde luego de haber usando el ciclo for, el programa evaluara los valores de i e imprimira respectivamente un mensaje de prueba para cada iteracion que se haga. En el ejercicio no hice uso de los break porque simplemente luego de imprimir un mensaje el programa se detendria, por lo que si agregamos la sentencia break, el programa simplemente se detendra luego de una impresion, por lo que al removerlo lo unico que pasara es que el programa continuara imprimiendo las veces que sean necesarias

No entendi muy bien el ejercicio 29, no lo realice

Y para finalizar, en el ejercicio 30, definimos la funcion primo, en la que si el numero que intrducimos es menor o igual a 1, directamente el programa retornara false, porque el numero primo mas chiquito es 2, entonces el rango de nuestra funcion debe estar entre el 2 y el numero de entrada. Si el resto de la division entre nuestro numero y el valor que tome i es 0, eso quiere decir que nuestro numero no es primo, por lo que el programa retorna false nuevamente. Y ya para terminar con este ejercicio, el ultimo ciclo for recorre los numeros desde el 2 hasta el valor de entrada, y si ese valor luego de haber pasado por la funcion primo retorna True, significa que es un numero primo, por lo que se imprime
