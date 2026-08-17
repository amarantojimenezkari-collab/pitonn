"""
Ejercicio 6.2 — Aplanador de Listas Multidimensionales (Flatten) 
"""


def aplanar_lista(lista_anidada):
    resultado = []
    for elemento in lista_anidada:
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado


if __name__ == "__main__":
    datos = [1, [2, [3, 4], 5], 6, [7]]
    print(aplanar_lista(datos))

    habilidades = ["Python", ["React", ["TypeScript", "Tailwind"]], "Spring Boot"]
    print(aplanar_lista(habilidades))
