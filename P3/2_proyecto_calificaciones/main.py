''' 
Proyecto 3

Crear un proyecto que permita gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar,
mostrar, calcular promedio de un estudiante.
Notas: 
1.-Utilizar funciones y mandarlas llamar desde otro archivo (modulos)
2.-Utilizar list (bidimensional) para almacenar el nombre del alumno a si mismo como sus tres calificaciones

'''
import calificaciones


def main():
    datos = []
    opcion = True
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
                calificaciones.Buscar(datos)
                calificaciones.esperarTecla()       
            case "5":
                calificaciones.borrar(datos)
                calificaciones.esperarTecla()
            case "6":
                calificaciones.modificar(datos)
                calificaciones.esperarTecla()   
            case "7":
                calificaciones.limpiarPantalla()
                print("\t\t\U0001F6AA Saldra \U0001F6AA")
                print("\t\t\U0001F389 Termino la ejecucion del SW \U0001F389")
                calificaciones.esperarTecla()
                opcion = False
            case _:
                input("\u26A0 Opcion no valida, oprima cualquier tecla para continuar \U0001F449  ")

if __name__ == "__main__":
    main()                