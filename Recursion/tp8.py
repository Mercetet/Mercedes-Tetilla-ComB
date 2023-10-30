import funcion_recursion

# 1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
# num = int(input("Ingrese un numero positivo: "))
# dig = funcion_recursion.count_dig(num)
# print(f"El numero {num} tiene {dig} digitos. ")

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
# n = int(input("Ingrese un numero para la base: "))
# b = int(input("Ingrese un numero para ver si es potencia: "))
# print(f"El numero {n} es potencia de {b}: {funcion_recursion.power_num(n, b)}")

# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:
# a = input("Ingrese una frase: ").lower()
# b = input("Ingrese lo q desea buscar en la frase: ").lower()
# print(funcion_recursion.search_str(a,b))

# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.
# num = int(input("Ingrese un numero: "))
# if funcion_recursion.even_num(num):
#     print(f"El numero {num} es par.")
# else:
#     print(f"El numero {num} es impar.")

# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.2
# list_num = []
# while True:
#     num = int(input("Ingrese un numero a la lista. (-1 para salir)"))
#     if num == -1:
#         break
#     else:
#         list_num.append(num)

# if len(list_num) > 0:
#     max_num =funcion_recursion.max_num(list_num)
#     print(f"El numero mas grande de la lista es: {max_num}")
# else:
#     print("La lista esta vacia. ")

# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
# list_num = []
# while True:
#     num = int(input("Ingrese un numero a la lista. (-1 para salir)"))
#     if num == -1:
#         break
#     else:
#         list_num.append(num)
# n = int(input("Ingrese la cantidad de veces q desea que se repitan los elementos de la lista: "))
# if len(list_num) > 0:
#     final = funcion_recursion.repeat_list(list_num, n)
#     print(final)
# else:
#     print("La lista esta vacia. ")

# 7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número d,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)
# n = int(input("Ingrese un numero: "))
# p = int(input("Ingrese otro numero: "))

# print(funcion_recursion.add_mult(n,p))

# 8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
# n = int(input("Ingrese un numero para la fila: "))
# k = int(input("Ingrese un numero para la columna: "))

# print(f"El valor que se encuentra en la fila {n} y columna {k} es: {funcion_recursion.pascal(n,k)}")

# 9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).
# list_char = []
# while True:
#     char = input("Ingrese un caracter a la lista. (0 para salir)").lower()
#     if char == '0':
#         break
#     else:
#         list_char.append(char)

# k = int(input("Ingrese la longitud de las cadenas de la combinacion de caracteres de la lista: "))

# new_list = funcion_recursion.conbinations(list_char, k)

# print(new_list)

# 10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.
n = int(input("Ingrese el numero de la hoja a la que desea calcular el alto y ancho: Hoja A"))

length, width = funcion_recursion.paper_size(n)
print(f"El largo de la hoja es: {length}, y el ancho es: {width}")