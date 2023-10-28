import o_y_b_funcion

# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.
# num = [123,245,23,989,91, 4]
# print(f"Lista original: \n{num} \nLista ordenada: ")
# arr = o_y_b_funcion.bubble(num)
# print(arr)

# 2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
# arr = ["Pepe", "Juan", "Abril", "Lola"]
# print(f"Lista original: \n{arr} \nLista ordenada: ")
# ord = o_y_b_funcion.selection(arr)
# print(ord)

# 3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.
# dic_list = [
#     {"titulo":"La razon de estar contigo",
#     "autor" : "Pepe",
#     "anio": 2015
#     },
#     {
#     "titulo": "El nombre del viento",
#     "autor": "Juan",
#     "anio": 2019
#     },
#     {
#     "libro":"Antes de diciembre",
#     "autor": "Joana",
#     "anio": 2014
#     },
#     {
#     "libro":"Damian",
#     "autor": "Lola",
#     "anio": 2017
#     }
# ]
# print(f"Diccionario original: ")
# for i in dic_list:
#     print(i)
# print("Diccionario ordenado por año: ")
# dic_list.sort(key=lambda x: x["anio"])
# for i in dic_list:
#     print(i)

# 4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.
# arr = ["Pepe", "Juanito", "Abril", "Lolita"]
# len_arr = []
# final = []

# for i in arr:
#     len_arr.append(len(i))

# len_arr.sort()

# for i in len_arr:
#     for j in arr:
#         if i == len(j):
#             final.append(j)

# print(f"Lista original: \n{arr} \nLista ordenada: \n{final}")

# 5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.
# num = [123,245,23,989,91, 4]
# print(f"Lista original: \n{num} \nLista ordenada descendente: ")
# num.sort()
# num.reverse()
# print(num)

# 6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.
# num = [123,245,23,989,91, 4]
# print(f"Lista original: \n{num} \nLista ordenada: ")
# arr = o_y_b_funcion.counting(num)
# print(arr)

# 7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.
# arr = [989, "Pepe", 123, 4, "Juanito",245, "Abril", 23, "Lolita", 91,]
# nums = []
# st_arr = []

# print(f"Lista original: \n{arr} \nLista ordenada: ")

# for i in arr:
#     if isinstance(i, int):
#         nums.append(i)
#     else:
#         st_arr.append(i)

# nums.sort()
# st_arr.sort()

# print(nums + st_arr)

# 8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.
arr = [123,245,23,989,91, 4]
arr = o_y_b_funcion.merge(arr)

for i in arr:
    print(i, end=", ")