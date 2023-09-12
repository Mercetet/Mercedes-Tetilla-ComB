import random
box1={1:"Objeto comun", 2:"Objeto comun", 3:"Objeto comun", 4:"Objeto comun", 5:"Objeto poco comun", 6:"Objeto poco comun",7:"Objeto raro"}
box2={1:"Objeto comun", 2:"Objeto comun",3:"Objeto raro", 4:"Objeto raro",5:"Objeto legendario"}
box3={1:"Objeto raro", 2:"Objeto raro",3:"Objeto legendario",4:"Objeto exotico"}
aux=["i","n","g"]
inventory=[]
objc=0
objp=0
objr=0
objl=0
obje=0
cash=0
print("Bienvenido a GoodCases! Elija su opcion.\n")
while True:
    option=int(input("1. Comprar cajas.\n2. Ver inventario.\n3. Depositar dinero.\n4. Salir. \n"))
    if option==1:
        print("Tenemos 3 cajas a la venta, con diferentes probabilidades de drop.")
        print(f"Su dinero actual es ${cash}")
        print("i: Inicial Box: %60 de probabilidades de un objeto comun. \n %30 de probabilidades de un objeto poco comun. \n %10 de probabilidades de un objeto raro. \n Valor:$50\n")
        print("n: Nice Box: %40 de probabilidades de un objeto comun. \n %40 de probabilidades de un objeto raro. \n %20 de probabilidaes de un objeto legendario. \n Valor:$100\n")
        print("g: Good Box: %50 de probabilidades de un objeto raro. \n %25 de probabilidades de un objeto legendario. \n %25 de probabilidades de un objeto exotico especial. \n Valor:$500\n")
        box=input("Ingrese su seleccion. i/n/g \n").lower()
        if box in aux:
            if box=="i":
                if cash>=50:
                    print("Compra confirmada. \n")
                    cash-=50
                    inventory.append(box1[random.randint(1,7)])
                    print(f"Le toco un: {inventory[-1]}")
                    print(" ")
                else:
                    print("Dinero insuficiente. \n")
            elif box=="n":
                if cash>=100:
                    print("Compra confirmada. \n")
                    cash-=100
                    inventory.append(box2[random.randint(1,5)])
                    print(f"Le toco un: {inventory[-1]}")
                    print(" ")
                else:
                    print("Dinero insuficiente. \n")
            elif box=="g":
                if cash>=500:
                    print("Compra confirmada. \n")
                    cash-=500
                    inventory.append(box3[random.randint(1,4)])
                    print(f"Le toco un: {inventory[-1]}")
                    print(" ")
                else:
                    print("Dinero insuficiente. \n")
            else:
                print("Opcion incorrecta \n")
    elif option==2:
        for i in inventory:
            if i=="Objeto comun":
                objc+=1
            if i=="Objeto poco comun":
                objp+=1
            if i=="Objeto raro":
                objr+=1
            if i=="Objeto legendario":
                objl+=1
            if i=="Objeto exotico":
                obje+=1
        print(f"Objetos comunes: {objc} \n Objetos poco comunes: {objp} \n Objetos raros: {objr} \n Objetos legendarios: {objl} \n Objetos exoticos: {obje}")
    elif option==3:
        while True:
            income=float(input("Ingrese el valor del deposito.\n"))
            if income>0:
                cash+=income
                print(f"Su dinero actual es de {cash}\n")
                break
            else:
                print("No se permiten ingresos negativos. \n")
    elif option==4:
        break
    else:
        print("Opcion incorrecta.")