#Ejercicio 1
abc = "abcdefghijklmnopqrstuvwxyz"
corre = int(input("Ingrese el corrimiento: "))
for i in range(5):
    msj = input("Ingrese el mensaje: ")
    msj2 = ""
    for letra in msj:
        if letra in abc:
            index = abc.index(letra)
            index2 = (index + corre) % len(abc)
            cesar = abc[index2]
            msj2 += cesar
        else:
            msj2 += letra
    print(f"Mensaje: {msj2}")

#Ejercicio 2
par = 0
inpar = 0

num = int(input("Ingrese numeros enteros positivos. Ingrese 0 para salir. "))

while (num != 0):
    if(num%2 == 0):
        par +=1
    else:
        inpar+=1
    num = int(input("Ingrese numeros enteros positivos. Ingrese 0 para salir. "))
print(f"Ingreso {par} numeros pares y {inpar} numeros inpares. ")

