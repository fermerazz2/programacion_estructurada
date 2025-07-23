import os
import mysql.connector
from mysql.connector import Error

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_agenda"
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def menu_principal():
        print("\t\t\n  1️⃣  Agregar contacto \t\t\n  2️⃣  Mostrar todos los contactos \t\t\n  3️⃣ Bucar contacto por nombre\t\t\n  4\ufe0f\u20e3. Eliminar contacto \t\t\n  5\ufe0f\u20e3. Modificar contacto \t\t\n  6\ufe0f\u20e3. Salir")
        opcion=input("\n\t\tIngrese una opción: (1-4):  ")
        return opcion.strip()

      
def limpiar_pantalla():
    import os
    os.system("cls")

def espere_tecla():
    input("\n\t\tPresione Enter para continuar...")       

def agregar_contacto(agenda):
    conexionBD=conectar()
    print("\n\t\t..::Agregar contacto::.. \U0001F4DD")
    nombre= input("\n\t\t\U0001F4DD Ingrese el nombre del contacto: ").upper().strip()
    cursor=conexionBD.cursor()
    agenda=cursor.execute("select nombre from agenda")
    nombres_en_bd = [fila[0] for fila in cursor.fetchall()]
    if nombre in nombres_en_bd:
        print("\n\t\tEl contacto ya existe.")
        espere_tecla()
    else:
        telefono = input("\n\t\t\U0001F4DD Ingrese el número de teléfono: ").strip()
        email = input("\n\t\t\U0001F4DD Ingrese el correo electrónico: ").lower().strip()
        #Agregar el atributo nombre al diccionario con los valores de tel y email en una lista
        try:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO agenda (nombre, telefono, email) VALUES (%s, %s, %s)",
                (nombre, telefono, email)
            )
            conexionBD.commit()
            input("\n\t\t\U0001F389 Contacto agregado correctamente en la base de datos. Presione Enter para continuar... \U0001F389")
        except Error as e:
            print("❌ Error al insertar en la base de datos:", e)

def mostrar_contactos(agenda):
    conexionBD= conectar()
    print("\n\t\tMostrar todos los contactos")
    cursor=conexionBD.cursor()
    cursor.execute(
            "select * from agenda"
    )
    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de contactos: \U0001F4BE\n")
        print(f"{"ID":<10}{"Nombre":<15}{"Telefono":<15}{"Email":<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)    
        espere_tecla()
    else:
        input("\t .:: ⚠ No hay registros en el sistema ⚠::.")        

def buscar_contacto(agenda):
    conexionBD= conectar()
    print("\n\t\t🔍 Buscar contacto por nombre 🔍")
    cursor=conexionBD.cursor()
    buscar=input("\t\U0001F4DDIngresa el nombre de la persona a buscar: ")
    cursor.execute(
        "select * from agenda where nombre=%s",(buscar,)
    )
    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de contactos: \U0001F4BE\n")
        print(f"{"ID":<10}{"Nombre":<15}{"Telefono":<15}{"Email":<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)    
    else:
        print("\t .:: ⚠ No esta esta persona en el sistema ⚠::.")   
    espere_tecla()    
            

def eliminar_contacto(agenda):
    conexionBD= conectar()
    print("\n\t\t🔍 Buscar contacto por nombre 🔍")
    cursor=conexionBD.cursor()
    buscar=input("\t\U0001F4DDIngresa el nombre de la persona a buscar: ")
    cursor.execute(
        "select * from agenda where nombre=%s",(buscar,)
    )
    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de contactos: \U0001F4BE\n")
        print(f"{"ID":<10}{"Nombre":<15}{"Telefono":<15}{"Email":<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)
        decision=input("Seguro de borrar este registro? (si/no)").lower().strip()    
        if decision == "si":
            cursor.execute(
            "delete from agenda where nombre=%s",(buscar,)
            )
            conexionBD.commit()
            print("\tContacto borrado correctamente")    
        else:
            print("\tNo borro nada")
    else:
        print("\t .:: ⚠ No esta esta persona en el sistema ⚠::.")   
    espere_tecla()    
            

def modificar_contacto(agenda):
    conexionBD= conectar()
    print("\n\t\tModificar contacto \U0001F4BE")
    cursor=conexionBD.cursor()
    buscar=input("\t\U0001F4DDIngresa el nombre de la persona a buscar: ")
    cursor.execute(
        "select * from agenda where nombre=%s",(buscar,)
    )
    registros=cursor.fetchall()
    if registros:
        print("\n\tTabla de contactos: \U0001F4BE\n")
        print(f"{"ID":<10}{"Nombre":<15}{"Telefono":<15}{"Email":<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)
        decision=input("Seguro de modificar este registro? (si/no)").lower().strip()    
        if decision == "si":
            nombre= input("\n\t\t\U0001F4DD Ingrese el nombre del contacto: ").upper().strip()
            cursor.execute("select nombre from agenda")
            nombres_en_bd = [fila[0] for fila in cursor.fetchall()]
            if nombre in nombres_en_bd:
                print("\n\t\tEl contacto ya existe.")
                espere_tecla()
            else:
                telefono = input("\n\t\t\U0001F4DD Ingrese el número de teléfono: ").strip()
                email = input("\n\t\t\U0001F4DD Ingrese el correo electrónico: ").lower().strip()
                try:
                    cursor = conexionBD.cursor()
                    cursor.execute(
                        "update agenda set nombre=%s, telefono=%s, email=%s where nombre=%s",
                        (nombre, telefono, email, buscar)
                    )
                    conexionBD.commit()
                    input("\n\t\t\U0001F389 Contacto agregado correctamente en la base de datos. Presione Enter para continuar... \U0001F389")
                except Error as e:
                    print("❌ Error al insertar en la base de datos:", e)
                    espere_tecla()
        else:
            input("No modifico nada")            
    else:
        print("\n\t\tEl contacto no existe. \u26A0")
        espere_tecla()


