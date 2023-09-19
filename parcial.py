# Realizar un programa que cumpla con las siguientes condiciones:

# Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
# Generar un menú de opciones, que serán:
# Juego de números.
# Juego de palabras.
# Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
# El mayor número par.
# El promedio de los números impares.
# Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
# No olvides realizar las debidas validaciones!

name = str(input("Ingrese su nombre: "))

if name <= "z" and name >= "a": 

    print(f"Hola {name}. ")
    print("1. Juego de numeros.")
    print("2. Juego de palabras.")

    op = int(input(f"{name}, ingrese el numero correspondiente a la opcion elegida: "))
    maxi = 0
    prom = 0
    count = 0
    add = 0
    a=0
    e=0
    i=0
    o=0
    u=0

    #verifica q el numero sea 1 o 2
    if (op < 3 and op > 0):
        #verifica que la opcion sea 1
        if op == 1:
            while True:
                num = int(input(f"{name}, ingrese un numero entero, 0 para salir: "))
                #verifica que el numero sea 0
                if num == 0:
                    print(f"{name}, salio del programa. ")
                    break
                #Si el numero no es 0 hace lo siguiente.
                else:
                    if (num % 2) == 0:
                        if num > maxi:
                            maxi = num
                    else:
                        count +=1
                        add = add + num
                        prom = add/count
            print(f"{name}, el numero par mas grande ingresado es: {maxi}")
            print(f"{name}, el promedio de los numeros impares ingresados es: {prom}")

        elif op == 2:
            phrase = str(input(f"{name}, ingrese una frase: ")).lower()
            for v in phrase:
                if v == "a":
                    a +=1
                elif v == "e":
                    e += 1
                elif v == "i":
                    i += 1
                elif v == "o":
                    o += 1
                elif v == "u":
                    u += 1
            print(f"Se contaron {a} a")
            print(f"Se contaron {e} e ")
            print(f"Se contaron {i} i ")
            print(f"Se contaron {o} o ")
            print(f"Se contaron {u} u ")



