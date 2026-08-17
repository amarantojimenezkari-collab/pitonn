"""
Ejercicio 3.1 — Calculadora Estadística Multivariable
Es util para sacar métricas rápidas en Joblify, por ejemplo cuántas
postulaciones recibió una vacante por día.
"""


def calcular_metricas(*numeros, **opciones):
    operacion = opciones.get("operacion", "suma")
    redondear = opciones.get("redondear", False)

    if operacion == "promedio":
        resultado = sum(numeros) / len(numeros) if numeros else 0
    elif operacion == "suma":
        resultado = sum(numeros)
    else:
        return f"Error: operación '{operacion}' no soportada."

    if redondear:
        # Si redondear=True -> 0 decimales; si es un entero -> esa cantidad
        decimales = redondear if isinstance(redondear, int) and not isinstance(redondear, bool) else 0
        resultado = round(resultado, decimales)

    return resultado


if __name__ == "__main__":
    postulaciones_por_dia = [12, 8, 15, 9, 20]

    print(calcular_metricas(*postulaciones_por_dia, operacion="suma"))
    print(calcular_metricas(*postulaciones_por_dia, operacion="promedio"))
    print(calcular_metricas(*postulaciones_por_dia, operacion="promedio", redondear=True))
    print(calcular_metricas(*postulaciones_por_dia, operacion="promedio", redondear=2))
