from conexionBD import *
import funciones
import datetime

def crear (usuario_id,titulo,descripcion):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s,NOW())",
                       (usuario_id, titulo, descripcion))
        conexion.commit()
        return True
    except:
        return False    
    
def mostrar (usuario_id):
    try:
        cursor.execute("Select * from  notas where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    except:
        return False    

def cambiar(id, usuario_id):
    try:
        
        cursor.execute("SELECT * FROM notas WHERE id=%s and usuario_id=%s", (id,usuario_id))
        fila = cursor.fetchone()
        
        if fila:
            funciones.borrarPantalla()
            print("\n\t\U0001F501 Nota a modificar: \n")
            print(f"{'ID':<10}{'ID de usuario':<15}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
            print("-" * 80)
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print("-" * 80)
            
            seguro = input("¿Seguro que deseas modificar este registro? (si/no): ").lower().strip()
            if seguro == "si":
                titulo = input("\t Nuevo título: ")
                descripcion = input("\t Nueva descripción: ")
                cursor.execute(
                    "UPDATE notas SET titulo=%s, descripcion=%s, fecha=NOW() WHERE id=%s and usuario_id=%s",
                    (titulo, descripcion, id, usuario_id)
                )
                conexion.commit()
                return True
            else:
                print("No modifico nada")
                return False
        else:
            print("\u26A0 No existe esta nota. \u26A0")
            return False

    except Exception as e:
        print("\u26A0 Error al modificar:", e)
        return False
"""def cambiar (id, titulo, descripcion):
    try:
        cursor.execute("Select * from  notas where id=%s",(id,))
        registros=cursor.fetchone()
        if registros:
            print("\n\tTabla de notas: \U0001F4BE\n")
            print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print(f"-"*80)   
            seguro=input("Seguro de modificar este registro? ")
            if seguro=="si":
                cursor.execute("Update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s",(titulo,descripcion,id))
                conexion.commit()
                return True
            else:
                return False
        else:
            print("No existe esta nota")
            return False    
    except:
        return False
"""       
    
def borrar (id, usuario_id):
    try:
        cursor.execute("Select * from notas where id=%s and usuario_id=%s",(id, usuario_id))
        registros=cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\t\U0001F4DB Nota a eliminar: \n")
            print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print(f"-"*80)   
            seguro=input("Seguro de borrar este registro? (si/no) ").lower().strip()
            if seguro=="si":
                cursor.execute("delete from notas where id=%s and usuario_id=%s",(id, usuario_id))
                conexion.commit()
                return True
            else:    
                print("No borro nada")
                return False
        else:  
            print("\u26A0 No existe esta nota \u26A0")
            return False  
    except:
        print("\u26A0 Error al ingresar a base de datos \u26A0")
        return False    