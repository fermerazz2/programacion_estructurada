
def borrar_pantalla():
    import os
    os.system('clear')

def esperar_tecla():
    input("\n\t\t\tOprima una tecla para continuar")

def menu_principal():
    print( "\n\t\t\t 🎓..::: CALIFICACIONES :::...🎓 \n\t\t 📝..::: Sistema de Gestión de Calificaciones :::...📝\n\t\t 1.- \U0001F4DD Agregar \n\t\t 2.- \U0001F50D Mostrar Alumnos \n\t\t 3.- \U0001F50D Calcular promedio \n\t\t 4.- \U0001F50D Buscar Alumno \n\t\t 5.- \U0001F6AA Salir ")
    opcion = input("\t\t\t🥸 Elige una opción: 1-5 ").upper()
    return opcion

def agregar_calificaciones(lista):
    borrar_pantalla()
    print("\n\t\t\t Agregar caificaciones")
    nombre = input("\n\t\t\t Nombre del Alumno:  ".upper().strip())
    calificaciones = []
    for i in range(1, 4):
        continuar = True
        while continuar == True:
            try:
                cali = float(input(f"Calificacion: {i} "))
                if cali >= 0 and cali < 11:
                    calificaciones.append(cali)
                    continuar = False
                else:
                    print("\n\t\t\t ❌ Ingresa un numero valido")
            except ValueError:
                print("\n\t\t\t ❌ Ingresa un numero valido")
    lista.append([nombre, *calificaciones])
    print("✅ Accion realizada con exito")

def mostrar_calificaciones(datos):
    borrar_pantalla()
    print("\n\t\t\tMostrar calificaciones")
    if len(datos) > 0:
        califs = []
        for cali in datos:
            califs.append(f"El alumno {cali[0]}, tiene la siguientes calificaciones P1:{cali[1]}, P2:{cali[2]}, P3:{cali[3]}")
        
        alumnos = len(datos)
        print(f"\n\t\t\t 📝 Hay {alumnos} alumnos capturados")
        print("\n".join(califs))
    
    else:
        print("\n\t\t\t ❌No hay califiaciones registradas en el sistema")

def calcular_promedio(datos):
    borrar_pantalla()
    if len(datos) > 0:
        print(f"\n\t\t\t\t{'Alumno':<15}{'Promedio': <10}")
        promedios = []
        prom_grup = 0
        for alumno in datos:
            prom = (alumno[1] + alumno[2] + alumno[3])/3
            promedios.append(f"\n\t\t\t Nombre: {alumno[0]}, promedio: {prom}")
            prom_grup += prom
        print(f"\n\t\t\t{'-'*30}")
        print("\n".join(promedios))
        print(f"\n\t\t\t🎓El promedio grupal es de: {prom_grup/len(promedios)}")

def buscar_alumno(datos):
    borrar_pantalla()
    nombre = input("Escriba el nombre del alumno a buscar: ").strip().upper()
    
    coincidencias = []
    for alumno in datos:
        if nombre == alumno[0]:
            coincidencias.append(alumno)
    
    if coincidencias:
        for alumno in coincidencias:
            print(f"- {alumno[0]}, cal1: {alumno[1]} cal2: {alumno[2]} cal3: {alumno[3]}")
        print(f"\nSe encontraron {len(coincidencias)} alumno(s):")
    else:
        print(f"\nNo se encontraron alumnos con el nombre '{nombre}'")
    