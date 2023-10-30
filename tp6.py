import random

# # 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
# nums = []
# original = []

# while True:
#     num = int(input("Ingrese un numero(0 para salir): "))
#     if num == 0:
#         break
#     else:
#         nums.append(num)
#         original.append(num)
# print(nums)
# # 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
# remove_num = int(input("Ingrese un numero a eliminar de la lista: "))
# if remove_num in nums:
#     nums.remove(remove_num)
#     print("Se elimino correctamente.")
# else:
#     print("No se pudo eliminar. ")
# print(nums)
# # 3.	Imprimir la sumatoria de todos los números de la lista.
# aux = 0
# for num in nums:
#     aux += num
# print(aux)

# # 4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
# new_nums = []
# new_num = int(input("Ingrese un numero: "))
# for num in nums:
#     if num < new_num:
#         new_nums.append(num)
# print(new_nums)

# # 5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)
# new_list = []
# for i in original:
#     count = 0
#     for j in original:
#         if i == j:
#             count +=1
#     if (i,count) not in new_list:
#         new_list.append((i,count))

# print(new_list)

# 6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
# primary = []
# high = []

# while True:
#     p_alum = input("Ingrese un alumno de primaria ('x' para salir): ").title()
#     if p_alum == "X":
#         break
#     else:
#         primary.append(p_alum)

# while True:
#     h_alum = input("Ingrese un alumno de secundaria ('x' para salir): ").title()
#     if h_alum == "X":
#         break
#     else:
#         high.append(h_alum)
    
# # a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# primary = list(set(primary))
# print(f"Alumnos del nivel primario: {primary}")
# high = list(set(high))
# print(f"Alumnos del nivel secundario: {high}")

# # b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# repeated = list(set(primary) & set(high))
# print(f"Nombres que se repiten: {repeated}")

# # c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
# not_repeated = list(set(primary) - set(high))
# print(f"Nombres que no se repiten: {not_repeated}")

# 7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
# ‘r’:5
# ‘%’:3
# ‘a’:8
# ‘9’:1
# strings={}

# for i in range(50):
#     string = input("Ingrese un string: ")
#     for j in string:
#         if j in strings:
#             strings[j] +=1
#         else:
#             strings[j]=1

# print("Ocurrencias de cada caracter: ")
# for j, k in strings.items():
#     print(f"{j}:{k}")

# 8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
# Los goles anotados en cada encuentro se registraron en el siguiente cuadro:

# Escriba un programa que:
# o	Lea el cuadro de goles en un arreglo de dos dimensiones.
# rows = 10
# cols = 10
# final = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         if i != j:
#             row.append(random.randint(1,8))
#         else:
#             row.append(0)
#     final.append(row)

# for row in final:
#     print(row)

# # o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
# win=[0]*10
# lose = [0]*10
# tie = [0]*10
# for i in range(10):
#     for j in range(10):
#         if i==j:
#             continue
#         else:
#             if(final[i][j] == final[j][i]):
#                 tie[i] += 1
#             elif(final[i][j] > final[j][i]):
#                 win[i] += 1
#             else:
#                 lose[i] += 1

# for i in range(10):
#     print(f"Equipo {(i+1)}:")
#     print(f"Triunfos: {win[i]}")
#     print(f"Empates: {tie[i]}")
#     print(f"Derrotas: {lose[i]}")
#     print("")

# # o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
# # o	Determine la cantidad de puntos obtenidos por cada equipo.
# ours = [0]*10
# their = [0]*10
# sust = [0]*10

# for i in range(10):
#     for j in range(10):
#         ours[i] += final[i][j]
#         their[i] += final[j][i]

# for i in range(10):
#     sust[i] = ours[i]-their[i]

# for i in range(10):
#     print(f"Equipo {(i+1)}:")
#     print(f"Goles metidos: {ours[i]}")
#     print(f"Goles recividos: {their[i]}")
#     print(f"Diferencia: {sust[i]}")
#     print("")

# 9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.
# board = []
# hide = ["A", "B", "C", "D", "E", "F", "A", "B", "C", "D", "E", "F"]
# random.shuffle(hide)

# for i in range(3):
#     row = hide[i * 4: (i + 1) * 4]
#     board.append(row)

# opened = [['[ ]'] * 4 for _ in range(3)]
# found = 0

# while found < 6:
#     for i in range(3):
#         for j in range(4):
#             print(opened[i][j], end=" ")
#         print("")

#     row = int(input("Ingrese la fila de la primer carta (1-3):") )- 1
#     col = int(input("Ingrese la columna de la primer carta (1-4):")) - 1

#     if not (0 <= row <= 2 and 0 <= col <= 3):
#         print("Ingreso mal. Intente otra vez.")
#         continue

#     if opened[row][col] != '[ ]':
#         print("La carta ya está abierta. Elija otra.")
#         continue

#     opened[row][col] = board[row][col]
#     for i in range(3):
#         for j in range(4):
#             print(opened[i][j], end=" ")
#         print("")
#     row2 = int(input("Ingrese la fila de la segunda carta (1-3):")) - 1
#     col2 = int(input("Ingrese la columna de la segunda carta (1-4):")) - 1

#     if not (0 <= row2 <= 2 and 0 <= col2 <= 3):
#         print("Ingreso mal. Intente otra vez.")
#         continue

#     if opened[row2][col2] != '[ ]':
#         print("La carta ya está abierta. Elija otra.")
#         continue

#     opened[row2][col2] = board[row2][col2]
#     for i in range(3):
#         for j in range(4):
#             print(opened[i][j], end=" ")
#         print("")

#     if opened[row][col] == opened[row2][col2] and (row != row2 or col != col2):
#         found += 1
#         print("¡Muy bien!")
#     else:
#         print("Te equivocaste. Inténtalo otra vez.")
#         opened[row][col] = '[ ]'
#         opened[row2][col2] = '[ ]'

# print("¡Encontraste todas las parejas. Ganaste!")

# 10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a.	la diagonal principal.
# b.	la diagonal inversa.
# n = 3 
# square = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# print("Matriz original:")
# for row in square:
#     print(row)

# main_diagonal = [square[i][i] for i in range(n)]

# reverse_diagonal = [square[i][n - 1 - i] for i in range(n)]

# print(f"Diagonal principal:{main_diagonal}")
# print(f"Diagonal inversa:{reverse_diagonal}")

# 11.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# money = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# currency = input("Ingrese una divisa.").title()
# if currency in money:
#     aux = money[currency]
#     print(f"El simbolo del tipo de moneda {currency} es {aux}")
# else:
#     print("No se encuentra este tipo de divisa.")

# 12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’.
# name = input("Ingrese su nombre.").capitalize()
# age = input("Ingrese su edad.")
# address = input("Ingrese su direccion.")
# num = input("Ingrese su telefono.")
# data = {
#     'name' : name,
#     'age' : age,
#     'address' : address,
#     'num' : num
# }
# print(f"{data['name']} tiene {data['age']} años, vive en {data['address']} y su numero de telefono es {data['num']}")

# 13.	Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
fruitprices = {
    'manzana' : 300,
    'pera' : 250,
    'uva' : 230,
    'banana' : 600,
    'frutilla' : 1000
}
fruit = input("Ingrese que fruta quiere comprar")
if fruit in fruitprices:
    kg = float(input("Ingrese la cantidad de kilos a llevar."))
    total = fruitprices[fruit] * kg
    print(f"El total de llevar {kg} kg de {fruit} es de {total}")
else:
    print("La fruta no esta en el catalogo.")