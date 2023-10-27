# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
# from Person import Person;

# p1 = Person("Pepe", 18, 4654753)
# p2 = Person("Juan", 12, 1234567)
# p3 = Person("Lola", 24, 87654321)

# p1.show()
# p2.show()
# p3.show()

# print(f"La persona 1 es mayor: {p1.adult()}")
# print(f"La persona 2 es mayor: {p2.adult()}")
# print(f"La persona 3 es mayor: {p3.adult()}")

# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
# from Account import Account;

# while True:
#     name = input("Ingrese el nombre del titular. ")
#     if name == "":
#         print("No ingreso ningun titular, intente otra vez. ")
    
#     else:
#         num = int(input("Ingrese la cantidad de dinero en la cuenta. "))
#         a1 = Account(name, num)
#         money = int(input("Cuanto dinero va a agregar?"))
#         print(f"Hay {a1.deposit(money)} dinero en la cuenta.")

#         money2 = int(input("Cuanto dinero va a retirar?"))
#         print(f"Se retiro correctamente. Queda {a1.withdraw(money2)} dinero en la cuenta.")
#         break

# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
# from Triangle import Triangle;

# s1 = int(input(f"Ingrese el lado 1 😁")) 
# s2 = int(input(f"Ingrese el lado 2 😉")) 
# s3 = int(input(f"Ingrese el lado 3 🥲")) 

# t1 = Triangle(s1, s2, s3)
# print(f"El lado mas largo mide: {t1.max_side()}")
# t1.type_t()

# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda
# from Phonebook import Phonebook;
# p1 = Phonebook("Pepe", 123, "pepe@pepe")
# book = []

# while True:
#     op = int(input("Que desea hacer👀?: \n 1.Añadir contacto. \n 2.Listar contactos. \n 3.Buscar contacto. \n 4.Editar contacto. \n 5.Cerrar agenda.\n"))
#     if (op == 1):
#         book.append(p1.add())
#     elif (op == 2):
#         for i in book:
#             print(i)
#     elif (op == 3):
#         print(f"El contacto se encuentra en la posicion: {p1.serch(book)+1}")
#     elif (op == 4):
#         loc = p1.serch(book)
#         p1.edit(book, loc)
#     elif (op == 5):
#         print("Saliendo de la agenda... ")
#         break
#     else:
#         print("Esa opcion no esta en el menu. Intente otra vez...")
# print("Adios!")