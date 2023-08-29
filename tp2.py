import math

# 1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el 
# computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
anios = int(input("Ingrese cuantos años tiene su computadora."))

if (anios <= 2):
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

# 2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
anios = int(input("Ingrese cuantos años tiene su computadora."))

if (anios < 0):
    print("Error.")
elif (anios <= 2):
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
# A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir 
# ‘no hay coincidencia’.
nom1 = str(input("Ingrese un nombre. ")).lower()
nom2 = str(input("Ingrese un nombre. ")).lower()

if(nom1[0] == nom2[0]):
    print("Coincidencia.")
else:
    print("No hay coincidencia.")

#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
voto = str(input("Ingrese a qu candidato votar. A, B o C. ")).lower()

if(voto == "a"):
    print("Voto por el partido rojo.")
elif(voto=="b"):
    print("Voto por el partido verde.")
elif(voto=="c"):
    print("Voto por el partido azul.")
else:
    print("Opcion erronea.")

#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
letra = str(input("Ingrese una letra. ")).lower()

if(len(letra)==1):
    if(letra == "a" or letra == "e" or letra == "i" or letra == "a" or letra == "o" or letra == "u"):
        print("Ingreso una vocal.")
    else:
        print("Ingreso una consonante.")
else:
    print("No se puede procesar")

#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
anio = int(input("Ingrese un año. "))

if (((anio % 4) == 0 and ((anio % 100) != 0)) or (((anio % 100) == 0) and (((anio % 400) == 0)))):
    print("El año es bisiesto.")
else:
    print("El año no fue bisiesto.")

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
num1 = int(input("Ingrese un numero. "))
num2 = int(input("Ingrese otro numero. "))
num3 = int(input("Ingrese otro numero. "))

may = num1

if(num2 > may):
    may=num2
if(num3> may):
    may = num3
print(f"El numero mas grande es: {may}")

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
nom = str(input("Ingrese un nombre de usuario. "))
cont = str(input("Ingrese una contraseña. "))

if((nom == "Gwenevere") and (cont == "excalibur")):
    print("Puede ingresar a Camelot.")
else:
    print("Acceso denegado")

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nom = str(input("Ingrese su nombre. ")).lower()
sexo = str(input("Ingrese su sexo. H/M")).lower()

if(((sexo == "h") and (nom[0] > "n")) or ((sexo == "m") and (nom[0] < "m"))):
    print("Es parte del equipo A")
else:
    print("Es parte del equipo B.")

#10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.
edad = int(input("Ingrese la edad del cliente. "))

if (edad < 4):
    print("Ingrese gratis.")
elif(edad > 3 and edad <19):
    print("Debe pagar $500.")
else:
    print("Debe pagar $1000.")

#11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
pizza = str(input("Desea una pizza vegetariana? S/N")).lower()

if(pizza == "s"):
    print("Elija un ingrediente de la lista.")
    print("1. Pimiento.")
    print("2. Tofu.")
    ing = int(input("Seleccione el numero del ingrediente deseado. "))
    if(ing == 1):
        print(f"La pizza seleccionada es vegetariana con pimiento.")
    else:
        print(f"La pizza seleccionada es vegetariana con tofu.")
else:
    print("Elija un ingrediente de la lista.")
    print("1. Peperoni.")
    print("2. Jamon.")
    print("3. Salmon.")
    ing = int(input("Seleccione el numero del ingrediente deseado. "))
    if(ing == 1):
        print(f"La pizza seleccionada no es vegetariana y tiene peperoni.")
    elif(ing == 2):
        print(f"La pizza seleccionada no es vegetariana y tiene jamon.")
    else:
        print(f"La pizza seleccionada no es vegetariana y tiene salmon.")

#12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
deseo = int(input("Ingrese una año deseado. "))
anio = int(input("Ingrese el año actual. "))

if(deseo>anio):
    tot = deseo-anio
    print(f"Faltan {tot} años para el año ingresado.")
else:
    tot = anio-deseo
    print(f"Pasaron {tot} años desde el año ingresado.")

#13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.
num1 = int(input("Ingrese un numero. "))
num2 = int(input("Ingrese otro numero. "))

if(num1 <= 1 and num2 <= 1):
    print("Uno de los numeros ingresados es invalido.")
elif(num1 > num2):
    if(num1 % num2 == 0):
        print("El mayor es multiplo del menor.")
else:
    if(num2 % num1 == 0):
        print("El mayor es multiplo del menor.")

#14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
#x = -b / a
a=int(input("Ingrese el primer coeficiente. "))
b = int(input("Ingrese el segundo coeficiente. "))

if(a==0):
    if(b==0):
        print("Solucion infinita.")
    else:
        print("Solucion nula.")
else:
    x = -b/a
    print(f"La solucion es: {x}")

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
forma = str(input("Desea calcular el area de un triangulo o de un circulo? T/C")).lower()

if(forma=="t"):
    b=int(input("Ingrese la base. "))
    h = int(input("Ingrese la altura. "))

    tot=(b*h)/2

    print(f"El area del triangulo es: {tot}")
elif(forma == "c"):
    r=int(input("Ingrese el radio. "))

    tot = (r**2)*math.pi

    print(f"El area del circulo es: {tot}")

#16-	Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#•	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b
numero1=int(input("Ingrese un numero. "))
numero2 = int(input("Ingrese otro numero. "))

print("1. Suma")
print("2. Multiplicacion")
print("3. Resta")
print("4. Divicion")
op = int(input("Ingrese el numero de la operacion que desea hacer."))

if(op==1):
    suma = (numero1 + numero2)
    print(f"{suma}")
elif(op==2):
    multi = (numero1 * numero2)
    print(f"{multi}")
elif(op==3):
    rest = (numero1 - numero2)
    print(f"{rest}")
elif(op==4):
    divi = (numero1 / numero2)
    print(f"{divi}")

#17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia = str(input("Ingrese un dia de la semana")).lower()

if(dia == "lunes"):
    print("Feliz lunes.")
if(dia == "viernes"):
    print("Feliz viernes.")
if(dia == "sabado" or dia == "domingo"):
    print("Buen finde.")
else:
    print("Mitad de semana. Sobrevivi.")

#18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
horas = float(input("Cuantas horas trabajaste?"))
sal = float(input("Cuanto es su salario por hora?"))

if(horas > 48):
    hs_extra=horas-48
    print(f"Trabajo {hs_extra} horas extra.")
    tot=sal*48+sal+((sal*0.10)*hs_extra)
    print(f"Este mes cobro {tot} de salario.")

#19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
lapiz = int(input("Cuantas lapices se va a llevar?"))

if(lapiz>= 1000):
    tot=60*lapiz-((60*0.07)*lapiz)
    print(f"El total es de ${tot}")
else:
    print(f"El total es de ${lapiz*60}")

#20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
num1 = float(input("Ingrese la nota 1: "))
num2 = float(input("Ingrese la nota 2: "))
num3 = float(input("Ingrese la nota 3: "))
num4 = float(input("Ingrese la nota 4: "))

prom = (num1 + num2 + num3 + num4)/4

if (prom > 6):
    print("Esta aprobado.")
else:
    print("Desaprobo.")
