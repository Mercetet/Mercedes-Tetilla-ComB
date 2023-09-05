# 1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
word = str(input("Inserte una palabra."))
for times in range(10):
    print(f"{word}")

# 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("Ingrese su edad. "))
first = 0
for i in range(age):
    first += 1
    print(first)

# 3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num = int(input("Ingrese un numero entero positivo: "))
odd = 0
for i in range(num):
    odd += 1
    if (odd%2!= 0):
        print(odd, end=", ")

# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Ingrese un numero entero positivo: "))
odd = 0

for i in range(num+1):
    print(num, end=", ")
    num -= 1

# 5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cash = float(input("Ingrese una cantidad a invertir: "))
interest = int(input("Ingrese el interes anual: "))
years = int(input("Ingrese el numero de años: "))
total = 0
cash2 = 0
for i in range(years):
    total = cash + (cash*interest)/100
    cash2 += total
    print(f"En el {i+1}° año obtubo ${cash2}.")

# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
size = int(input("Ingrese un tamaño para el triangulo. "))
for i in range(size):
    for j in range(i+1):
        print("*", end=" ")
    print("")

# 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range(10+1):
    for j in range(10+1):
        total =j*i
        print(f"{i} x {j} = {total}")

# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
num = int(input("Ingrese un numero entero. "))
for i in range(1, num * 2, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = "stiles"
word = "hi"
while (word != password):
    word = str(input("Inserte una contraseña. "))
print("Ingreso la contraseña correcta.")

# 10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num = int(input("Ingrese un numero entero. "))
if num <= 1:
    print("No es un número primo")
else:
    prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print("Es un número primo")
    else:
        print("No es un número primo")

# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = str(input("Inserte una palabra. "))
for i in range(len(word) - 1, -1, -1):
    print(word[i])

# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
word = str(input("Inserte una frase. "))
letter = str(input("Inserte una letra. "))
count=0
for i in word:
    if i == letter:
        count += 1
print(f"Se encontraron {count} letras {letter} en la frase.")

# 13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
word = ""
ex = "salir"
while word != ex:
    word = str(input("Ingrese una palabra: "))
    print(word)

# 14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
num = int(input("Ingrese un numero entero. "))
num2 = int(input("Ingrese un numero entero. "))
i = num
for num in range(num2-1):
    if (i % 2 == 0):
        print(f"{i} es par")
        i += 1
    else:
        print(f"{i} es inpar")
        i += 1

# 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num = int(input("Ingrese un numero entero. "))
count = 1
for i in range(1, num +1):
    if (num%i == 0):
        print(i)

# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
count = int(input("Cuantos numeros va a introducuir. "))
negative = 0
for i in range(count):
    num = int(input("Ingrese un numero. "))
    if (num < 0):
        negative += 1
print(f"Ingreso {negative} numeros negativos")

# 17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
sent = str(input("Ingrese una frase: ")).lower()
vocals = "aeiou"
count=""
for i in sent:
    if i in vocals and i not in count:
        count += i

print(f"Vocales encontradas: {count}")

# 18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
num = 0
num2 = 1
for i in range(10):
    print(num, end=" ")
    num, num2 = num2, num + num2

# 19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
obj = int(input("Ingrese la cantidad que desea ahorrar: "))
savings = 0
tot = 0
while tot < obj:
    savings = int(input("Ingrese la cantidad que ingreso: "))
    if (savings > 0):
        tot += savings
    else:
        print("ingreso un numero negativo")
print(f"Alcanzo el objetivo!! {tot}")

# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
num = 1
num2 = 0
while num != 0:
    num = int(input("Ingrese un numero (salir con 0): "))
    num2 += num
print(f"La suma de los numeros es: {num2}")

# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
num = 1
top = 0
while num != 0:
    num = int(input("Ingrese un numero (salir con 0): "))
    if(num > top):
        top = num

print(f"El mayor numero es: {top}")

# 22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
num = 0
count = 0
while num != -1:
    num = int(input("Ingrese un número entero positivo (-1 para salir): "))
    add = 0
    num2 = num    
    while num2 > 0:
        digit = num2 % 10
        add += digit
        num2 //= 10
    print(f"La suma es {add}")
    if num % 2 == 0:
        count += 1
print(f"Total de números pares ingresados: {count}")

# 23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
num = 1
tot= 0
while num != 0:
    num = int(input("Ingrese los montos de los productos (0 para salir): "))
    tot += num
print(f"El monto total es: {tot}")

# 24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
tot= 0
num = int(input("Ingrese los montos de los productos (0 para salir): "))
while num != 0:
    if num < 0:
        print("Ingreso un monto negativo, intente nuevamente. ")
    else:
        tot += num
    num = int(input("Ingrese los montos de los productos (0 para salir): "))
if tot >1000:
    pay = tot - (tot *0.10)
    print(f"El total a pagar, con descuento, es de {pay}.")
else:
    print(f"El total a pagar es: {tot}")

# 25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
num = int(input("Ingrese un número entero: "))
if num < 0:
    print("Ingreso un numero negativo.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")