"""
Ejercicio 6.1 — Navegación de JSON / Diccionarios Profundamente Anidados
Contexto: buscar un campo específico dentro del JSON de configuración de
Kenkō, que puede tener sub-objetos anidados a varios niveles.
"""


def buscar_clave_profunda(estructura, clave_objetivo):
    if not isinstance(estructura, dict):
        return None

    if clave_objetivo in estructura:
        return estructura[clave_objetivo]

    for valor in estructura.values():
        if isinstance(valor, dict):
            encontrado = buscar_clave_profunda(valor, clave_objetivo)
            if encontrado is not None:
                return encontrado

    return None


if __name__ == "__main__":
    config_kenko = {
        "registro": {
            "titulo": "Ficha clínica",
            "contacto": {
                "telefono": "3001234567",
                "direccion": {
                    "ciudad": "Cartagena",
                },
            },
        },
        "clinica_id": "CLI-001",
    }

    print(buscar_clave_profunda(config_kenko, "ciudad"))
    print(buscar_clave_profunda(config_kenko, "telefono"))
    print(buscar_clave_profunda(config_kenko, "no_existe"))
