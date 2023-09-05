#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

perimetro = base*2 + altura*2
area = base * altura

print(f"El perimetro es: {perimetro}, y el area es: {area}.")

#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1 = float(input("Ingrese el cateto a del triangulo rectangulo: "))
cateto2 = float(input("Ingrese el cateto b del triangulo rectangulo: "))

hipotenusa = (cateto1**2 + cateto2**2)**(1/2)

print(f"La hipotenusa es: {hipotenusa}.")

#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
numero1 = float(input("Ingrese el numero a: "))
numero2 = float(input("Ingrese el numero b: "))

suma = (numero1 + numero2)
rest = (numero1 - numero2)
multi = (numero1 * numero2)
divi = (numero1 / numero2)

print(f"suma: {suma}, resta: {rest}, multi: {multi}, divi: {divi}")

#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
fahr = float(input("Ingrese la cantidad de grados Fahrenheit: "))

cel = (fahr-32)*5/9

print(f"Celsius: {cel}")

#5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”) Le falta valor a la variable nombre.
nombre = "Mercedes"
input(nombre + ", Cual es tu cancion favorita?")

#b)	precio = input(“Precio: “) Falta poner el tipo del input y las comillas estan mal.
#total = precio + (precio * 0.1)
precio = float(input("Precio: ")) 
total = precio + (precio * 0.1)

#c)	edad = int(input(“Edad: “)) Las comillas estan mal
#print(tu edad es, edad) Faltan la f, las comillas y los corchetes.
edad = int(input("Edad: "))
print(f"tu edad es, {edad}")

#d)	edad = int(input(“Edad: “)) Las comillas estan mal
#print(“Veamos si tu edad es 18…”, edad=18) Las comillas estan mal, falta la f y los corchetes y el = no compara la edad.
edad = int(input("Edad: "))
print(f"Veamos si tu edad es 18…, {edad==18}")

#6.	Calcular la media de tres números pedidos por teclado.
numero1 = float(input("Ingrese el numero a: "))
numero2 = float(input("Ingrese el numero b: "))
numero3 = float(input("Ingrese el numero c: "))

prom = (numero1 + numero2 + numero3)/3

print(f"La media de los 3 numeros es: {prom}")

#7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
mins = int(input("Ingrese la cantidad de minutos: "))

hora = int(mins/60)
mins2 = (mins % 60)

print(f"Esa cantidad de minutos corresponde a {hora} horas y {mins2} minutos")

#8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
base = float(input("Ingrese su sueldo base: "))
prod1 = float(input("Ingrese el precio del primer producto: "))
prod2 = float(input("Ingrese el precio del segundo producto: "))
prod3 = float(input("Ingrese el precio del tercer producto: "))

extra = (prod1+prod2+prod3)* 0.10
total = (base + extra)

print(f"El total que recibira es: {total}")

#9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
prod = float(input("Ingrese el precio del producto: "))

dto = prod * 0.15
total= prod - dto

print(f"El precio final es: {total}")

#10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.
par1 = float(input("Ingrese la nota del primer parcial: "))
par2 = float(input("Ingrese la nota del segundo parcial: "))
par3 = float(input("Ingrese la nota del tercer parcial: "))
ex = float(input("Ingrese la nota del examen final: "))
trabajo = float(input("Ingrese la nota del trabajo final: "))

parciales = ((par1+par2+par3)/3)*0.55
examen = ex * 0.30
tp = trabajo*0.15
total = parciales+examen+tp

print(f"La nota final es: {total}")

#11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
numero1 = float(input("Ingrese el numero a: "))
numero2 = float(input("Ingrese el numero b: "))

dist = abs((numero2-numero1))

print(f"La distancia entre los dos numeros es: {dist}")

#12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
num = float(input("Ingrese un numero: "))

cuad = num **(1/2)
cub = num ** (1/3)

print(f"La raiz cuadrada del numero es: {cuad}, y la cubica es: {cub}.")

#13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
num = str(input("Ingrese un numero de dos cifras: "))

print(f"El numero invertido es: {num[1]}{num[0]}")

#14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
numero1 = float(input("Ingrese el numero A: "))
numero2 = float(input("Ingrese el numero B: "))

numero1, numero2 = numero2, numero1

print(f"El nuevo valor de ambas variables es: variabe A: {numero1}, variable B: {numero2}")

#15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
print("Ingrese la hora, minuto y segundo de salida: ")

hora = int(input("Hora: "))
min = int(input("Minuto: "))
seg = int(input("Segundo: "))

llegada = int(input("Ingrese cuantos segundos tardo en llegar al destino. "))

llegada_hs = int(llegada / 3600)
llegada_mins = int((llegada % 3600) / 60)
llegada_seg = llegada % 60

hs = hora + llegada_hs
mins = min + llegada_mins
segs = seg + llegada_seg

if segs >= 60:
    mins += segs // 60
    segs %= 60

if mins >= 60:
    hs += mins // 60
    mins %= 60

hs %= 24

print(f"La hora de llegada fue a las {hs}:{mins}:{segs}")

#16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = str(input("Ingrese su nombre: "))
ap1 = str(input("Ingrese su primer apellido: "))
ap2 = str(input("Ingrese su segundo apellido: "))

ini_nom = nombre[0].upper()
ini_ap1 = ap1[0].upper()
ini_ap2 = ap2[0].upper()

print(f"{ini_nom}.{ini_ap1}.{ini_ap2}")

#17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario = str(input("Ingrese su nombre: "))

print(f"Ahora estas en la Matrix {usuario}")

#18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.
cena = float(input("Ingrese el precio de la cena: "))

servicio = cena * 0.062
propina = cena * 0.1
total = cena + servicio + propina

print(f"El monto total es de: {total}")

#19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.
print("Ingrese el dia, mes y año de su nacimiento: ")

dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

print(f"Su naciomiento fue el: {dia}/{mes}/{anio}")

#20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
nac = (input("Ingrese el dia, mes y año de su nacimiento: (sin espacios ni puntos)"))

dia = int(nac[:2])
mes = int(nac[2:4])
anio = int(nac[4:])

print(f"Su naciomiento fue el: {dia}/{mes}/{anio}")

#21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.
km = float(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
tanque = int(input("Ingrese qué capacidad (en litros) tiene el tanque: "))
recorrido = int(input("Ingrese cuantos kilometros va a recorrer: "))

km_total = km*tanque
inicio = 1

while recorrido > km_total:
    km_total += km
    inicio += 1

print(f"La cantidad de tanques necesarios va a ser de: {inicio}")
