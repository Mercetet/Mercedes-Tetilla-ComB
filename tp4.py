# 1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

sentence = str(input("Ingrese una frase: "))
num = 999

for i in range(num):
    print(sentence.upper())
    sentence = str(input("Ingrese una frase. Enter para salir: "))
    if not sentence:
        print("Finalizo.")
        break
    else:
        continue

# 2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50

# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos

# Ejemplo de una entrada:
# D 200
# D 200
# R 100
# D 50
# Introducir una línea vacía indica que ha finalizado la bitácora.
# La salida de éste programa sería:
# 350

tot = 0

while True:
    data = input("Ingrese q va a realizar (deposito/retiro) y el monto.(D/R cantidad)").lower()
    if not data:
            print("Finalizo.")
            break
    op = data[0:data.find(" ")].lower()
    amount = int(data[data.find(" ")+1:])
    if(op == "r"):
        tot -= amount
    elif(op == "d"):
        tot += amount

print(f"Monto: {tot}")

# 3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
count = 0
num = 4

while True:
    num = int(input("Ingrese un numero entero mayor que 1. 0 para salir."))
    if(num == 0):
        break
    if num < 0: 
        print("Ingreso un numero negativo. Intente otra vez. ")
    else:
        if num == 2:
            count += 1
        elif num > 2 and num % 2 != 0:
            prime = True
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                count += 1

print(f"La cantidad de numeros primos ingresados es: {count}")

# 4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
start = int(input("Ingrese un año para iniciar. "))
end = int(input("Ingrese un año para finalizar. "))

for i in range(start, end+1):
    if (((i % 4) == 0 and ((i % 100) != 0)) or (((i % 100) == 0) and (((i % 400) == 0))) or (i % 10 == 0)):
        print(i, end=", ")

# 5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.
for i in range(1, 20+1):
    if (i % 2 != 0):
        continue
    print(i, end=", ")

# 6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.
list1 = [2,9,0,4,1,5,6,3,7,8]
num = 3

for i in list1:
    if i == num:
        print("El numero fue encontrado.")
        break

# 7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
while True:
    print("MENU")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    op = int(input("Ingrese una opcion: "))
    if op==1:
        print("Hola!! ")
    elif op == 2:
        print("Como estas??")
    elif(op == 3):
        print("Chau!")
    elif(op == 0):
        break
    else: 
        print("La opcion no esta en el menu. Intente nuevamente.")

