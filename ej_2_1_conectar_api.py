"""
Ejercicio 2.1 — Configuración Segura de Conexión HTTP / API con valores por omisión para Kenkō
"""


def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    protocolo = "https" if use_ssl else "http"
    comando = (
        f"CONNECT {protocolo}://{url} "
        f"--timeout={timeout}s --retries={retries}"
    )
    return comando


if __name__ == "__main__":
    print(conectar_api("api.kenko.dev/citas"))

    print(conectar_api("api.joblify.dev/postulaciones", timeout=10, retries=1))

    # Conexión insegura explícita (ej. entorno local de desarrollo)
    print(conectar_api("localhost:8080/health", use_ssl=False))
