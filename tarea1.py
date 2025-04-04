
#Ejercicio 1

print("Hola, ya se imprimir frases")

#Ejercicio 2

entero = int("19")
print(entero)

#Ejercicio 3

decimal = float("3.1416")
print(decimal)

#Ejercicio 4

num1 = 1234
num2 = 532
suma = num1 + num2
print(suma)

#Ejercicio 5

num1 = 1234
num2 = 532
resta= num1 - num2
print(resta)

#Ejercicio 6

num1 = 1234
num2 = 532
mult = num1 * num2
print(mult)

#Ejercicio 7

num1 = 1234
num2 = 532
div = num1 / num2
print(div)

#Ejercicio 8

print("1, 2, 3")

#Ejercicio 9

for i in range(1,10):
    print(i)

#Ejercicio 10

for i in range(1,10001):
    print(i)

#Ejercicio 11

print("5, 6, 7, 8, 9, 10")

#Ejercicio 12

for i in range(5,16):
    print(i)

#Ejercicio 13

for i in range(5,15001):
    print(i)

#Ejercicio 14

for i in range(200):
    print("Holaa")

#Ejercicio 15

for i in range(1,31):
    print(i**2)

#Ejercicio 16 

rta = 1
for i in range(1,21):
    rta *= i
print(rta)

#Ejercicio 17

suma = 0
for i in range(1,101):
    suma += i**2
print(suma)

#Ejercicio 18

num = int(input(" "))
suma = 0
for i in range(num, num + 101):
    suma += i
print(suma)

#Ejercicio 19

valor = 1.09
euros = float(input("cuantos euros?: "))
dolar = euros * valor
print(dolar)

#Ejercicio 20

altura = float(input("altura en decimal del rectangulo: "))
base = float(input("base en decimal del rectangulo: "))
area = altura * base
print(area)

#Ejercicio 21

num1 = int(input("escriba un numero: "))
num2 = int(input("escriba otro numero: "))
if num1 > num2:
    print("el numero mayor es: ",num1 ," y el menor es: ",num2,)
elif num1 == num2:
    print("los numeros son iguales")
else:
    print("el numero mayor es: ",num2 ," y el menor es: ",num1,)

#Ejercicio 22

num = int(input(" "))
i = 1
while i < num:
    print(i)
    i += 2

#Ejercicio 23 

def algoritmo(a,b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))
rta = algoritmo(num1, num2)
print(rta)

#Ejercicio 24

num1 = float(input("coeficiente de a: "))
num2 = float(input("coeficiente de b: "))
num3 = float(input("coeficiente de c: "))

if num1 == 0:
    print("no es ecuacion cuadratica")
else:
    x = num2**2 - 4*num1*num3
    if x > 0:
        sol1 = (-num2 + x**0.5) / (2 * num1)
        sol2 = (-num2 - x**0.5) / (2 * num1)
        print("las soluciones son: ", sol1, sol2,)
    elif x == 0:
        x = -num2 / (2 * num1)
        print("la solucion es: ",x ,)
    else:
        print("sus soluciones son complejas")

#Ejercicio 25

numf = int(input("calcular factorial de: "))
factorial = 1
for i in range(1, numf + 1):
    factorial *= i
print(factorial)

num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

while num1 == 0:
    numack = num2 + 1
    break
while num1 > 0 and num2 == 0:
    num1 -= 1
    num2 = 1
while num1 > 0 and num2 > 0:
    num2 -= 1
    while num1 > 0 and num2 == 0:
        num1 -= 1
        num2 = 1
    numack = num2 + 1
print(numack)

#Ejercicio 26

num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))
num3 = int(input("tercer numero: "))

if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("los numeros deben ser positivos")
else:
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
print("el mayor es: ",mayor , "y el menor es: ", menor,)

#Ejercicio 27

def conversion(fahr):
    return(fahr - 32) * 5/9

while True:
    temperaturaF = float(input("temperatura en fahrenheit: "))
    if temperaturaF == 999:
        break
    temperaturaC = conversion(temperaturaF)
    print("la temperatura en celsius es de: ", temperaturaC,)

#Ejercicio 28

for i in range(4):
    print("iteracin:" ,i + 1,)
    
    if i == 0:
        print("mensaje 1")
    elif i == 1:
        print("mensaje 2")
    elif i == 2:
        print("mensaje 3")
    elif i == 3:
        print("mensaje 4")
    else:
        print("no es valido")
    
    print()

#Ejercicio 29

print("No lo entendi :(")

#Ejercicio 30

def primo(num):
    if num <= 1:
        return False
    for i in range (2, num):
        if num % i ==0:
            return False
    return True

numero = int(input("introduce un numero: "))

for numero in range(2, numero + 1):
    if primo(numero):
        print(numero, "es primo")
        

