"""
Ejercicio 1.1 — Sistema de Registro de Usuarios y Validación de Roles Simulado Con ejemplo Joblify 
"""


def crear_perfil_usuario(nombre, email, rol):
    if "@" not in email:
        return f"Error: el email '{email}' no es válido, falta el símbolo '@'."

    perfil = {
        "nombre": nombre,
        "email": email,
        "rol": rol,
    }
    return perfil


if __name__ == "__main__":
    # Llamada posicional (el orden importa)
    print(crear_perfil_usuario("Laura Gómez", "laura@empresa.com", "Desarrolladora"))

    # Llamada con argumentos nombrados (el orden ya no importa)
    print(crear_perfil_usuario(rol="Admin", nombre="Carlos", email="carlos_sin_arroba"))

    # Caso extra: un reclutador registrando un talento en Joblify
    print(crear_perfil_usuario(nombre="Karla Ríos", email="karla@joblify.dev", rol="Talento"))
