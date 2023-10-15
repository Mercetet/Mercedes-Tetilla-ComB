import o_y_b_funcion
arr = [9,3,7,5,6,4,8,2]

#ORDENAMIENTO
#Ordenamiento por burbuja(Bubble sort)
# arr = o_y_b_funcion.bubble(arr)

# for i in arr:
#     print(i, end=", ")

#Orden de seleccion(Selection Sort)
# arr = o_y_b_funcion.selection(arr)

# for i in arr:
#     print(i, end=", ")

#Tipo de insercion(Insert Sort)
# arr = o_y_b_funcion.insert(arr)

# for i in arr:
#     print(i, end=", ")

#Combinar ordenamiento(Merge Sort)
# arr = o_y_b_funcion.merge(arr)

# for i in arr:
#     print(i, end=", ")

#BUSQUEDA
element = 4

#Busqueda lineal
# posi = o_y_b_funcion.lineal(arr, element)

# print(f"El elemento se encuentra en la posicion: {posi+1}")

#Busqueda binaria
posi = o_y_b_funcion.binary(arr, element)

print(f"El elemento se encuentra en la posicion: {posi+1} en la lista ordenada. ")