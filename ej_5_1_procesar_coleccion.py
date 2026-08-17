"""
Ejercicio 5.1 — Pipeline de Procesamiento y Filtrado de Datos
Contexto: filtrar y transformar la lista de postulantes de Joblify, por
ejemplo quedarse solo con los que tienen experiencia senior y calcularles
un "score" ajustado.
"""

def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    resultado = []
    for dato in lista_datos:
        if funcion_filtro(dato):
            resultado.append(funcion_transformacion(dato))
    return resultado


if __name__ == "__main__":
    numeros = list(range(1, 21))

    es_par = lambda n: n % 2 == 0
    duplicar = lambda n: n * 2

    print(procesar_coleccion(numeros, duplicar, es_par))

    def es_experiencia_senior(anios):
        return anios >= 5

    def convertir_a_score(anios):
        return anios * 10

    anios_experiencia = [1, 3, 5, 7, 2, 8, 4]
    print(procesar_coleccion(anios_experiencia, convertir_a_score, es_experiencia_senior))
