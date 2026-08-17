# Cuaderno de Ejercicios — Funciones y Parámetros en Python

Cada ejercicio está en su propio archivo `.py`, listo para correr directo
(`python nombre_archivo.py`). Los ejemplos están contextualizados con ejemplos de aplicaciones reales
(Kenkō, Joblify, Clow)

| Archivo | Tema | Qué demuestra |
|---|---|---|
| `ej_1_1_perfil_usuario.py` | Parámetros posicionales y nombrados | Cómo Python resuelve args por posición vs. por nombre, más validación básica de string. |
| `ej_1_2_impuesto_transacciones.py` | Paso por asignación | Por qué una lista SE modifica dentro de una función y un float NO (mutabilidad). |
| `ej_2_1_conectar_api.py` | Valores por omisión | Un parámetro obligatorio + varios opcionales, sobrescribiendo solo lo necesario. |
| `ej_2_2_bitacora_mutable.py` | Trampa del default mutable | El bug clásico de `def f(x=[])` y su arreglo idiomático con `None`. |
| `ej_3_1_calculadora_estadistica.py` | `*args` y `**kwargs` | Recibir cantidad variable de números + opciones nombradas para decidir el cálculo. |
| `ej_3_2_auditar_evento.py` | `*args` + `**kwargs` combinados | Formatear un log condicional según qué llegó y qué no. |
| `ej_4_1_inicializar_db.py` | Desempaquetado `**dict` | Pasar un diccionario completo como argumentos nombrados de una función estricta. |
| `ej_4_2_generar_reporte.py` | Desempaquetado combinado | Desempaquetar una tupla y una lista en la misma llamada, sin fusionarlas antes. |
| `ej_5_1_procesar_coleccion.py` | Callbacks | Pasar funciones (filtro + transformación) como argumentos para un pipeline reusable. |
| `ej_5_2_ejecutar_mision.py` | Hooks de éxito/error | Callbacks opcionales invocados según el resultado interno de una tarea simulada. |
| `ej_6_1_buscar_clave_profunda.py` | Recursión en diccionarios | Buscar una clave en un JSON anidado a N niveles. |
| `ej_6_2_aplanar_lista.py` | Recursión en listas | Aplanar una lista con sublistas anidadas a cualquier profundidad. |
| `ej_7_event_dispatcher.py` | Proyecto integrador | Un mini sistema de eventos (`EventDispatcher`) que junta todo lo anterior. |

## Cómo probarlos
```bash
python ej_1_1_perfil_usuario.py
python ej_1_2_impuesto_transacciones.py
# ...y así con cada uno
```

Todos corren solos porque cada archivo tiene su propio bloque
`if __name__ == "__main__":` con las pruebas del enunciado.


# Karla Amaranto - TDSIS V
