from funciones.funciones import *
from funciones.menus import menu

def main():
    usuarios = ["ADMIN", "USER1", "USER2"]  # Lista inicial de usuarios
    carrito = []
    total = 0
    usuario_actual = ""
    
    print("\t\t\t..::☕ Bienvenido a cafetería ☕::..")
    
    while True:
        opcion = mostrar_menu_principal()
        borrar_pantalla()
        
        match opcion:
            case "1":
                usuario_actual = iniciar_sesion(usuarios)
                if usuario_actual:
                    carrito, total = menu_usuario(usuario_actual, carrito, total)
            case "2":
                usuarios = registrar_usuario(usuarios)
            case "3":
                print("\n\t\t\t..::☕ Salir ☕::..")
                print("\n\t\tGracias por visitar la cafería. ¡Hasta luego!")
                break
            case _:
                print("\n\t\t⚠ Opción no válida, por favor intente de nuevo. ⚠")
                esperar_tecla()

def mostrar_menu_principal():
    print("\t\t\n  1️⃣  Iniciar sesión \t\t\n  2️⃣  Registrarse \t\t\n  3️⃣  Salir")
    return input("\n\t\tIngrese una opción (1-3): ").strip()

def iniciar_sesion(usuarios):
    print("\n\t\t\t..::☕ Iniciar sesión ☕::..")
    usuario = input("\n\t\tIngrese su usuario: ").upper().strip()
    
    if usuario not in usuarios:
        print("\n\t\t⚠ Usuario no encontrado, por favor intente de nuevo. ⚠")
        esperar_tecla()
        return None
    else:
        print(f"\n\t\tBienvenido {usuario} a la cafería!")
        esperar_tecla()
        return usuario

def registrar_usuario(usuarios):
    print("\n\t\t\t..::☕ Registrarse ☕::..")
    usuario = input("\n\t\tIngrese su usuario: ").upper().strip()
    
    while usuario in usuarios:
        print("\n\t\t⚠ Usuario ya existe, por favor elija otro. ⚠")
        usuario = input("\n\t\tIngrese un nuevo usuario: ").upper().strip()
    
    usuarios.append(usuario)
    print(f"\n\t\tUsuario {usuario} registrado exitosamente!")
    esperar_tecla()
    return usuarios

def menu_usuario(usuario, carrito, total):
    while True:
        borrar_pantalla()
        print(f"\n\t\t\t..::☕ Bienvenido {usuario} ☕::..")
        print("\n\t\t\t..::☕ Selecciona una opción ☕::..")
        print("\t\t\n  1️⃣  Ver bebidas 🥤")
        print("  2️⃣  Ver comida 🥗")
        print("  3️⃣  Ver carrito 🛒")
        print("  4️⃣  Realizar pedido 💳")
        print("  5️⃣  Cerrar sesión 🚪")
        
        opcion = input("\n\t\tIngrese una opción (1-5): ").strip()
        
        match opcion:
            case "1":
                carrito, total = mostrar_bebidas(carrito, total)
            case "2":
                carrito, total = mostrar_comida(carrito, total)
            case "3":
                mostrar_carrito(carrito, total)
            case "4":
                carrito, total = realizar_pedido(carrito, total)
            case "5":
                print(f"\n\t\tHasta luego {usuario}!")
                esperar_tecla()
                break
            case _:
                print("\n\t\t⚠ Opción no válida, por favor intente de nuevo. ⚠")
                esperar_tecla()
    
    return carrito, total

def mostrar_bebidas(carrito, total):
    while True:
        borrar_pantalla()
        print("\n\t\t\t..::☕ Bebidas disponibles ☕::..")
        print("\t\t1️⃣ Café ☕")
        print("\t\t2️⃣ Té 🍵")
        print("\t\t3️⃣ Volver al menú principal")
        
        opcion = input("\n\t\tIngrese el número: ").strip()
        
        match opcion:
            case "1":
                carrito, total = seleccionar_cafe(carrito, total)
            case "2":
                carrito, total = seleccionar_te(carrito, total)
            case "3":
                break
            case _:
                print("\n\t\t⚠ Opción no válida, por favor intente de nuevo. ⚠")
                esperar_tecla()
    
    return carrito, total

def seleccionar_cafe(carrito, total):
    borrar_pantalla()
    print("\n\t\t\t..::☕ Tipos de Café ☕::..")
    
    cafes = menu["bebidas"]["Cafe"]
    for i, cafe in enumerate(cafes, 1):
        print(f"\t\t{i}️⃣ {cafe['nombre']}")
    print(f"\t\t{len(cafes)+1}️⃣ Volver")
    
    opcion = input("\n\t\tSeleccione su café: ").strip()
    
    try:
        opcion_num = int(opcion)
        if 1 <= opcion_num <= len(cafes):
            cafe_seleccionado = cafes[opcion_num - 1]
            return seleccionar_tamano_cafe(cafe_seleccionado, carrito, total)
        elif opcion_num == len(cafes) + 1:
            return carrito, total
        else:
            print("\n\t\t⚠ Opción no válida ⚠")
            esperar_tecla()
    except ValueError:
        print("\n\t\t⚠ Por favor ingrese un número válido ⚠")
        esperar_tecla()
    
    return carrito, total

def seleccionar_tamano_cafe(cafe, carrito, total):
    borrar_pantalla()
    print(f"\n\t\t\t..::☕ {cafe['nombre']} ☕::..")
    print("\t\t1️⃣ Chico 🥤 - $" + str(cafe['size']['Chico']))
    print("\t\t2️⃣ Grande 🥤 - $" + str(cafe['size']['Grande']))
    print("\t\t3️⃣ Volver")
    
    opcion = input("\n\t\tSeleccione el tamaño: ").strip()
    
    match opcion:
        case "1":
            item = f"{cafe['nombre']} (Chico)"
            precio = cafe['size']['Chico']
            carrito.append({"item": item, "precio": precio})
            total += precio
            print(f"\n\t\t✅ {item} agregado al carrito - ${precio}")
        case "2":
            item = f"{cafe['nombre']} (Grande)"
            precio = cafe['size']['Grande']
            carrito.append({"item": item, "precio": precio})
            total += precio
            print(f"\n\t\t✅ {item} agregado al carrito - ${precio}")
        case "3":
            return carrito, total
        case _:
            print("\n\t\t⚠ Opción no válida ⚠")
    
    esperar_tecla()
    return carrito, total

def seleccionar_te(carrito, total):
    borrar_pantalla()
    print("\n\t\t\t..::🍵 Tipos de Té 🍵::..")
    
    tes = menu["bebidas"]["te"]
    for i, te in enumerate(tes, 1):
        print(f"\t\t{i}️⃣ {te['nombre']} - ${te['precio']}")
    print(f"\t\t{len(tes)+1}️⃣ Volver")
    
    opcion = input("\n\t\tSeleccione su té: ").strip()
    
    try:
        opcion_num = int(opcion)
        if 1 <= opcion_num <= len(tes):
            te_seleccionado = tes[opcion_num - 1]
            carrito.append({"item": te_seleccionado['nombre'], "precio": te_seleccionado['precio']})
            total += te_seleccionado['precio']
            print(f"\n\t\t✅ {te_seleccionado['nombre']} agregado al carrito - ${te_seleccionado['precio']}")
            esperar_tecla()
        elif opcion_num == len(tes) + 1:
            return carrito, total
        else:
            print("\n\t\t⚠ Opción no válida ⚠")
            esperar_tecla()
    except ValueError:
        print("\n\t\t⚠ Por favor ingrese un número válido ⚠")
        esperar_tecla()
    
    return carrito, total

def mostrar_comida(carrito, total):
    while True:
        borrar_pantalla()
        print("\n\t\t\t..::🍽️ Comida disponible 🍽️::..")
        print("\t\t1️⃣ Sándwiches 🥪")
        print("\t\t2️⃣ Postres 🍰")
        print("\t\t3️⃣ Volver al menú principal")
        
        opcion = input("\n\t\tIngrese el número: ").strip()
        
        match opcion:
            case "1":
                carrito, total = seleccionar_sandwich(carrito, total)
            case "2":
                carrito, total = seleccionar_postre(carrito, total)
            case "3":
                break
            case _:
                print("\n\t\t⚠ Opción no válida, por favor intente de nuevo. ⚠")
                esperar_tecla()
    
    return carrito, total

def seleccionar_sandwich(carrito, total):
    borrar_pantalla()
    print("\n\t\t\t..::🥪 Sándwiches 🥪::..")
    
    sandwiches = menu["comida"]["sandwiches"]
    for i, sandwich in enumerate(sandwiches, 1):
        print(f"\t\t{i}️⃣ {sandwich['nombre']} - ${sandwich['precio']}")
    print(f"\t\t{len(sandwiches)+1}️⃣ Volver")
    
    opcion = input("\n\t\tSeleccione su sándwich: ").strip()
    
    try:
        opcion_num = int(opcion)
        if 1 <= opcion_num <= len(sandwiches):
            sandwich_seleccionado = sandwiches[opcion_num - 1]
            carrito.append({"item": sandwich_seleccionado['nombre'], "precio": sandwich_seleccionado['precio']})
            total += sandwich_seleccionado['precio']
            print(f"\n\t\t✅ {sandwich_seleccionado['nombre']} agregado al carrito - ${sandwich_seleccionado['precio']}")
            esperar_tecla()
        elif opcion_num == len(sandwiches) + 1:
            return carrito, total
        else:
            print("\n\t\t⚠ Opción no válida ⚠")
            esperar_tecla()
    except ValueError:
        print("\n\t\t⚠ Por favor ingrese un número válido ⚠")
        esperar_tecla()
    
    return carrito, total

def seleccionar_postre(carrito, total):
    borrar_pantalla()
    print("\n\t\t\t..::🍰 Postres 🍰::..")
    
    postres = menu["comida"]["postres"]
    for i, postre in enumerate(postres, 1):
        print(f"\t\t{i}️⃣ {postre['nombre']} - ${postre['precio']}")
    print(f"\t\t{len(postres)+1}️⃣ Volver")
    
    opcion = input("\n\t\tSeleccione su postre: ").strip()
    
    try:
        opcion_num = int(opcion)
        if 1 <= opcion_num <= len(postres):
            postre_seleccionado = postres[opcion_num - 1]
            carrito.append({"item": postre_seleccionado['nombre'], "precio": postre_seleccionado['precio']})
            total += postre_seleccionado['precio']
            print(f"\n\t\t✅ {postre_seleccionado['nombre']} agregado al carrito - ${postre_seleccionado['precio']}")
            esperar_tecla()
        elif opcion_num == len(postres) + 1:
            return carrito, total
        else:
            print("\n\t\t⚠ Opción no válida ⚠")
            esperar_tecla()
    except ValueError:
        print("\n\t\t⚠ Por favor ingrese un número válido ⚠")
        esperar_tecla()
    
    return carrito, total

def mostrar_carrito(carrito, total):
    borrar_pantalla()
    print("\n\t\t\t..::🛒 Tu Carrito 🛒::..")
    
    if not carrito:
        print("\n\t\t🛒 Tu carrito está vacío")
    else:
        print("\n\t\t📋 Artículos en tu carrito:")
        for i, item in enumerate(carrito, 1):
            print(f"\t\t{i}. {item['item']} - ${item['precio']}")
        print(f"\n\t\t💰 Total: ${total}")
    
    esperar_tecla()

def realizar_pedido(carrito, total):
    if not carrito:
        print("\n\t\t⚠ No tienes artículos en tu carrito ⚠")
        esperar_tecla()
        return carrito, total
    
    borrar_pantalla()
    print("\n\t\t\t..::💳 Realizar Pedido 💳::..")
    print("\n\t\t📋 Resumen de tu pedido:")
    
    for i, item in enumerate(carrito, 1):
        print(f"\t\t{i}. {item['item']} - ${item['precio']}")
    print(f"\n\t\t💰 Total a pagar: ${total}")
    
    confirmacion = input("\n\t\t¿Confirmar pedido? (s/n): ").lower().strip()
    
    if confirmacion == 's' or confirmacion == 'si':
        print("\n\t\t✅ ¡Pedido confirmado!")
        print("\n\t\t🚀 Tu pedido está siendo preparado...")
        print("\n\t\t⏰ Tiempo estimado: 10-15 minutos")
        carrito.clear()
        total = 0
    else:
        print("\n\t\t❌ Pedido cancelado")
    
    esperar_tecla()
    return carrito, total

if __name__ == "__main__":
    main()