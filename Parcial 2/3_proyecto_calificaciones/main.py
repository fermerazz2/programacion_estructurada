#Proyecto 3
#Crear un proyecto que permita gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante

#NOTAS:
#1-.Utilizar funciones y maandar llamar desde otro archivo (modulos)
#2-.Utilizar una lista bidimensional para almacenar el nombre del estudiante y sus tres calificaciones.

import calificaciones

def main():
    opcion = True
    datos = []
    while opcion:
        calificaciones.borrar_pantalla()
        opcion = calificaciones.menu_principal()
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperar_tecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperar_tecla()
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperar_tecla()
            case "4":
                calificaciones.buscar_alumno(datos)
                calificaciones.esperar_tecla()
            case "5":
                opcion = False
                calificaciones.borrar_pantalla()
                print("\n\t 👋 Terminaste la ejecucion del SW")
            case _:
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")
                calificaciones.esperar_tecla()

if __name__ == "__main__":
    main()