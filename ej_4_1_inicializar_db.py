"""
Ejercicio 4.1 — Inyección de Configuraciones desde JSON / Diccionario
así se vería inicializar la conexión a la base de datos de Kenkō
(Supabase/PostgreSQL) a partir del config leído de un .env o JSON.
"""
def inicializar_db(host, puerto, db_name, usuario, password):
    return (
        f"Conectando a '{db_name}' en {host}:{puerto} "
        f"como '{usuario}' (password oculta por seguridad)"
    )


if __name__ == "__main__":
    config = {
        "host": "cluster-db.internal",
        "puerto": 5432,
        "db_name": "kenko_production",
        "usuario": "app_user",
        "password": "S3cur3P@ss!",
    }
    print(inicializar_db(**config))
