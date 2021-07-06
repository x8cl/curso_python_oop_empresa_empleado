from empleado import Empleado
from empresa import Empresa

empresa1 = Empresa("X8 Tecnologia SPA")

empleado1 = Empleado("111-1", "Juan", "Perez", 180)
empleado2 = Empleado("222-2", "Juanita", "Perez", 200, 12000)
empleado3 = Empleado("333-3", "Ed", "Valencia", 80)
empleado4 = Empleado("444-4", "Juaco", "Perez", 190, 7000)
empleado5 = Empleado("555-5", "Marcos", "Rodriguez", 300, 5000)
empleado6 = Empleado("666-6", "Marco", "Rodriguez", 10, 25000)
empleado7 = Empleado("777-7", "marcelo", "Rodriguez", 100)

""" #print(empleado1.info_empleado())
#print(empleado2.info_empleado())
#print(empleado3.info_empleado())
#print(empleado4.info_empleado())

#print(empresa1.info_empresa())

print(empresa1.contratar_empleado(empleado1))
print(empresa1.contratar_empleado(empleado1))
print(empresa1.contratar_empleado(empleado2))
print(empresa1.contratar_empleado(empleado3))
print(empresa1.contratar_empleado(empleado5))
print(empresa1.contratar_empleado(empleado1))
print(empresa1.contratar_empleado(empleado4))
print(empresa1.contratar_empleado(empleado6))
print(empresa1.contratar_empleado(empleado7))

for i in empresa1.empleados:
    print(i.info_empleado())

#print(f"Total de Horas Extra: {empresa1.obtener_total_hrs_extra()}")

#print(f"Total de Sueldos: ${empresa1.obtener_total_sueldos()}") """

#Agrego algunos empleados de ejemplo
empresa1.contratar_empleado(empleado1)
empresa1.contratar_empleado(empleado2)
empresa1.contratar_empleado(empleado3)
empresa1.contratar_empleado(empleado4)
empresa1.contratar_empleado(empleado5)
empresa1.contratar_empleado(empleado6)
empresa1.contratar_empleado(empleado7)


import os
def menu():    
    opcion = -1
    menu = ("-")*50 + "\n"
    menu += "Opciones:\n"
    menu += ("-")*50 + "\n"
    menu += "[1] Contratar Empleado\n"
    menu += "[2] Despedir Empleado\n"
    menu += "[3] Informacion Empleados\n"
    menu += "[4] Mostrar total de Sueldos pagados\n"
    menu += "[5] Mostrar total Horas Extra pagadas\n"
    menu += "[0] Salir\n"
    menu += ("-")*50 + "\n"

    while opcion < 0 or opcion > 5:
        os.system("cls")
        print(menu)
        try:
            opcion = int(input("Ingrese una opcion: "))
        except:
            input("El valor ingresado no parece ser un numero, presione ENTER para continuar...")
        if opcion < 0 or opcion > 5:
            input("Opcion ingrsada no valida, presione ENTER para continuar...")
    return opcion


opcion = menu()
while opcion > 0:
    if opcion == 1:
        print("Ingrese informacion del nuevo Empleado")
        rut = input("RUT: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        hTrabajadas = input("Horas trabajadas: ")
        vHora = input("Valor Hora: ")
        empleado = Empleado(rut, nombre, apellido, hTrabajadas, vHora)
        if empresa1.contratar_empleado(empleado) == True:
            print("Empleado contratado satisfactoriamente")
        else:
            print("El RUT ingresado ya existe")
    
    elif opcion == 2:
        rut = input("Ingrese RUT: ")
        if empresa1.despedir_empleado(rut) == True:
            print("Empleado eliminado")
        else:
            print("El RUT ingresado no existe")

    elif opcion == 3:
        for i in empresa1.empleados:
            print(i.info_empleado())
    
    elif opcion == 4:
        print(f"El total de Sueldos es: ${empresa1.obtener_total_sueldos()}")

    elif opcion == 5:
        print(f"El total de Horas Extra es: {empresa1.obtener_total_hrs_extra()}")

    input("Presione ENTER para continuar")
    opcion = menu()

else:
    print("Hasta pronto!")
