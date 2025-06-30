import os
import platform
from datetime import datetime

def borrar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def esperar_tecla():
    input("\n\t\t.::Presione Enter para continuar::. ")

def mostrar_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def validar_entrada_numerica(mensaje, rango_min, rango_max):
    while True:
        try:
            entrada = int(input(mensaje))
            if rango_min <= entrada <= rango_max:
                return entrada
            else:
                print(f"\n\t\t⚠ Por favor ingrese un número entre {rango_min} y {rango_max} ⚠")
        except ValueError:
            print("\n\t\t⚠ Por favor ingrese un número válido ⚠")

def confirmar_accion(mensaje):
    respuesta = input(f"\n\t\t{mensaje} (s/n): ").lower().strip()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']

def mostrar_encabezado(titulo):
    borrar_pantalla()
    print(f"\n\t\t\t..::☕ {titulo} ☕::..")

def formatear_precio(precio):
    return f"${precio:.2f}"

def generar_ticket(carrito, total, usuario):
    ticket = f"""
    {"="*50}
                    CAFETERÍA ☕
    {"="*50}
    Fecha: {mostrar_hora()}
    Cliente: {usuario}
    {"="*50}
    
    ARTÍCULOS:
    """
    
    for i, item in enumerate(carrito, 1):
        ticket += f"    {i}. {item['item']:<30} {formatear_precio(item['precio']):>10}\n"
    
    ticket += f"""
    {"="*50}
    TOTAL: {formatear_precio(total):>40}
    {"="*50}
    
    ¡Gracias por su compra!
    ¡Que disfrute sus productos! ☕🥪
    {"="*50}
    """
    
    return ticket

def guardar_venta(usuario, carrito, total):
    try:
        with open("ventas.txt", "a", encoding="utf-8") as archivo:
            fecha = mostrar_hora()
            archivo.write(f"Fecha: {fecha} | Usuario: {usuario} | Total: ${total}\n")
            for item in carrito:
                archivo.write(f"  - {item['item']}: ${item['precio']}\n")
            archivo.write("-" * 50 + "\n")
        return True
    except Exception as e:
        print(f"\n\t\t⚠ Error al guardar la venta: {e} ⚠")
        return False

def validar_usuario(usuario, usuarios):
    return usuario.upper().strip() in [u.upper() for u in usuarios]

def usuario_existe(usuario, usuarios):
    return usuario.upper().strip() in [u.upper() for u in usuarios]

def mostrar_estadisticas_basicas(usuarios):
    print(f"\n\t\t📊 Usuarios registrados: {len(usuarios)}")
    print(f"\t\t📅 Fecha actual: {mostrar_hora().split()[0]}")