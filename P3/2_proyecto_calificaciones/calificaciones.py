import mysql.connector
from mysql.connector import Error
def limpiarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t\u270BPresione una tecla para continuar\u270B  ")    

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_calificaciones"
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None
  
def AgregarCalificaciones(lista):
    conexionBD=conectar()
    limpiarPantalla()
    print("\n\t\t\t\U0001F4BE ..::Agregar Calificaciones::.. \U0001F4BE\n")
    nombre = input("\U0001F4DD Nombre del alumno:  ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                if cal>=0 and cal<10.1:
                    calificaciones.append(cal)
                    continua=False
                else:
                    input("\u26A0 Ingresa un numero valido \u26A0  ")    
            except ValueError:
                input("\u26A0 Ingrese un valor numerico \u26A0  ")
    lista.append([nombre]+calificaciones)
    promedio=(calificaciones[0]+calificaciones[1]+calificaciones[2])/3
    try:
        cursor = conexionBD.cursor()
        cursor.execute("INSERT INTO calificaciones (id, nombre, cali_1, cali_2, cali_3, promedio) VALUES (NULL, %s, %s, %s, %s, %s)"
        , (nombre, calificaciones[0], calificaciones[1], calificaciones[2], promedio))
        conexionBD.commit()
        print("\t\t.:: ✅ Operacion realizada con exito ✅ ::.")
    except Error as e:
        print("Error al intentar guardar registro en Base de Datos")
    input("\U0001F389 Accion realizada con exito \U0001F389")                     
   

def ConsultarCalificaciones(lista):
    conexionBD=conectar()
    limpiarPantalla()
    cursor=conexionBD.cursor()
    cursor.execute(
        "select nombre, cali_1, cali_2, cali_3 from calificaciones"
    )
    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de calificaciones: \U0001F4BE\n")
        print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"-"*40)
        for fila in registros:
            print(f"\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"-"*40)    
        cuantos=len(registros)
        print(f"\n\tSon: {cuantos} alumnos\U0001F4C2")
    else:
        print("\t .:: ⚠ No hay calificaciones en el sistema ⚠::.")



def CalcularPromedio(lista):
    conexionBD=conectar()
    limpiarPantalla()
    print("\t\t..::Promedio::..")
    cursor=conexionBD.cursor()
    cursor.execute(
        "select * from calificaciones"
    )

    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de calificaciones: \U0001F4BE\n")
        print(f"\n\t{'Nombre':<15}{'Promedio':<10}")
        print(f"-"*40)
        for fila in registros:
            print(f"\t{fila[1]:<15}{fila[5]:<10}")
        print(f"-"*40)    
    else:
        print("\t .:: ⚠ No hay calificaciones en el sistema ⚠::.")   
          

def CalcularPromedio2(lista):
    print("\t\t\U0001F552 PROMEDIOS \U0001F552")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<15}{'Promedio':<10}")
        print(f"\t {'-'*30}")
        promedioTot=0
        promedio=0
        suma=0
        i=1
        for fila in lista:
            print(f"\t{fila[0]:<15}{promedio:<10.2f}")
            while i < 4:
                suma += fila[i]
                i += 1
            promedio = suma / 3
            promedioTot += promedio
            print(f"\t{fila[0]:<15}{promedio:<10.2}")   
        promedioTot= promedioTot/(len(lista))
        print(f"\t {'-'*30}")
        print(f"\n\t\U0001F389 El promedio de los alumnos es: {promedioTot:.2f} \U0001F389")
        print(f"\t {'-'*30}")
    else:
        print("\n\t\u26A0 No hay calificaciones en el sistema \u26A0")    
              
def menuPrincipal():
    print(f"\n\t\t\t\U0001F4DD..::Sistema de Gestion De Calificaciones::..\U0001F4DD \n\t\t1\ufe0f\u20e3  Agregar calificaciones\n\t\t2\ufe0f\u20e3  Consultar calificaciones"
                 "\n\t\t3\ufe0f\u20e3  Calcular promedio\n\t\t4\ufe0f\u20e3  Buscar\n\t\t5\ufe0f\u20e3  Borrar\n\t\t6\ufe0f\u20e3  Modificar\n\t\t7\ufe0f\u20e3  Salir\n")
    opcion=input("\n\t\t\U0001F449  Selecciona una opcion: (1-5): ")
    return opcion

def Buscar(datos):
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t.:: 🔍 Mostrar calificacion alumno 🔍 ::.\n ")
        cursor=conexionBD.cursor()
        buscar=input("\t\U0001F4DDIngresa el nombre del alumno a buscar: ")
        cursor.execute(
            "select * from calificaciones where nombre=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print(f"\n\t Alumno: {buscar}\U0001F4BE\n")
            print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}{"Promedio":<10}")
            print(f"-"*50)
            for fila in registros:
                print(f"{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*50)    
        else:
            print("\t .:: ⚠ No esta este alumno en el sistema ⚠::.")

def borrar(datos):
    conexionBD=conectar()
    if conexionBD!=None:
        limpiarPantalla()
        print("\n\t\t.:: \U0001F4DB Borrar alumnos \U0001F4DB ::.\n ")
        cursor=conexionBD.cursor()
        buscar=input("\t\U0001F4DDIngresa el nombre del alumno a buscar: ")
        cursor.execute(
            "Select * from calificaciones where nombre=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print("\n\t: \U0001F4BE\n")
            print(f"\n\t Alumno: {buscar}\U0001F4BE\n")
            print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}{"Promedio":<10}")
            print(f"-"*50)
            for fila in registros:
                print(f"{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*50)    
            borrar=input("DESEA BORRAR ESTA Alumno? (si/no) ").lower()
            if borrar=="si":
                cursor.execute(
                "delete from calificaciones where nombre=%s",(buscar,)
                )
                conexionBD.commit()
                print("\tAlumno borrada correctamente \U0001F4DB")
            else:
                print("No borro nada")    
           
        else:
            print("\t .:: ⚠ No esta esa el alumno en el sistema ⚠::.")

def modificar(datos):
    conexionBD=conectar()
    if conexionBD!=None:
        limpiarPantalla()
        print("\n\t\t.:: 🔄 Modificar Alumnos 🔄 ::.\n ")
        cursor=conexionBD.cursor()
        buscar=input("\t\U0001F4DDIngresa el nombre del alumno a buscar: ")
        cursor.execute(
            "Select * from calificaciones where nombre=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print(f"\n\t Alumno: {buscar}\U0001F4BE\n")
            print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}{"Promedio":<10}")
            print(f"-"*50)
            for fila in registros:
                print(f"{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*50)    
            Modificar=input("DESEA Modificar ESTA Alumno? (si/no) ").lower()
            if Modificar=="si":
                nombre = input("\U0001F4DD Nombre del alumno:  ").upper().strip()
                calificaciones=[]
                for i in range(1,4):
                    continua=True
                    while continua:
                        try:
                            cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                            if cal>=0 and cal<10.1:
                                calificaciones.append(cal)
                                continua=False
                            else:
                                input("\u26A0 Ingresa un numero valido \u26A0  ")    
                        except ValueError:
                            input("\u26A0 Ingrese un valor numerico \u26A0  ")
                promedio=(calificaciones[0]+calificaciones[1]+calificaciones[2])/3
                try:
                    cursor = conexionBD.cursor()
                    cursor.execute("update calificaciones set  nombre=%s, cali_1=%s, cali_2=%s, cali_3=%s, promedio=%s where nombre=%s"
                    , (nombre, calificaciones[0], calificaciones[1], calificaciones[2], promedio, buscar))
                    conexionBD.commit()
                    print("\t\t.:: ✅ Operacion realizada con exito ✅ ::.")
                except Error as e:
                    print("Error al intentar guardar registro en Base de Datos")
                
            else:
                print("No modifico nada")    
           
        else:
            print("\t .:: ⚠ No esta este alumno en el sistema ⚠::.")            
'''
def main():
    datos=[]
    opcion=True
    while opcion:
        calificaciones.limpiarPantalla()
        opcion = calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.AgregarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                
                calificaciones.ConsultarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.CalcularPromedio(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.limpiarPantalla() 
                print("\t\tSaldra")
                print("\t\tTermino la ejecucion del SW")
                calificaciones.esperarTecla()
                
                opcion=False
            case _:
                print("\u26A0 Opcion no valida, oprima cualquier tecla para continuar")              
'''

