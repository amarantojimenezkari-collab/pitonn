"""
Ejercicio 3.2 — Sistema de Logging Flexible con Contexto
Contexto: el tipo de log de seguridad que le pondría a Kenkō para auditar
accesos a información sensible del sistema.
"""


def auditar_evento(nivel, *etiquetas, **metadatos):
    partes = [f"[{nivel.upper()}]"]

    if etiquetas:
        tags = ", ".join(f"#{t}" for t in etiquetas)
        partes.append(f"Tags: {tags}")

    if metadatos:
        meta = ", ".join(f"{k}: {v}" for k, v in metadatos.items())
        partes.append(f"Metadatos -> {meta}")

    print(" | ".join(partes))

if __name__ == "__main__":
    auditar_evento("error", "seguridad", "auth",
                    usuario="admin", ip="192.168.1.50", intento=3)

    # Sin etiquetas
    auditar_evento("info", usuario="karla")

    # Sin metadatos
    auditar_evento("warning", "backup")

    # Sin nada extra
    auditar_evento("debug")
