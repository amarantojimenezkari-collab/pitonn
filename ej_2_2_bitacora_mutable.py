"""
Ejercicio 2.2 — Refactorización de la Trampa del Parámetro Mutable con ejemplo Clow 
"""

def agregar_bitacora_bug(mensaje, historial=[]):
    historial.append(mensaje)
    return historial
def demostrar_bug():
    print("== Demostración del bug ==")
    ticket_a = agregar_bitacora_bug("Cliente reporta caída del sitio")
    print(f"ticket_a: {ticket_a}")

    ticket_b = agregar_bitacora_bug("Cliente pide cambiar dominio")
    print(f"ticket_b: {ticket_b}  <- arrastró el mensaje del ticket_a")

def agregar_bitacora(mensaje, historial=None):
    if historial is None:
        historial = []  
    historial.append(mensaje)
    return historial


def demostrar_fix():
    print("\n== Versión corregida ==")
    ticket_a = agregar_bitacora("Cliente reporta caída del sitio")
    print(f"ticket_a: {ticket_a}")

    ticket_b = agregar_bitacora("Cliente pide cambiar dominio")
    print(f"ticket_b: {ticket_b}  <- ahora sí, independiente")


if __name__ == "__main__":
    demostrar_bug()
    demostrar_fix()
