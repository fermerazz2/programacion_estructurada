import agenda

def main():
    print("\t\t..::Sistema de gestion de agenda de contactos::..")
    agenda_contactos={}
    while True: 
        agenda.limpiar_pantalla()
        opcion=agenda.menu_principal()
        match opcion:
            case "1":
                agenda.limpiar_pantalla()
                agenda.agregar_contacto(agenda_contactos)
            case "2":
                agenda.limpiar_pantalla()
                agenda.mostrar_contactos(agenda_contactos)
            case "3":
                agenda.limpiar_pantalla()
                agenda.buscar_contacto(agenda_contactos)
            case "4":
                agenda.limpiar_pantalla()
                agenda.eliminar_contacto(agenda_contactos)
            case "5":
                agenda.limpiar_pantalla()
                agenda.modificar_contacto(agenda_contactos)    
            case "6":
                agenda.limpiar_pantalla()
                print("\n\t\tSaliendo del programa...") 
                break 
            case _:
                input("\n\t\tOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
