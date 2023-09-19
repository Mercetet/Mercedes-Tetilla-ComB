import funciones;

x = int(input("Un numero: "))
y = int(input("Otro numero: ")) 
print(f"{funciones.most(x-3, funciones.least(x+2, y-5))}") 