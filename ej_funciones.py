import funciones;

num = int(input("Numero a procesar: "))
aux = 0

while num != 0:
    aux += num
    print(f"Sumo: {funciones.add_digits(num)}")
    num = int(input("Numero a procesar: "))
    
print(f"La suma de los numeros es: {aux}")
print(f"La suma de los digitos es: {funciones.add_digits(aux)}")