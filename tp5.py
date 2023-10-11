import funciones

# 1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
# dni = input("Inserte un numero de DNI.")
# print(funciones.comprobation(dni))

# 2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
# phrase = input("Ingrese una frase: ").lower()
# print(funciones.word_lenght(phrase))

# 3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254
# bo = True
# bo2 = True
# while bo:
#     info = input("Ingrese su nombre completo: ").lower()
#     name = funciones.wordselector(info,0).capitalize()
#     last_name=funciones.wordselector(info,-1)
    
#     if info=="":
#         print("Saliendo del programa. ")
#         break
#     else:
#         last_len = len(last_name)
#         while (bo2):
#             dni = input("Ingrese su DNI: ")
#             if funciones.comprobation(dni):
#                 first= funciones.three_first_dni(dni)
#                 print(f"{name}{last_len}{first}")
#                 break
#             else:
#                 print("Ingreso mal el DNI. Intente nuevamente. ")

# 4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo. !!!!!!!!!!!!!!!!!!!!!!!!!
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# funciones.multiple(num1, num2)

# 5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
# days = int(input("Ingrese de cuantos dias desea calcular la temperatura: "))
# for i in range(days): 
#     min=int(input(f"Ingrese la temperatura minima de el dia {i+1}: "))
#     max=int(input(f"Ingrese la temperatura maxima de el dia {i+1}: "))
#     avg = funciones.temperature(min, max)
#     print(f"La temperatura media del dia {i+1} fue de: {avg}")

# 6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
# phrase = input("Ingrese una frase: ")
# print(funciones.spaces(phrase))

# 7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
# num_list = []
# while True:
#     nums = int(input("Ingrese numeros (0 para salir): "))
#     if nums == 0:
#         break
    
#     num_list.append(nums)
#     min, max = funciones.min_max(num_list)
#     print(f"El numero maximo de la lista es: {max} y el minimo es: {min}")

# 8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
# radio = int(input("Ingrese el radio de la circunferencia: "))
# area, perim = funciones.area_per_circle(radio)
# print(f"El area es {area} y el perimetro es {perim}")

# 9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

# for i in range (3):
#     user = input("Ingrese el nombre de usuario: ")
#     password = input("Ingrese la contraseña: ")
#     bo = funciones.login(user, password, i)
#     if bo:
#         print("Bienvenido.")
#         break

# 10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# dicc = {"200" : "25", "1000" : "50", "100" : "5", "500" : "40"}

# 11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
# list1=[10,20,30,40,50]
# list2= funciones.list_func(list1, funciones.multi)
# print(list2)

# 12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
# phrase = input("Ingrese una frase.")
# print(funciones.long_phrase(phrase))

# 13.	Escribir una función que calcule el módulo de un vector.
# cath = int(input("Ingrese el cateto A."))
# cath2 = int(input("Ingrese el cateto B."))
# print(funciones.hypo(cath, cath2))

# 14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
# num = int(input("Ingrese un numero entero."))
# print(funciones.prime(num))

# 15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
# num = int(input("Ingrese un numero."))
# print(funciones.factorial(num))

# 16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.
# num = input("Ingrese un numero.")
# dig = input("Ingrese un digito.")
# print(funciones.serch_dig(num, dig))

# 17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.
top = 0

while True:
    prime = int(input("Ingrese un numero primo (numero no primo para finalizar.): "))
    if prime <= 1:
        break
    if funciones.prime(prime):
        if prime > top:
            top = prime
        
        print(f"La suma de los digitos en {prime} es: {funciones.sum_dig(prime)}.")
        dig=int(input("Ingrese un digito: "))
        count = funciones.serch_dig(prime, dig)
        print(f"El digito {dig} aparece {count} veces en {prime}.")
    else:
        print("Saliendo del programa...")
        break

print(f"El factorial de {top} es: {funciones.factorial(top)}.")

