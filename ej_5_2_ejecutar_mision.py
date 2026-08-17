"""
Ejercicio 5.2 — Gestor de Tareas Asíncronas Simulado con Hooks
Contexto: simulando el deploy de un proyecto de Clow (Railway/Render) con
hooks de éxito y error, como si fuera un mini CI/CD.
"""

import random


def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    exito = random.choice([True, False])  # simula el resultado del deploy

    if exito:
        resultado = "Deploy completado sin errores"
        if al_exito:
            al_exito(nombre_tarea, resultado)
    else:
        mensaje_error = "Timeout al conectar con el servidor de despliegue"
        if al_error:
            al_error(nombre_tarea, mensaje_error)


def notificar_exito(tarea, resultado):
    print(f"[OK] {tarea}: {resultado}")


def notificar_error(tarea, error):
    print(f"[FALLO] {tarea}: {error}")


if __name__ == "__main__":
    random.seed(1)  # para que el resultado sea reproducible al probar
    ejecutar_mision("Deploy Kenkō v1.3", al_exito=notificar_exito, al_error=notificar_error)
    ejecutar_mision("Deploy Joblify v0.9", al_exito=notificar_exito, al_error=notificar_error)

    # Si no se pasa ningún hook, simplemente no pasa nada visible
    ejecutar_mision("Deploy silencioso")
