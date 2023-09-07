fecha = input("Ingrese la fecha de hoy(Dia, DD/MM)")

dia = fecha[0:fecha.find(",")].lower()
dd = int(fecha[fecha.find(" ")+1: fecha.find("/")])
mm = int(fecha[fecha.find("/")+1:])

print(f"{dia}, {dd}/{mm}")

if ((dia == "lunes" or dia == "martes" or dia == "miercoles")  and (mm < 12 and mm>1) and (dd>1 and dd<31 )):
    ex = input("Hoy tomaron examenes? s/n")
    ex = ex.lower()
    if(ex == "s"):
        ap = int(input("Cuantos alumnos aprobaron?"))
        des = int(input("Cuantos alumnos desaprobaron?"))
        sum = ap+des
        por = (ap / sum)*100
        print(f"El porsentaje de aprobados es: {por}")
elif ((dia == "jueves") and (mm < 12 and mm>1) and (dd>1 and dd<31 )):
    tot = int(input("Cual es el total de los alumnos?"))
    asi = int(input("Cuantos alumnos asistieron a clases?"))
    por = ((asi * 100)/tot)
    if (por > 50):
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")
elif ((dia == "viernes") and (mm < 12 and mm>1) and (dd>1 and dd<31 )):
    if((mm == 1 and dd == 1)or(mm==7 and dd==1)):
        print("Comienzo del nuevo ciclo")
        nuevo = int(input("Ingrese la cantidad de alumnos nuevos:"))
        ara = float(input("Ingrese el arancel por alumno"))
        tot = nuevo*ara
        print(f"Ingrso total: {tot}")
else:
    print("ERROR")
