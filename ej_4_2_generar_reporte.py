"""
Ejercicio 4.2 — Fusión y Desempaquetado Combinado de Listas y Tuplas
Contexto: armar el reporte semanal que Clow le manda a un cliente, con
secciones fijas y secciones extra según el proyecto.
"""


def generar_reporte(titulo, *secciones, **firmas):
    print(f"--- {titulo} ---")
    for i, seccion in enumerate(secciones, start=1):
        print(f"{i}. {seccion}")
    if firmas:
        print("Firmado por:")
        for rol, nombre in firmas.items():
            print(f"  - {rol}: {nombre}")


if __name__ == "__main__":
    secciones_fijas = ("Resumen ejecutivo", "Horas invertidas")
    secciones_extra = ["Bugs resueltos", "Próximos pasos"]

    generar_reporte(
        "Reporte semanal - Cliente XYZ",
        *secciones_fijas,
        *secciones_extra,
        desarrolladora="Karla",
        pm="Isabel",
    )
