"""
Ejercicio 1.2 — Procesador de Transacciones Financieras (Paso por Asignación) Ejemplo con Planes Clow 
"""


def aplicar_impuesto(tasa_iva, lista_precios):
    print(f"[dentro-antes] tasa_iva: {tasa_iva}")
    print(f"[dentro-antes] lista_precios: {lista_precios}")

    # Intento de "modificar" el escalar: esto solo vuelve a asignar la referencia local
    tasa_iva = tasa_iva + 0.05

    # Modificación real de la lista, elemento por elemento
    for i in range(len(lista_precios)):
        lista_precios[i] = round(lista_precios[i] * (1 + tasa_iva), 2)

    print(f"[dentro-después] tasa_iva (cambio local, no se propaga): {tasa_iva}")
    print(f"[dentro-después] lista_precios (sí se propaga): {lista_precios}")


if __name__ == "__main__":
    tasa_iva = 0.19
    precios_planes = [50000, 120000, 300000]  # planes Starter / Pro / Enterprise

    print(f"[fuera-antes] tasa_iva: {tasa_iva}")
    print(f"[fuera-antes] precios_planes: {precios_planes}")

    aplicar_impuesto(tasa_iva, precios_planes)

    print(f"[fuera-después] tasa_iva: {tasa_iva}          <- NO cambió (inmutable)")
    print(f"[fuera-después] precios_planes: {precios_planes}  <- SÍ cambió (mutable)")
