import funciones
import conexionBD
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t\U0001F464 ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t{nombre} {apellidos} se registro correctamente, con el email {email}")
            else:
                print("No fue posible ingresar el registro")    
                print("Por favro intente de nuevo")

              
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t\U0001F464 Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\tE-mail o contraseña incorrectas")
                print("\n\tIntentelo de nuevo")    
            funciones.esperarTecla()    
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"Se creo la nota {titulo} de manera correcta")
            else:
                print("No fue posible crear la nota")    
            #Agregar codigo
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
                
            if len(lista_notas)>0:
                print("\n\tTabla de notas: \U0001F4BE\n")
                print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"-"*80)
            else:
                print("No se pudo mostrar la tabla de notas")

            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            #Agregar codigo
            lista_notas=nota.mostrar(usuario_id)
                
            if len(lista_notas)>0:
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                print("\n\tTabla de notas: \U0001F4BE\n")
                print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"-"*80)
                id = input("\t \t ID de la nota a actualizar: ")
                respuesta=nota.cambiar(id,usuario_id)
                if respuesta:
                    print(f"Se modifico la nota {id} de manera correcta") 
            else:
                print("No hay notas para modificar")
              
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            
            if len(lista_notas)>0:
                print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                print("\n\tTabla de notas: \U0001F4BE\n")
                print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"-"*80)
                id = input("\t \t ID de la nota a eliminar: ")
                borrar=nota.borrar(id, usuario_id)
                if borrar:
                    print(f"Se borro la nota {id}")     
            else:
                print("No hay notas para eliminar")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    

